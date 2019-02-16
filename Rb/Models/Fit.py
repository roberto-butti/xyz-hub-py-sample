from Rb.Models.BaseModel import BaseModel
from fitparse import FitFile, FitParseError
from geojson import Feature, Point, FeatureCollection
import json
import datetime

# https://pythonhosted.org/fitparse/
def default_timestamp_format(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


class Fit(BaseModel):
    def __init__(self, config):
        super().__init__(config)

    def parse_fit(self, fit_file):
        try:
            fitfile = FitFile(fit_file)
        except FitParseError as e:
            print("Error while parsing .FIT file: {0}".format(e))
            return None
        except FileNotFoundError:
            print("File not exists: {0}".format(fit_file))
            return None

        i=1
        features_array = []
        for record in fitfile.get_messages('record'):
            record_values = record.get_values()
            r = 0
            for record_data in record:
                if record_data.units:
                    r = r+1
                    print(" * %s: %s %s" % (
                        record_data.name, record_data.value, record_data.units,
                    ))
                else:
                    r = r + 1
                    # print(" * %s: %s" % (record_data.name, record_data.value))
            # print("---------------"+str(i))
            i=i+1
            latitude = record_values["position_lat"] * ( 180 / 2147483648)
            longitude = record_values["position_long"] * ( 180 / 2147483648)
            p = Point( (longitude, latitude) )
            f =Feature(geometry=p, properties=record_values)
            features_array.append(f)
        feature_collection = FeatureCollection(features_array)
        with open(fit_file + '.json', 'w') as outfile:
            outfile.write(json.dumps(feature_collection, sort_keys=True, indent=1, default=default_timestamp_format))
            outfile.close()
        return None

