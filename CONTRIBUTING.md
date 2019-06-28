# Contributing

## Local Development

- Install:
  - `virtualenv venv -p python3` <!-- Make sure this is Python 3.5+ -->
  - `source venv/bin/activate`
  - `pip install -e .[dev]`
- Docs Build:
  - `make html`
  - `open docs/index.html`
- Testing:
  - `pytest --cov=elizur test/`
- Checking Code Quality:
  - `black --exclude venv .`
  - `pylint elizur/`

## Pull Requests

Please fork this repository and submit PRs via your fork

- Pull Request Requirements
    - New tests and compatibility with old tests
    - Accurate documentation
    - Compatible with Python 3.5+

## Creating and Tracking Issues

Create or track issues [here](https://github.com/trollefson/elizur/issues)

## Releases

All releases will follow [semantic versioning](https://semver.org) and be published to PyPi.
