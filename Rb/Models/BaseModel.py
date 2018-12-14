import uuid
from Rb.Api import Api


class BaseModel:
    uuid = ""
    #base_url = "https://xyz.api.here.com/"
    base_url = "https://xyz.cit.api.here.com/"

    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self.rot = ""
        self.api = Api()
