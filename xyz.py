import json
import requests
import argparse


__author__ = "Roberto B."

base_url = "https://xyz.api.here.com/"
base_url_projects = base_url + "project-api/projects/"
base_url_spaces = base_url + "hub/spaces"
rot = ""

parser = argparse.ArgumentParser(description='XYZ Studio Project Inspector.')
parser.add_argument('--pid', help='Project Identifier')
args = parser.parse_args()
print(args.pid)
project_id = args.pid



def get_json(url, token = None):
    headers = {}
    if ( token != None ):
        headers = {'Authorization': 'Bearer ' + token}

    with requests.get(url, headers = headers) as response:
        data = json.loads(response.text)
        print(json.dumps(data, indent=4))
    return data




try:
    print("Retrieving project " + project_id)
    data = get_json(base_url_projects+project_id)

    rot = data["rot"]
    print(rot)
    print("Retrieving spaces")
    data = get_json(base_url_spaces, rot)

    for d in data:
        my_url = base_url_spaces+"/"+d["id"]+"/statistics"
        print(my_url)
        stats = get_json(my_url, rot)


    print("ok")



except:
    print("There was an error")

