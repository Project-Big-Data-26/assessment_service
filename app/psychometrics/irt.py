"""Unidimensional logistic IRT using regularized marginal likelihood.

The latent scale is fixed to N(0,1); Gauss-Hermite quadrature integrates
abilities out. Missing cells contribute no likelihood. This is a local
calibration, not equating across populations, forms, grades, or versions.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import minimize
from scipy.special import expit, logsumexp

from .contracts import AnalysisPolicy


def response_probability(theta, a, b, c=0.0):
    return np.asarray(c) + (1 - np.asarray(c)) * expit(np.asarray(a) * (np.asarray(theta) - np.asarray(b)))


def fit_irt(matrix: np.ndarray, model: str, policy: AnalysisPolicy) -> dict:
    """Fit after readiness checks. Public callers should use analyze_matrix."""
    if model not in {"rasch", "2pl", "3pl"}:
        raise ValueError("unsupported IRT model")
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2 or not matrix.size or np.isinf(matrix).any():
        raise ValueError("IRT requires a finite binary matrix with NaN for missing cells")
    if not np.isin(matrix[~np.isnan(matrix)], [0, 1]).all():
        raise ValueError("IRT requires dichotomous scores")
    observed = (~np.isnan(matrix)).astype(float)
    scores = np.nan_to_num(matrix, nan=0.0)
    incorrect = observed - scores
    item_count = matrix.shape[1]
    nodes, weights = hermgauss(policy.quadraturePoints)
    theta = nodes * np.sqrt(2)
    log_weights = np.log(weights / np.sqrt(np.pi))
    p0 = (scores.sum(axis=0) + 0.5) / (observed.sum(axis=0) + 1)
    initial_b = np.clip(np.log((1 - p0) / p0), -3, 3)
    initial = initial_b
    bounds = [(-5.0, 5.0)] * item_count
    if model != "rasch":
        initial = np.r_[initial, np.zeros(item_count)]
        bounds += [(np.log(0.2), np.log(4.0))] * item_count
    if model == "3pl":
        initial = np.r_[initial, np.full(item_count, 0.15)]
        bounds += [(0.001, 0.35)] * item_count

    def unpack(parameters):
        b = parameters[:item_count]
        a = np.ones(item_count) if model == "rasch" else np.exp(parameters[item_count:2 * item_count])
        c = parameters[2 * item_count:] if model == "3pl" else np.zeros(item_count)
        return a, b, c

    def posterior(parameters):
        a, b, c = unpack(parameters)
        logistic = expit(a[None, :] * (theta[:, None] - b[None, :]))
        probabilities = np.clip(c + (1 - c) * logistic, 1e-12, 1 - 1e-12)
        joint = scores @ np.log(probabilities).T + incorrect @ np.log1p(-probabilities).T + log_weights
        normalizer = logsumexp(joint, axis=1)
        return np.exp(joint - normalizer[:, None]), normalizer, probabilities, logistic

    def objective(parameters):
        a, b, c = unpack(parameters)
        post, normalizer, probabilities, logistic = posterior(parameters)
        expected_correct = post.T @ scores
        expected_count = post.T @ observed
        residual = (expected_correct - expected_count * probabilities) / (probabilities * (1 - probabilities))
        common = (1 - c) * logistic * (1 - logistic)
        gradient_b = -np.sum(residual * (-a * common), axis=0)
        # Weak proper priors make extreme response patterns numerically finite.
        penalty = np.sum(b ** 2) / 18
        gradients = [gradient_b + b / 9]
        if model != "rasch":
            log_a = parameters[item_count:2 * item_count]
            gradient_a = -np.sum(residual * common * a * (theta[:, None] - b), axis=0)
            penalty += np.sum(log_a ** 2) / (2 * 0.75 ** 2)
            gradients.append(gradient_a + log_a / 0.75 ** 2)
        if model == "3pl":
            # Beta(5,17) prior: lower asymptote is estimated, not 1/option count.
            penalty -= np.sum(4 * np.log(c) + 16 * np.log1p(-c))
            gradients.append(-np.sum(residual * (1 - logistic), axis=0) - 4 / c + 16 / (1 - c))
        return float(-normalizer.sum() + penalty), np.concatenate(gradients)

    result = minimize(
        objective, initial, method="L-BFGS-B", jac=True, bounds=bounds,
        options={"maxiter": policy.maxIterations, "ftol": policy.tolerance, "gtol": 1e-5},
    )
    if not np.isfinite(result.fun) or not np.isfinite(result.x).all():
        raise FloatingPointError("IRT optimizer produced non-finite estimates")
    a, b, c = unpack(result.x)
    post, normalizer, probabilities, _ = posterior(result.x)
    eap = post @ theta
    posterior_sd = np.sqrt(np.maximum(0, post @ (theta ** 2) - eap ** 2))
    warnings = []
    if not result.success:
        warnings.append("optimizer_not_converged")
    boundary = [index for index, (value, bound) in enumerate(zip(result.x, bounds, strict=True))
                if min(value - bound[0], bound[1] - value) < 1e-3]
    if boundary:
        warnings.append("parameter_at_boundary")
    # Posterior-curvature uncertainty includes cross-item covariance. It is not
    # an unpenalized frequentist SE and must be labelled accordingly.
    standard_errors = None
    if result.success and not boundary:
        step = 1e-4
        hessian = np.empty((len(result.x), len(result.x)))
        for column in range(len(result.x)):
            shift = np.zeros(len(result.x)); shift[column] = step
            hessian[:, column] = (objective(result.x + shift)[1] - objective(result.x - shift)[1]) / (2 * step)
        hessian = (hessian + hessian.T) / 2
        if np.linalg.eigvalsh(hessian).min() > 1e-7:
            standard_errors = np.sqrt(np.diag(np.linalg.inv(hessian)))
        else:
            warnings.append("uncertainty_not_identified")

    person_p = response_probability(eap[:, None], a, b, c)
    variance = np.clip(person_p * (1 - person_p), 1e-9, None)
    squared_residual = (scores - person_p) ** 2 * observed
    counts = observed.sum(axis=0)
    infit = squared_residual.sum(axis=0) / (variance * observed).sum(axis=0)
    outfit = (squared_residual / variance).sum(axis=0) / counts
    item_parameters = []
    grid = np.linspace(-3, 3, 25)
    grid_p = response_probability(grid[:, None], a, b, c)
    logistic = expit(a * (grid[:, None] - b))
    derivative = (1 - c) * a * logistic * (1 - logistic)
    information = derivative ** 2 / np.clip(grid_p * (1 - grid_p), 1e-12, None)
    for index in range(item_count):
        b_sd = float(standard_errors[index]) if standard_errors is not None else None
        item_parameters.append({
            "a": float(a[index]), "b": float(b[index]), "c": float(c[index]),
            "bPosteriorSd": b_sd,
            "bInterval95": [float(b[index] - 1.96 * b_sd), float(b[index] + 1.96 * b_sd)] if b_sd is not None else None,
            "infit": float(infit[index]), "outfit": float(outfit[index]),
            "empiricalDifficulty": "Easy" if b[index] < policy.easyB else "Hard" if b[index] > policy.hardB else "Medium",
        })
    log_likelihood = float(normalizer.sum())
    parameter_count = len(result.x)
    return {
        "status": "estimated" if not warnings else "estimated_with_warnings",
        "model": model, "method": "regularized_marginal_likelihood_gauss_hermite",
        "scale": "theta ~ N(0,1); logistic D=1; no cross-population linking",
        "priors": {"b": "N(0,3^2)", "logA": "N(0,0.75^2)" if model != "rasch" else None,
                   "c": "Beta(5,17), bounded [0.001,0.35]" if model == "3pl" else None},
        "converged": bool(result.success), "iterations": int(result.nit),
        "logLikelihood": log_likelihood,
        "aic": 2 * parameter_count - 2 * log_likelihood,
        "bic": parameter_count * np.log(matrix.shape[0]) - 2 * log_likelihood,
        "informationCriteriaCaveat": "descriptive at regularized estimates; not a model-selection approval",
        "warnings": warnings, "items": item_parameters,
        "persons": [{"thetaEap": float(value), "posteriorSd": float(sd), "answeredItems": int(count)}
                    for value, sd, count in zip(eap, posterior_sd, observed.sum(axis=1), strict=True)],
        "testInformation": {"theta": grid.tolist(), "information": information.sum(axis=1).tolist()},
    }
