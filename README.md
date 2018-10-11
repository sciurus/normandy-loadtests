# Normandy Load tests

This project uses [pipenv](https://pipenv.readthedocs.io/en/latest/) to manage dependencies.
After checking out this repo, run the following commands to create the virtual environment and
install the required dependencies.

`pipenv install`

`pipenv shell`

The load tests were written using [Molotov](https://molotov.readthedocs.io/en/stable/)
and can be started using the following command:

`molotov -c -v api_tests.py`

Check the Molotov documentation for details on other options available to run the tests.

