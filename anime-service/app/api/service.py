import os
import httpx

STUDIO_SERVICE_HOST_URL = "https://localhost:8002/api/v1/studio/"
url = os.environ.get('STUDIO_SERVICE_HOST_URL') or STUDIO_SERVICE_HOST_URL

def is_studio_present(studio_id: int):
    r = httpx.get(f'{url}{studio_id}')
    return True if r.status_code == 200 else False