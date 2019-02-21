import uuid
from Rb.Api import Api
from Rb.Models.Project import Project
from Rb.Models.Space import Space
from Rb.Models.Feature import Feature
from Rb.Models.Fit import Fit
from Rb.Config import Config
from flask import render_template
import json


class controllers():

    def __init__(self):
        pass

    def project_list(self):
        config = Config()
        config.load()
        print(config.hostname)
        project = Project(config)
        print("Retrieving projects ")
        p = project.get_projects()
        return p
        # return render_template("project_list.html", data=p)
        # return p
        # print(json.dumps(p, indent=1))
        # return json.dumps(p, indent=1)


    def project_detail(self, id):
        config = Config()
        config.load()
        print(config.hostname)
        project = Project(config)
        print("Retrieving projects ")
        p = project.get_project(id)
        return p


    def space_detail(self, id, rot):



        config = Config()
        config.load()
        print(config.hostname)
        space = Space(config)
        print("Retrieving space " + id)
        s = space.get_space(id, rot)
        return s
