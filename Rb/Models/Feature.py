from Rb.Models.BaseModel import BaseModel
import json


class Feature(BaseModel):
    base_url_feature = ""

    def __init__(self, config):
        super().__init__(config)
        self.base_url_feature = self.base_url + "hub/spaces/{0}/iterate"

    # https://xyz.api.here.com/hub/static/swagger/#/Read_Features/iterateFeatures
    def get_features(self, sid, rot=None):
        url = self.base_url_feature.format(sid)
        if rot is None:
            rot = self.rot
        f = self.api.get_json(url, rot, 'application/geo+json')

        return json.dumps(f, indent=2)
