![Build & Test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-2/actions/workflows/build.yaml/badge.svg)

# `thisday`

`thisday` is a package that accesses onthisday.com to give the user events that occurred for that day.


## How to use the package

It is recommended to install the package in a virtual environment, though one can install globally by using `pip` instead of `pipenv` where it appears should they please.

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
3. Learn about what happened on this day!

## Test program

## Package functions

### run
<strong>Params:</strong> args(argument for the function)<br>
<strong>Returns:</strong> content retrieved from website if runs correctly, or an error message if something went wrong.<br>
<strong>Description:</strong> Main driver function of the package

### process_input
<strong>Params:</strong> inputString(a string for input)<br>
<strong>Returns:</strong> the input string if it is valid, or an error message if it is not.<br>
<strong>Description:</strong> Function to check if the argument is valid for the package

### connect
<strong>Params:</strong> option(a string returned from process_input)<br>
<strong>Returns:</strong> A BeautifulSoup object generated from the website if option is valid, or 0 if option is invalid<br>
<strong>Description:</strong> Function to connect to the respective URL for each input option

### get_events
<strong>Params:</strong> soup(a BeautifulSoup object returned from connect)<br>
<strong>Returns:</strong> a list of strings retrieved from the website, or 0 if failed to retrieve<br>
<strong>Description:</strong> Function to retrieve data from the URL

### show
<strong>Params:</strong> my_data(a list of strings returned from get_events)<br>
<strong>Returns:</strong> a string if the list is valid, or 0 if not<br>
<strong>Description:</strong> Function that displays data to the user

## Contributing to the package

## PyPI Page
[Package on PyPI]()

## Authors

[Anvi Agarwal](https://github.com/agarwalanvi01) \
[Leo Xu](https://github.com/Leo6016) \
[Otis Lu](https://github.com/OtisL99) \
[Danilo Montes](https://github.com/danilo-montes)