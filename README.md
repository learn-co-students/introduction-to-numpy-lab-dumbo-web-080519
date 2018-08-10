
# Practicing NumPy

## Introduction

Now that we have introduced NumPy, let's put it to practice. In this lab, we are going to be creating arrays, performing operations on them, and returning new array all using the NumPy library. Let's get started!

## Objectives
* Create a NumPy Array
* Operate on the NumPy Array to return an Array with new values

## Instructions

Create a NumPy Array for each of the following:
    1. Using a range
    2. Using a Python List
    
Below, create a list in Python that has 5 elements (i.e. [0,1,2,3,4]) and assign it to the variable `py_list`. 

Next, do the same, but instead of a list, create a range with 5 elements and assign it to the variable, `py_range`.

Finally, use the list and range to create NumPy arrays and assign the array from list to the variable `array_from_list`, and the array from the range to the variable `array_from_range`.


```python
import numpy as np
```


```python
py_list = None
py_range = None
array_from_list = None
array_from_range = None
```

Next, we have a list of heights and weights and we'd like to use them to create a collection of BMIs. However, they are both in inches and pounds (imperial system), respectively. 

Let's use what we know to create NumPy arrays with the metric equivalent values, (height in meters & weight in kg).

> **Remember:** *NumPy can make these calculations a lot easier and with less code than a list!*

> 1.0 inch = 0.0254 meters

> 2.2046 lbs = 1 kilogram


```python
# use the conversion rate for turning height in inches to meters
list_height_inches = [65, 68, 73, 75, 78]
array_height_inches = None
array_height_meters = None
```


```python
# use the conversion rate for turning weight in pounds to kilograms
list_weight_pounds = [150, 140, 220, 205, 265]
array_weight_punds = None
array_weight_kg = None
```

The metric formula for calculating BMI is as follows:

> BMI = weight (kg) ÷ height^2 (m^2)

So, to get BMI we divide weight by the squared value of height. For example, if i weighed 130kg and was 1.9 meters tall, the calculation would look like:

> BMI = 130 / (1.9*1.9)

Use the BMI calculation to create a NumPy array of BMIs


```python
BMI_array = None
```

## Summary

In this lab, we practiced creating NumPy arrays from both lists and rages. We then practiced peforming math operations like converting imperial measurements to metric measurements on each element of a NumPy array to create new arrays with new values. Finally, we used both of our new NumPy arrays to operate on eachother and create new arrays containing the BMIs from our arrays containing heights and weights.
