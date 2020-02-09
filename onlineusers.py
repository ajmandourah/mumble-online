#!/usr/bin/python3

import json, urllib.request

jsonurl = urllib.request.urlopen("CVP_URL_HERE")
rawdata = json.load(jsonurl)
data = rawdata['root']['channels']
userlist = []

def getUsrs():
    for channel in data:
        usersinfo = channel['users']
        for userinfo in usersinfo:
            name = userinfo['name']
            userlist.append(name)
    userlist.remove("MUSICBOT_NAME")
    print(userlist)

getUsrs()
