# pythonapp - Sample app for package installation and testing

## Package Creation

Create a package named mypackage with following structure:
  
* Create a new folder named `pythonapp`
* Inside `pythonapp`, create a folder `mypackage`
* Create an empty `__init__.py` file inside `mypackage`
* Create **modules** `welcome.py` and `mymath.py`
* Create `tests/test.py` for testing the code

That's it. package named `mypackage` is created.

## Importing a Module from a Package

To test this package, navigate to `pythonapp` folder and invoke the `python` prompt

```
> python
```

Import `mymath` module from the `mypackage` package and call its `power()` function.

```
>>> from mypackage import mymath
>>> mymath.power(3, 2)
9
```

## __init__.py

The package contains a special file called `__init__.py`, which stores the package's content. It serves two purposes:
* The Python interpreter recognizes a folder as the package if it contains `__init__.py` file.
* `__init__.py` exposes specified resources from its modules to be imported.

An empty `__init__.py` file makes all functions from the above modules available when this package is imported. 

The `__init__.py` file is normally kept empty. However, it can also be used to choose specific functions from modules in the package folder and make them available for import.


## Install a pacakge globally

The package can be installed for system-wide use by running the `setup` script (in parent folder). The script calls `setup()` function from the `setuptools` module. The setup() function takes various arguments such as name, version, author, list of dependencies, etc. The zip_safe argument defines whether the package is installed in compressed mode or regular mode.

Run the following command to install `mypackage` using pip3 utility

```
▶ pip3 install mypackage  
Collecting mypackage
  Using cached Mypackage-0.1-py3-none-any.whl
Installing collected packages: mypackage
Successfully installed mypackage-0.1

```

To verify that pacakge is installed

```
▶ python3
>>> import mypackage
>>> mypackage.average(20, 30)
25.0
>>> 
```

Equivalently following command uninstall the package

```
▶ pip3 uninstall mypackage
Found existing installation: Mypackage 0.1
Uninstalling Mypackage-0.1:
  Would remove:
    /usr/local/bin/shell
    /usr/local/lib/python3.9/site-packages/Mypackage-0.1.dist-info/*
    /usr/local/lib/python3.9/site-packages/Mypackage/*
Proceed (Y/n)? Y
  Successfully uninstalled Mypackage-0.1
```

## Testing

There are many test runners available for Python. The one built into the Python standard library is called `unittest`.

Sample code for testing using `unittest` is in `tests/test.py`, which can be run as follows:

```
> cd pythonapp/mypackage/
     
▶ python3 -m unittest -v tests/test.py 
test_average (tests.test.TestMypackage) ... ok
test_power (tests.test.TestMypackage) ... ok
test_sum (tests.test.TestMypackage) ... ok
```
