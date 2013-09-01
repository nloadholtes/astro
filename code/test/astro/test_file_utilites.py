from nose.tools import assert_equal
from nose import SkipTest

from astro.file_utilites import load_orbital_parameters

@SkipTest
def test_load_orbital_parameters():
    assert_equal(1,2)
    