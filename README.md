# FOG Python Client

This repository contains python scripts used to interface with Free Open-source Ghost (FOG).

##Usage

First you need to install the dependencies:

`pip3 install -r requirements.txt`

Then you need to setup your .env file:

`cp .env-model .env`

The .env file needs to have the FOG server's api and user keys, they can be found at the settings page of your FOG server.

`FOG_API_TOKEN="server's api token`

`FOG_USER_TOKEN="user's api token`

Then you can use the deploy script:

`python3 deploy.py [HOST1] [HOST2] [HOST3] `

The `HOST` stands for the hostname associated with the machine in the FOG server.
