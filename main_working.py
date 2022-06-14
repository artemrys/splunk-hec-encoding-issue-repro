import json
import time

import requests

while True:
    event = {
        "index": "main",
        "event": {"name": "goodbye", "value": "こんにちは世界"},
    }
    response = requests.post(
        "http://127.0.0.1:8088/services/collector/event",
        headers={"Authorization": "Splunk <your-hec-token>"},
        data=json.dumps(event, ensure_ascii=False).encode("utf-8"),
    )
    print(f"Event is sent, status code: {response.status_code}")
    time.sleep(5)
