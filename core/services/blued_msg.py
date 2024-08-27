import requests
from dotenv import load_dotenv
import os
load_dotenv()

def send(uuid: str, id: int):
    data = {
        'hashId': uuid,
        'templateId': id,
        "param1": os.getenv("WEB_URL")
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(os.getenv("BLUED_API"), json=data, headers=headers).json() # {code, msg}
    return response