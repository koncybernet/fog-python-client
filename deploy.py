#!/usr/bin/env python3

import json
from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv()

def loadDefaultConfig():
    config = {
    "baseURL": "http://fog.c3.furg.br",
    "fog-api-token": os.getenv("FOG_API_TOKEN"),
    "fog-user-token": os.getenv("FOG_USER_TOKEN"),
    }
    return config

def readConfig():
    try:
        with open("config.json") as jsonData:
            config = json.load(jsonData)
        pass
    except FileNotFoundError as e:
        print("No config.json detected!")
        exit(1)
        raise

def writeConfig(data):
    with open('config.json', 'w') as outfile:
        json.dump(data, outfile)


def main(argv):

    if not (os.path.exists("config.json")):
        writeConfig(config)
    else:
        readConfig()

    print("FOG Deploy script: Rafael Souza <rsouza19796@gmail.com>")
    print("Total Machines to Image: " + str(len(argv)))

    for x in range(len(argv)):
        print ("Sending request to machine #" + str(x) + ": " + argv[x])
        deployFogCurrentImage(getFogTaskTypeId("Deploy"), getFogHostID(argv[x]))

    print("Done, thanks for using me!")

def getFogHostID(name):
    searchURL=config["baseURL"] + "/fog/host/search/" + name
    r = requests.get(searchURL, headers=headers)
    return (r.json()['hosts'][0]['id'])

def getFogTaskTypeId(name):
    searchURL=config["baseURL"] + "/fog/tasktype"
    r = requests.get(searchURL, headers=headers)
    tasktypes = r.json()['tasktypes']
    for type in tasktypes:
        if (type['name'] == name):
            return type['id']

def deployFogCurrentImage(taskTypeID, hostID):
    taskURL=config["baseURL"] + "/fog/host/" + hostID + "/task"
    data = json.dumps({
        "taskTypeID": taskTypeID,
        "shutdown": 'true',
        "wol": 'true'
    }).encode('utf8')
    r = requests.post(taskURL, data=data, headers=headers)
    return (r.json())


config = loadDefaultConfig()
headers = {
"fog-api-token": config["fog-api-token"],
"fog-user-token": config["fog-user-token"],
"Content-Type": "application/json"
}

if (__name__ == "__main__"):
    main(sys.argv[1:])
