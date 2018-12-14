import json

import argparse
from Rb.Models.Project import Project
from Rb.Models.Space import Space
from Rb.Models.Feature import Feature



p = Project()

__author__ = "Roberto B."

def input_project(args):
    # print(args.pid)
    project_id = args.pid

    if project_id:
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
    else:
        project = Project()
        print("Retrieving projects ")
        p = project.get_projects()
        print(len(p))


def input_space(args):
    space = Space()
    s = space.get_space(args.sid, args.rot)
    print(s)
    if (args.statistics):
        s = space.get_space_statistics(args.sid, args.rot)
        print(s)




def input_features(args):
    feature = Feature()
    f = feature.get_features(args.sid, args.rot)
    print(f)


parser = argparse.ArgumentParser(prog='xyz', description='XYZ Studio Project Inspector.')
subparsers = parser.add_subparsers(help='Managing projects, spaces, feautres', dest='operation')

parser_project = subparsers.add_parser('project', help='Managing XYZ Projects')
parser_project.add_argument('--pid', help='Project Identifier')
parser_project.set_defaults(func=input_project)

parser_space = subparsers.add_parser('space', help='Managing XYZ Spaces')
parser_space.add_argument('--sid', help='Space Identifier')
parser_space.add_argument('--rot', help='ROT, Read Only Token')
parser_space.add_argument('--statistics', help='Include Statistics')
parser_space.set_defaults(func=input_space)

parser_features = subparsers.add_parser('feature', help='Managing XYZ Features')
parser_features.add_argument('--sid', help='Space Identifier')
parser_features.add_argument('--fid', help='Feature Identifier')
parser_features.add_argument('--rot', help='ROT, Read Only Token')
parser_features.set_defaults(func=input_features)

args = parser.parse_args()

if (args.operation is None):
    print("Operation is missing.")
else:
    args.func(args)

print("Well done!")

