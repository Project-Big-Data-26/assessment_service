import importlib

import pytest


@pytest.mark.parametrize(
    "module_name",
    [
        "datasets",
        "matplotlib",
        "numpy",
        "pandas",
        "seaborn",
        "sentencepiece",
        "sklearn",
        "torch",
        "transformers",
        "yaml",
    ],
)
def test_required_dependency_can_be_imported(module_name: str) -> None:
    assert importlib.import_module(module_name) is not None
