#!/bin/bash

poetry run flake8 ./ --exclude venv,build,dist --statistics
poetry run safety check --bare
ENV=test poetry run pytest --cov=ytdl tests/*.py
rm -rf ./ptester
