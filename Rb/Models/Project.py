from Rb.Models.BaseModel import BaseModel


class Project(BaseModel):
    base_url_projects = ""
    rot = ""

    def __init__(self, config):
        super().__init__(config)

        self.base_url_projects = self.base_url + "project-api/projects/"

    def get_project(self, project_id):
        p = self.api.get_json(self.base_url_projects + project_id)
        self.rot = p["rot"]
        return p

    def get_projects(self):
        p = self.api.get_json(self.base_url_projects)
        return p




