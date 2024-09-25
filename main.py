import os
import time
import logging

import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

api_url = os.getenv('API_URL')
api_key = os.getenv('API_KEY')
loop_interval = int(os.getenv('LOOP_INTERVAL', 60))

if not api_url or not api_key:
    logger.error("Please set the API_URL and API_KEY environment variables.")
    exit(1)

if not api_url.startswith("http://") and not api_url.startswith("https://"):
    logger.warning("No protocol found in API_URL, using default: https://")
    api_url = "https://" + api_url

if api_url.endswith("/"):
    api_url = api_url[:-1]

if not api_url.endswith("/api/v1"):
    api_url += "/api/v1"

logger.debug(f"Using API_URL: {api_url}")

headers = {
    'Authorization': 'Bearer ' + api_key,
}

response = requests.get(api_url + '/routes', headers=headers)

while True:
    start_time = time.time()
    for route in response.json()['routes']:
        if not route["enabled"]:
            logger.warning(f"Route {route['id']} is disabled")
            response = requests.post(api_url + '/routes/' + route["id"] + '/enable', headers=headers)
            if response.status_code == 200:
                logger.info(f"Route {route['id']} enabled")
            else:
                logger.error(f"Failed to enable route {route['id']}")
    logger.info("OK")

    remaining = loop_interval - (time.time() - start_time) % loop_interval
    logger.info(f"Sleeping for {remaining} seconds")
    time.sleep(remaining)
