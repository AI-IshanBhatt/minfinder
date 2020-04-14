# Problem Statement

 Implement a Python module, which can be installed using pip**, including tests, with the following functionality: Given an array of elements that provide a less than operator, find the minimum using as few comparisons as possible. The array shall be given such that the first few elements are strictly monotonically decreasing, the remaining elements are strictly monotonically increasing. The less than operator be defined as the operator that works on such arrays where a < b if min(a,b) == a.
 
## Installation
This package is not published on pypi.org, so to install it you need to build it by yourself.

`python setup.py test`

`python setup.py sdist bdist_wheel`

`pip install dist/minfinder-0.0.1-py3-none-any.whl`

OR (If you are a fan of Makefile)
```
make test
make buildproject
make install
```

## Usage
```
from minfinder import *
arr = [100, 90, 80, 50, 55, 59, 75, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]
minimum(arr)
50

minimum([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/ishanbhatt/MINFINDER/minfinder/minfinder/minfinder.py", line 24, in minimum
    raise ValueError("Empty Array supplied")
ValueError: Empty Array supplied
```

## Note
It will be an array of elements which has \__lt__ method implemented, otherwise it will throw TypeError.

## Using tox
```
tox
tox -e end
```
