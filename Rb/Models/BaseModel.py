import uuid
from Rb.Api import Api


class BaseModel:
    uuid = ""
    base_url = ""

    def __init__(self, config):
        self.uuid = str(uuid.uuid4())
        self.base_url = config.hostname
        self.rot = ""
        self.api = Api()
