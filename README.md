# MEMEGEN

## DESCRIPTION

A meme generator site written in Python, based on principles of DDD and TDD. It consists of 4 different domains running on separate Docker containers:
- Front, based on Django
- Generator domain, based on Flask and Pillow
- Listing domain, based on Flask
- Storage domain, based on Flask and SQLAlchemy

## Functionality

# Front

Front receives data from the user in form of an image file and bottom/top text, and sends it to Generator domain in POST request for further processing. Front also sends a GET request to Listing domain, asking to return either a list of all created memes or list of meme templates.

# Generator

Generator receives data from Front and processes it in three steps:
- Validation
- Meme generation
- Thumbnail generation

If all three steps are successfull, it then sends image data containing the meme and thumbnails to Storage domain through an adapter.

# Listing

Listing domain queries the Storage domain based on user's inputs and returns requested data back to Front domain.

# Storage

Storage domain uses and queries its PostreSQL database to save data sent by Generator domain and requested by Listing domain.

## Run it yourself!

Each domain can by ran as a discrete microservice. Each one includes a Makefile which automates testing, code style checking, runs the domain locally, deploys it and prepares development environment.

- `make develop` prepares virtual environment and installs requirements

- `make test` runs unittests based on pytest and pytest coverage extension

- `make codestyle` inspects code style using flake8

- `make ci-unit` runs tests and codestyle inspection

- `make install` installs requirements outside of virtual environment

- `make run` runs the service locally.