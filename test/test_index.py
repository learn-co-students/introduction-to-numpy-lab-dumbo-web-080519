import pytest
import numpy as np
from ipynb.fs.full.index import py_list, py_range, array_from_list, array_from_range, array_height_inches, array_height_meters, array_weight_pounds, array_weight_kg BMI_array

list_height_inches = [65, 68, 73, 75, 78]
list_weight_pounds = [150, 140, 220, 205, 265]


def test_py_list():
    assert type(py_list) == type([])
    assert len(py_list) == 5

def test_py_range():
    assert type(py_range) == type(range(0,1))
    assert len(py_range) == 5

def test_array_from_list():
    assert np.array(py_list) == array_from_list

def test_array_from_range():
    assert np.array(py_range) == array_from_range

def test_array_height_inches():
    array = create_array()
    assert type(array) == type(array_height_inches)

def test_array_height_meters():
    array = create_array([1.651, 1.7272, 1.8542, 1.905, 1.9812])
    assert type(array) == type(array_height_meters)
    assert array_height_meters == array

def test_array_weight_kg():
    array = create_array([68.03955366, 63.50358342, 99.79134537, 92.98739, 120.20321147])
    assert type(array) == type(array_weight_kg)
    assert array_height_meters == array

def test_array_BMI():
    array = create_array([24.9613063, 21.28692715, 29.02550097, 25.62324316, 30.62382485])
    assert type(array) == type(BMI_array)
    assert array_height_meters == array

def create_array(example_list=[1,2]):
    return np.array(example_list)
