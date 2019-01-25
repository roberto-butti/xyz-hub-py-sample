from Rb.Models.BaseModel import BaseModel
import json
from fitparse import FitFile


class Fit(BaseModel):
    #base_url_feature = ""

    def __init__(self, config):
        super().__init__(config)
        #self.base_url_feature = self.base_url + "hub/spaces/{0}/iterate"

    def parse_fit(self, fit_file):
        fitfile = FitFile(fit_file)
        i=1
        for record in fitfile.get_messages('record'):
        # Go through all the data entries in this record
            print(record)
            print(record.get_values())
            for record_data in record:
                
                # Print the records name and value (and units if it has any)
                #print(record_data)
                if record_data.units:
                    print(" * %s: %s %s" % (
                        record_data.name, record_data.value, record_data.units,
                    ))
                else:
                    print(" * %s: %s" % (record_data.name, record_data.value))
            print("---------------"+str(i))
            i=i+1
        
        return None

