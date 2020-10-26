# pytestcwd

A simple wrapper around pytest to add current working dir to **sys.path**.

Working as a replacement for `python -m pytest tests` when `pytest tests` won't find your module in current working dir.

## Installation
You can use [pipx](https://pipxproject.github.io/pipx/) and have **pytestcwd** globally available via command line:
```
pipx install pytestcwd
```
If you prefer you can also use pip:
```
pip install pytestcwd
```

## Usage
```
pytestcwd tests
```
### v0.1.0