/* Pedagogical calculations; pure functions mirrored from cited backend recipes.
 * This module never fits IRT item parameters or invokes a provider/API.
 * CommonJS export makes numerical verification possible with node:test. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.FlowMath = api;
})(typeof window === 'object' ? window : this, function () {
  'use strict';
  const finite = x => typeof x === 'number' && Number.isFinite(x);
  function softmax(logits, temperature = 1) {
    if (!Array.isArray(logits) || logits.length < 2 || !logits.every(finite) || !finite(temperature) || temperature <= 0) throw new RangeError('Logits finite dan temperature > 0 diperlukan.');
    const scaled = logits.map(x => x / temperature);
    const maximum = Math.max(...scaled);
    const exp = scaled.map(x => Math.exp(x - maximum));
    const total = exp.reduce((a, b) => a + b, 0);
    return exp.map(x => x / total);
  }
  function entropy(probabilities) {
    if (!Array.isArray(probabilities) || probabilities.length < 2 || !probabilities.every(x => finite(x) && x >= 0)) throw new RangeError('Distribusi probabilitas tidak valid.');
    const sum = probabilities.reduce((a, b) => a + b, 0);
    if (sum <= 0) throw new RangeError('Jumlah probabilitas harus positif.');
    return Math.max(0, Math.min(1, -probabilities.reduce((a, value) => { const p = value / sum; return a + (p > 0 ? p * Math.log(p) : 0); }, 0) / Math.log(probabilities.length)));
  }
  function route(probabilities, confidenceThreshold, entropyThreshold, policy) {
    const confidence = Math.max(...probabilities), h = entropy(probabilities);
    const reasons = [];
    if (!finite(confidenceThreshold) || confidenceThreshold <= 0 || (policy === 'confidence-entropy-v1' && !finite(entropyThreshold))) reasons.push('selective_threshold_gate_not_met');
    else {
      if (confidence < confidenceThreshold) reasons.push('confidence_below_validation_threshold');
      if (policy === 'confidence-entropy-v1' && h > entropyThreshold) reasons.push('entropy_above_validation_threshold');
    }
    return { confidence, entropy: h, action: reasons.length ? 'review' : 'predict', reasons, reviewRequired: true };
  }
  function sigmoid(x) { return x >= 0 ? 1 / (1 + Math.exp(-x)) : Math.exp(x) / (1 + Math.exp(x)); }
  function ordinal(score, first, gap) {
    if (![score, first, gap].every(finite)) throw new RangeError('Score dan cutpoint harus finite.');
    const second = first + Math.max(gap, 0) + Math.log1p(Math.exp(-Math.abs(gap))) + 0.0001;
    const q1 = sigmoid(score - first), q2 = sigmoid(score - second);
    // Python head clamps torch dtype epsilon and renormalizes; these examples
    // stay far from the epsilon boundary, with double precision arithmetic.
    const p = [1 - q1, q1 - q2, q2].map(x => Math.max(Number.EPSILON, x));
    const total = p.reduce((a, b) => a + b, 0);
    return { second, q1, q2, probabilities: p.map(x => x / total) };
  }
  function irt(theta, a, b, c = 0) {
    if (![theta, a, b, c].every(finite) || a <= 0 || c < 0 || c >= 1) throw new RangeError('Parameter IRT tidak valid.');
    const l = sigmoid(a * (theta - b)), p = c + (1 - c) * l;
    const derivative = (1 - c) * a * l * (1 - l);
    return { p, derivative, information: derivative ** 2 / Math.max(p * (1 - p), 1e-12) };
  }
  function wilson(correct, total) {
    if (!Number.isInteger(correct) || !Number.isInteger(total) || total <= 0 || correct < 0 || correct > total) throw new RangeError('r dan n harus bulat, 0 ≤ r ≤ n, n > 0.');
    const p = correct / total, z = 1.96, d = 1 + z * z / total;
    const center = (p + z * z / (2 * total)) / d;
    const half = z * Math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / d;
    const low = Math.max(0, center - half), high = Math.min(1, center + half);
    return { p, low, high, width: high - low };
  }
  function stableBand(interval, easyP = 0.7, hardP = 0.3) {
    if (interval.low > easyP) return 'Easy';
    if (interval.high < hardP) return 'Hard';
    if (interval.low >= hardP && interval.high <= easyP) return 'Medium';
    return null;
  }
  function empiricalDifficulty(b) { return b < -1 ? 'Easy' : b > 1 ? 'Hard' : 'Medium'; }
  function eap(items, responses, quadrature) {
    if (items.length !== responses.length || !responses.every(x => x === null || x === 0 || x === 1)) throw new RangeError('Pola respons harus 0, 1, atau null.');
    const values = quadrature.theta.map((theta, index) => {
      let logJoint = Math.log(quadrature.weights[index]);
      items.forEach((item, j) => {
        if (responses[j] === null) return;
        const p = Math.max(1e-12, Math.min(1 - 1e-12, irt(theta, item.a, item.b, item.c).p));
        logJoint += responses[j] === 1 ? Math.log(p) : Math.log1p(-p);
      });
      return logJoint;
    });
    const max = Math.max(...values), unnormalized = values.map(x => Math.exp(x - max));
    const z = unnormalized.reduce((a, b) => a + b, 0), posterior = unnormalized.map(x => x / z);
    const mean = posterior.reduce((a, p, i) => a + p * quadrature.theta[i], 0);
    const second = posterior.reduce((a, p, i) => a + p * quadrature.theta[i] ** 2, 0);
    return { mean, sd: Math.sqrt(Math.max(0, second - mean * mean)), posterior, logJoint: values, answered: responses.filter(x => x !== null).length };
  }
  return { softmax, entropy, route, sigmoid, ordinal, irt, wilson, stableBand, empiricalDifficulty, eap };
});
