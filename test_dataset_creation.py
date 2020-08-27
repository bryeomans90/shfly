import numpy as np
from dataset_creation import (
    clean_96_overlap, prod_cat2_nan_fill, rename_categories, get_months_before, get_weeks_before
)


def test_clean_96_overlap():
    in_data = [
        [0,1],
        [3,96],
        [7,96]
    ]
    obs = [clean_96_overlap(x[0], x[1]) for x in in_data]
    exp = [0,7,7]
    assert obs == exp


def test_prod_cat2_nan_fill():
    in_data = [
        [1,np.nan],
        [2,np.nan],
        [3,199],
        [1,2]
    ]
    obs = [prod_cat2_nan_fill(x[0], x[1]) for x in in_data]
    exp = [-1,-2, 199, 2]
    assert obs == exp, f'obs:{obs}, exp:{exp}'


def test_rename_categories():
    obs = rename_categories(0,'It_Worked!')
    exp = '0:It_Worked!'
    assert obs == exp


def test_get_months_before():
    input_data = [0, 11, 100, 120]
    obs = [get_months_before(x) for x in input_data]
    exp = [1, 1, 4, 5]
    assert obs == exp


def test_get_weeks_before():
    input_data = [0,1,8,13,41,22]
    obs = [get_weeks_before(x) for x in input_data]
    exp = [1,1,2,2,6,4]
    assert obs == exp