import requests
from requests.exceptions import HTTPError
import src.certificate_service as certificate_service
import src.proxy_service as proxy_service
import json
import time
import os

COSMOS_API = "https://cosmos.api.bbci.co.uk"
API_VERSION = "v1"
AWS_REGION = "eu-west-1"

def getInstances(serviceName, environment):
    try:
        response = requests.get(
            f"{COSMOS_API}/v1/services/{serviceName}/{environment}/main_stack/instances",
            cert=certificate_service.getCertificateLocation(),
            proxies=proxy_service.getProxies()
        )
        response.raise_for_status()
    except HTTPError as http_err:
        if http_err.response.status_code == 404:
            print(f"No service named {serviceName} found in {environment} environment")
            raise SystemExit
        print(f"HTTPError: {http_error}")
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json()


def getLoginInstance(serviceName, environment, instance=0):
    instances = getInstances(serviceName, environment)
    return instances['instances'][instance]


def createLogin(serviceName, environment, instance=0):
    instanceToLoginTo = getLoginInstance(serviceName, environment, instance)
    try:
        payload = {"instance_id": instanceToLoginTo["id"]}
        response = requests.post(
            f"{COSMOS_API}/{API_VERSION}/services/{serviceName}/{environment}/logins",
            data=json.dumps(payload),
            cert=certificate_service.getCertificateLocation(),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json()


def getLoginAvailability(loginRefUri):
    try:
        response = requests.get(
            loginRefUri,
            cert=certificate_service.getCertificateLocation()
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json()


def login(serviceName, environment, instance=0):
    if certificate_service.certificateValuesExported():
        login = createLogin(serviceName, environment, instance)
        loginAvailability = getLoginAvailability(login['login']['ref'])
        while loginAvailability['status'] != 'current':
            print(f"login status {loginAvailability['status']}")
            time.sleep(1)
            loginAvailability = getLoginAvailability(login['login']['ref'])
        instanceIp = loginAvailability['instance_private_ip']
        return os.system(f"ssh {instanceIp},{AWS_REGION}")
    else:
        print("certificates are not set")
