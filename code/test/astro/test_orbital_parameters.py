from nose.tools import assert_equal
# from nose import SkipTest

from astro.orbital_parameters import TRITON


def test_TRITON():
    assert_equal(157.345, TRITON.inclination)
