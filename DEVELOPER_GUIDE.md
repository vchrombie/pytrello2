# Developer Guide

## Forking and Cloning the Project

1. Fork the [pytrello2](https://github.com/5-jigglypuff/pytrello2) repository to
   your own GitHub account.
2. Clone your forked repository to your local machine
```bash
git clone https://github.com/<your-username>/pytrello2
```

## Creating a branch

When working on changes, create a separate branch instead of working directly on
`master`
```bash
git checkout -b <branch-name>
```

See GitHub docs on [creating
branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches).

## Setting Up the Project

1. Install the required dependencies using
   [Poetry](https://python-poetry.org/docs/)
```bash
cd pytrello2/
poetry install
```
2. Activate the virtual environment using Poetry
```bash
poetry shell
```

## Run Tests

Before committing changes, run tests to catch any regressions:
```bash
pytest
```

## Run Linting & Formatting

In addition to tests, run linting and formatting checks:
1. Lint with flake8
```bash
flake8
```
2. Format code with black
```bash
black .
```

Fix any failures before proceeding.

## Commit and Push Changes
Once tests pass and there are no linting/formatting issues, commit changes:
```bash
git add .
git commit -m "Description of changes"
```

Then, push commits to the remote branch.

## Opening a Pull Request

Once you have pushed your branch, open a pull request against the upstream
repository on GitHub following the pull request process.

The changes in the pull request will be reviewed before merging.

Follow the [Contributing Guidelines](./CONTRIBUTING.md) for more information.
