# Modules and Packages in Python:
# Module: is a simple python file.
# Packages: is a collection of modules or python files. its must have __init__.py file.
# Libraries: pandas,numpy,scipy etc. its a module.
# Framework: Django,Flask,Bottle etc. ist callend packages.
# modules: 
# A module is a single Python file that contains variables, functions, and classes.
# Modules allow you to organize your code logically by grouping related functionality together.
# You can create your own modules or use built-in modules provided by Python.
# To use a module in your code, you can import it using the import statement.
# Ex:
# import xyz
# so here xyz is a module.
# Ex:
# import random
# l = [1, 3, 4, 5]
# x = random.choice(l)
# print(x)
# o/p->5 
# using random module we print any random number from the list.
# Package: 
# A package is a collection of Python modules organized in a directory hierarchy.
# Packages allow you to group related modules together in a directory structure, making it easier to manage and organize larger projects.
# A package directory must contain a special file named __init__.py, which can be empty or can contain initialization code for the package.
# You can have nested packages, where a package can contain sub-packages and modules.
# To import a module from a package, you can use dot notation to specify the package and module names.
# For example, if you have a package named my_package containing a module named my_module, you can import it as follows:
# Ex:
# import my_package.my_module
# Alternatively, you can use the from keyword to import specific functions or classes from a module within a package:
# from my_package import my_module
# Ex: 
# from random import choice
# use "as" keyword: 
# some packages have long name so you can use short name as per your comfort.
# Ex:
# import pandas as pd 
# so here pd is user defined name.
# Use "*" wildcard symbol to import:
# if you want all the files in the modules so you can use *.
# Ex:
# from datetime import *
# Diffrent types of to importing from the module:
# (1) import random
# (2) from random import choice
# (3) from random import *
# (4) import random as rd
# (5) use For package:
# import random
# random.choices
# # So here . is use to import from the package.
# (6) if you want any info related module and packages use dir() function.
# import math
# print(dir(math))
# o/p->
# ['__doc__', '__loader__', '__name__', 
#  '__package__', '__spec__', 'acos', 'acosh', 'asin', 
#  'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb',
#    'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 
#    'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 
#    'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 
#    'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
#      'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log',
#        'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh',
#   'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']







