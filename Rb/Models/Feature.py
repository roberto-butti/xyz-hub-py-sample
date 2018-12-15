from Rb.Models.BaseModel import BaseModel


class Feature(BaseModel):
    base_url_feature = ""

    def __init__(self, config):
        super().__init__(config)
        self.base_url_feature = self.base_url + "hub/spaces/{0}/search"

    def get_features(self, sid, rot=None):
        url = self.base_url_feature.format(sid)
        if rot is None:
            rot = self.rot
        f = self.api.get_json(url, rot, 'application/geo+json')
        return f
