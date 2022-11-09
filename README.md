![Build & Test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-2/actions/workflows/build.yaml/badge.svg)

# `thisday`

`thisday` is a command line tool that accesses onthisday.com to give the user events that occurred for that day.


## How to use the package

It is recommended to install the package in a virtual environment, though one can install globally by using `pip` instead of `pipenv` where it appears should they please.

<strong>Note that this package is intended for command line use only.</strong>

1. install `thisday` via `pipenv`
```
$ pipenv install thisday
```
2. enter virtual environment
```
$ pipenv shell
```
3. use the terminal to type the command `thisday [option]`, valid options include: history, film-tv, sport, music
```
$ thisday history

$ thisday film-tv

$ thisday sport

$ thisday music
```
4. Learn about what happened on this day!

5. To exit the virtual environment, run the `exit` command within the shell (skip if not using a virtual environment)
```
$ exit
```

## Test program
We have provided a [shell script](func_example.sh) demonstrating the functionality of our package.

## Package functions

### `run`
<strong>Params:</strong> `args` (argument for the function) \
<strong>Returns:</strong> content retrieved from website if runs correctly, or an error message if something went wrong \
<strong>Description:</strong> Main driver function of the package

### `process_input`
<strong>Params:</strong> `inputString` (a string for input) \
<strong>Returns:</strong> the input string if it is valid, or an error message if it is not \
<strong>Description:</strong> Function to check if the argument is valid for the package

### `connect`
<strong>Params:</strong> `option` (a string returned from process_input) \
<strong>Returns:</strong> A BeautifulSoup object generated from the website if option is valid, or 0 if option is invalid \
<strong>Description:</strong> Function to connect to the respective URL for each input option

### `get_events`
<strong>Params:</strong> `soup` (a BeautifulSoup object returned from connect) \
<strong>Returns:</strong> a list of strings retrieved from the website, or 0 if failed to retrieve \
<strong>Description:</strong> Function to retrieve data from the URL

### `show`
<strong>Params:</strong> `my_data` (a list of strings returned from get_events) \
<strong>Returns:</strong> a string if the list is valid, or 0 if not \
<strong>Description:</strong> Function that displays data to the user

## Testing locally

If you would like to test the package, download the package files to your machine. Then, within the directory of the download, follow the steps 1 and 2 in [how to use the package](#how-to-use-the-package) to create and enter the virtual environment, then run the following command to run the test file:
```
$ pytest
OR 
$ python3 -m pytest
```

Tip: When working on the package, it might be helpful to install the package in editable mode, so that changes to the package are immediately updated in the virtual environment. To do this, run `pipenv install -e .` from the main directory of the project

## Authors

[Anvi Agarwal](https://github.com/agarwalanvi01) \
[Danilo Montes](https://github.com/danilo-montes) \
[Leo Xu](https://github.com/Leo6016) \
[Otis Lu](https://github.com/OtisL99)

## PyPI Page
[Package on PyPI](https://pypi.org/project/thisday/)