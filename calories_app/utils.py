import requests
import json

def get_product_from_barcode(barcode):
    endpoint = "https://world.openfoodfacts.org/api/v0/product/"
    raw_data = requests.get(endpoint + str(barcode) + ".json")
    if raw_data.status_code != 200:
        return None
    
    content = json.loads(raw_data.text)
    return content if content["status"] == 1 else None