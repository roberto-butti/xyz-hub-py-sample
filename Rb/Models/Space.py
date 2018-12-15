from Rb.Models.BaseModel import BaseModel

class Space(BaseModel):
    base_url_spaces = ""

    def __init__(self, config):
        super().__init__(config)
        self.base_url_spaces = self.base_url + "hub/spaces"

    def get_spaces(self, rot=None):
        if rot is None:
            rot = self.rot
        url = self.base_url_spaces
        s = self.api.get_json(url, rot)
        return s

    def get_space(self, sid, rot=None):
        if rot is None:
            rot = self.rot
        url = self.base_url_spaces+"/"+sid
        s = self.api.get_json(url, rot)
        return s

    def get_space_statistics(self, sid, rot=None):
        if rot is None:
            rot = self.rot
        url = self.base_url_spaces+"/"+sid+"/statistics"
        s = self.api.get_json(url, rot)
        return s