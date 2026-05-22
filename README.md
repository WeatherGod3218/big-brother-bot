# Big Brother Bot ![Static Badge](https://img.shields.io/badge/weather-%23b16ded?style=flat&logo=github&logoColor=black&labelColor=0%2C0%2C0&link=https%3A%2F%2Fgithub.com%2FweatherGod3218%2F)
Discord Bot for our Discord Server

![image](./docs/images/theman.jpg)
Documentation for the project can be found be appended /docs to the url
All HTML requests that are sent in the project can be seen by appending /swag

This project uses Python and [FastAPI](https://fastapi.tiangolo.com/).

## Installing
1. Clone and cd into the repo: git clone https://github.com/WeatherGod3218/big-brother-bot
>> Make another branch if your working on a large thing!

## Setup
1. Make sure you have docker installed
>> (OPTIONAL): You can use docker compose as well!!
2. Copy the .env.template file, rename it to .env and place it in the root folder

## Run

Big Brother is containerized through a docker file.

1. Build the docker file
```
    docker build -t Big-Brother .
```
2. Run the newly built docker on port 8000
```
    docker run -p 8080:80 Big-Brother
```

## Docker Compose

Big Brother also has support for Docker Compose, a extended version of docker that simplifies the steps.

(This is a really cool thing! If you use docker often, check it out!)
```
    docker compose up
```

## Development

### Setup
1. Install uv on your system if not already on it (this just makes it easy)
2. Run: `uv venv .venv`
3. Activate the virtual environment
    * Bash: `source .venv/bin/activate`
    * Fish: `source .venv/bin/activate.fish`
    * Windows: `.venv\Scripts\activate`
    * Other: Good luck!
4. Run:
    * `uv pip install -r dev-requirements.txt`
    * `uv pip install -r src/requirements.txt`
    * `uv pip install -r tests/requirements,txt`
    * `uv pip install -r docs/requirements.txt`
5. Run: `pre-commit install`
6. You're all set!

