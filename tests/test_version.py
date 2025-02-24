"""Unit tests for __version__.py."""

import hw5_helpers_pkg


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(hw5_helpers_pkg, "__version__")
    assert hw5_helpers_pkg.__version__ != "0.0.0"
