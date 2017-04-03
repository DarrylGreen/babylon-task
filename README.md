# babylon-task

## Installing and running the tests

This test suite was tested on a Debian machine and assumes that python and pip are installed. If pip is not installed, instructions can be found [here](https://packaging.python.org/installing)

This test suite is run using py.test and requires the pytest and requests packages to be installed. Install them simply by doing the following:

	pip install pytest
	pip install requests

Once these are installed, navigate to the directory containing the tests. To run all the tests, simply run:

	py.test

This will run all the tests, hiding all output from tests that have passed and showing all the tests that have failed.

If you wish to run a subset of the tests, the tests have been marked using pytest marks. Each test has a mark for which API call it is testing, either GET, POST, PATCH or DELETE, and another for whether it was passing or failing at the latest update of this repository. To run tests with a specific mark, do the following:

	py.test -m {mark}

where {mark} is one of get, post, patch, delete, passing or failing.