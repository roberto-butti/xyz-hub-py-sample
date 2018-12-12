import json

import argparse
from Rb.Models.Project import Project
from Rb.Models.Space import Space
from Rb.Models.Feature import Feature



p = Project()

__author__ = "Roberto B."


parser = argparse.ArgumentParser(description='XYZ Studio Project Inspector.')
parser.add_argument('--pid', help='Project Identifier')
parser.add_argument('--sid', help='Space Identifier')
parser.add_argument('--rot', help='ROT, Read Only Token')
args = parser.parse_args()
print(args.pid)
print(args.sid)
print(args.rot)
project_id = args.pid

try:
    if args.pid:
        project = Project()
        print("Retrieving project " + project_id)
        p = project.get_project(project_id)
        rot = project.rot

        project_id = p["id"]
        print("Project: " + p["id"] + " Read access only token: " + rot)
        print("Retrieving spaces")
        space = Space()
        space.rot = rot
        spaces = space.get_spaces()
        for s in spaces:
            print("Space:" + s["id"] + " - " + s["title"])



    if args.sid and args.rot:
        space = Space()
        s = space.get_space(args.sid, args.rot)
        print(s)
        feature = Feature()
        f = feature.get_features(args.sid, args.rot)
        print(f)



    print("Well done!")



except:
    print("There was an error")

