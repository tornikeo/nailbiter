import json
import requests

SERVER_URL = 'http://localhost:8501/v1/models/model:predict'


def predict(instances:list, signature_name='serving_default'):
    '''
    Thin wrapper around tf serving's prediction protocol.
    
    instances must be a list of shape (batch_size, height, width, 3)
    '''
    data = json.dumps({
        "signature_name": signature_name,
        "instances": instances,
    })
    
    # print(input_data_json)
    response = requests.post(
            SERVER_URL, 
            data=data
        )
    response.raise_for_status() # raise an exception in case of error

    return response.json()

