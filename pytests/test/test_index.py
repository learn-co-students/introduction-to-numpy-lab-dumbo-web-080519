import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose
from ipynb.fs.full.index import py_list, py_range, array_from_list, array_from_range, array_height_inches, array_height_meters, array_weight_pounds, array_weight_kg, BMI_array

list_height_inches = [65, 68, 73, 75, 78]
list_weight_pounds = [150, 140, 220, 205, 265]

def test_py_list():
    assert type(py_list) == type([])
    assert len(py_list) == 5

def test_py_range():
    assert type(py_range) == type(range(0,1))
    assert len(py_range) == 5

def test_array_from_list():
    # asserts that the py_list has been created
    assert py_list
    array = create_array(py_list)
    assert_array_equal(array_from_list, array, err_msg="Oh no! make sure to use the py_list to create your NumPy array")

def test_array_from_range():
    # asserts that the py_range has been created
    assert py_range
    array = create_array(py_range)
    assert_array_equal(array_from_range, array, err_msg="Oh no! make sure to use the py_range to create your NumPy array")

def test_array_height_inches():
    array = create_array()
    assert type(array) == type(array_height_inches)

def test_array_height_meters():
    array = create_array([1.651, 1.7272, 1.8542, 1.905, 1.9812])
    assert type(array) == type(array_height_meters)
    assert_allclose(array_height_meters, array, err_msg="Oh no! make sure to use the use the correct conversion for inches to meters")

def test_array_weight_kg():
    array = create_array([68.03955366, 63.50358342, 99.79134537, 92.98739, 120.20321147])
    assert type(array) == type(array_weight_kg)
    assert_allclose(array_weight_kg, array, err_msg="Oh no! make sure to use the use the correct conversion for pounds to kilograms")

def test_array_BMI():
    array = create_array([24.9613063, 21.28692715, 29.02550097, 25.62324316, 30.62382485])
    assert type(array) == type(BMI_array)
    assert_allclose(BMI_array, array, err_msg="Make sure to use NumPy arrays to perform your BMI calculation and double check your calculation")

def create_array(example_list=[1,2]):
    return np.array(example_list)
