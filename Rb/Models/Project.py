from Rb.Models.BaseModel import BaseModel


class Project(BaseModel):
    base_url_projects = ""
    rot = ""

    def __init__(self):
        super().__init__()
        self.base_url_projects = self.base_url + "project-api/projects/"

    def get_project(self, project_id):
        p = self.api.get_json(self.base_url_projects + project_id)
        self.rot = p["rot"]
        return p






