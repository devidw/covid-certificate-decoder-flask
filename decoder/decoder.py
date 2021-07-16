import base45
import zlib
import cbor2
import json


def decode(cert):
    """decode eu-covid-health-certivate qr-codes plain text to json"""
    # remove 'HC1:' (Healh Certificate Version 1)
    base45_data = cert[4:]
    zlib_data = base45.b45decode(base45_data)
    cbor_data = zlib.decompress(zlib_data)
    cbor_data = cbor2.loads(cbor_data)
    json_data = cbor2.loads(cbor_data.value[2])
    json_data = json.dumps(json_data, indent=2)
    object = json.loads(json_data)
    object = object['-260']['1']
    return object
