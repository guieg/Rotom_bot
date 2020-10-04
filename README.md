# Rotom Bot
> Rotom is a telegram bot made to help pokémon go groups with raid organization.

## Requirements

- Python 3.8 or later;
- Pip;
- MongoDB;
- A telegram account of course :D

## Setup

### Telegram Bot

To run this bot you need to create your bot on telegram using the Father Bot:

- https://core.telegram.org/bots#3-how-do-i-create-a-bot

The Father bot will give you a bot token, type your token on "Rotom" from [credetials file](creds/tokens.json).


### MongoDB

If you want to connect the bot to a cloud MongoDB you have to access the [credetials file](creds/tokens.json) and type your MongoDB url on "AppURL":

```json
{
	"Rotom": "telegram token",
	"OP": "your telegram user id, just if you want OP's functionalities",
	"AppURL": "mongodb server url",
	"LocalURL": "mongodb local url for tests",
	"DB": "database name from mongodb"
}
```

If you only want to run this bot locally you can install mongodb using one of the following methods:

1. Installing MongoDB following this [tutorial](https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials).

    After installed run the following comands to start mongodb.

    On most linux distros, it can be started or stopped with:

    ```sh
    service start mongod
    service stop mongod
    ```

2. Pulling a MongoDB container image from Docker Hub with the following command (this require docker installed on your machine): 

    ```sh 
    docker pull mongo # pull image

    docker create -p 27017:27017 --name mongodb mongo # create a container as a service on port 27017
    ```

    It can be started or stoped with:

    ```sh
    docker start mongodb
    docker stop mongodb
    ```

Is very recommended that you choose to run with docker because it will work in any OS since it has docker installed.

Once MongoDB is running in your machine, just type your local url on "AppURL" and "LocalURL" from [credetials file](creds/tokens.json).


## Installation

Using docker:

```sh
docker build -t rotom .
```

Normally:

```sh
pip install -r requirements.txt
```

## Run

Using docker:

```sh
docker run -it --rm --network host rotom
```

Normally:

```sh
python3 src/main.py
```