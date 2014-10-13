__author__ = 'msteiger'

import logging
import json
import urllib2
import httplib

logging.basicConfig(level=logging.DEBUG)

githubUrl = 'https://api.github.com/orgs/Terasology/repos'

logging.info('Downloading ' + githubUrl)
data = urllib2.urlopen(githubUrl)
jsonOrgs=json.load(data)

mods = {}

for entry in jsonOrgs:
    url = entry["html_url"] + '/raw/master/' + 'module.txt'
    id = entry["name"]
    logging.info('Downloading ' + url)
    try:
        response = urllib2.urlopen(url)
        moduleJson = json.load(response)
        mods[id] = moduleJson
    except urllib2.HTTPError, e:
        logging.info('HTTPError = ' + str(e.reason))
    except urllib2.URLError, e:
        logging.error('URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
        logging.error('HTTPException')

with open('index.json', 'w') as jsonFile:
    json.dump(mods, jsonFile, indent=4)
