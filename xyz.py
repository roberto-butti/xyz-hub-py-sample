import json

import argparse
from Rb.Models.Project import Project
from Rb.Models.Space import Space
from Rb.Models.Feature import Feature
from Rb.Config import Config


__author__ = "Roberto B."


config = Config()
config.load()
print(config.hostname)


def input_project(args):
    # print(args.pid)
    project_id = args.pid

    if project_id:
        project = Project(config)
        print("Retrieving project " + project_id)
        p = project.get_project(project_id)
        rot = project.rot
        project_id = p["id"]
        print("Project: " + p["id"] + " Read access only token: " + rot)
        if args.spaces:
            print("Retrieving spaces")
            space = Space(config)
            space.rot = rot
            spaces = space.get_spaces()
            for s in spaces:
                print("Space:" + s["id"] + " - " + s["title"])
    else:
        project = Project(config)
        print("Retrieving projects ")
        p = project.get_projects()
        if (args.show):
            print(p)
        else:
            print(len(p))


def input_space(args):

    if (args.list):
        space = Space(config)
        s = space.get_spaces(args.rot)
        print(json.dumps(s, indent=2))
    else:
        space = Space(config)
        s = space.get_space(args.sid, args.rot)
        print(s)
        if (args.statistics):
            s = space.get_space_statistics(args.sid, args.rot)
            print(s)




def input_features(args):
    feature = Feature(config)
    f = feature.get_features(args.sid, args.rot)
    print(f)


parser = argparse.ArgumentParser(prog='xyz', description='XYZ Studio Project Inspector.')
subparsers = parser.add_subparsers(help='Managing projects, spaces, feautres', dest='operation')

parser_project = subparsers.add_parser('project', help='Managing XYZ Projects')
parser_project.add_argument('--pid', help='Project Identifier')
#parser_project.add_argument('show')
parser_project.add_argument('--show', action='store_const', const=True, help='Show also the Project Json')
parser_project.add_argument('--spaces', action='store_const', const=True, help='Show also the list of spaces related to the Project')

parser_project.set_defaults(func=input_project)

parser_space = subparsers.add_parser('space', help='Managing XYZ Spaces')
parser_space.add_argument('--list', action='store_const', const=True, help='Show all spaces')
parser_space.add_argument('--sid', help='Space Identifier')
parser_space.add_argument('--rot', help='ROT, Read Only Token')
parser_space.add_argument('--statistics', action='store_const', const=True, help='Include Statistics')
parser_space.set_defaults(func=input_space)

parser_features = subparsers.add_parser('feature', help='Managing XYZ Features')
parser_features.add_argument('--sid', help='Space Identifier')
parser_features.add_argument('--fid', help='Feature Identifier')
parser_features.add_argument('--rot', help='ROT, Read Only Token')
parser_features.set_defaults(func=input_features)

args = parser.parse_args()
# print(args)
if (args.operation is None):
    print("Operation is missing.")
    parser.print_help()
else:
    args.func(args)

# print("Well done!")

