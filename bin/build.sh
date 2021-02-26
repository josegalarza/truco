#!/usr/bin/env bash
REPO_ROOT=$(git rev-parse --show-toplevel)
# Install environment
pipenv install
# Test
pipenv run python -m pytest "${REPO_ROOT}"/src
