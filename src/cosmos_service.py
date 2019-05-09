import requests
from requests.exceptions import HTTPError
import certificate_service
import json
import time
import os

cosmosApiBase = "https://cosmos.api.bbci.co.uk";
def getInstances(serviceName, environment):
    try:
        response = requests.get(
            f"{cosmosApiBase}/v1/services/{serviceName}/{environment}/main_stack/instances",
            cert=certificate_service.getCertificateLocation()
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json();

def getLoginInstance(serviceName, environment, instance = 0):
    instances = getInstances(serviceName, environment);
    return instances['instances'][instance]

def createLogin(serviceName, environment, instance = 0):
    instanceToLoginTo = getLoginInstance(serviceName, environment, instance)
    try:
        payload = { "instance_id" : instanceToLoginTo["id"] }
        response = requests.post(
            f"{cosmosApiBase}/v1/services/{serviceName}/{environment}/logins",
            data=json.dumps(payload),
            cert=certificate_service.getCertificateLocation(),
            headers={ "Content-Type" : "application/json" }
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.json();

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
        return response.json();

def login(serviceName, environment, instance = 0):
    if certificate_service.certificatesExist():
        login = createLogin(serviceName, environment, instance = 0)
        loginAvailability = getLoginAvailability(login['login']['ref'])
        while loginAvailability['status'] != 'current':
            print(f"login status {loginAvailability['status']}")
            time.sleep(1)
            loginAvailability = getLoginAvailability(login['login']['ref'])
        # look at replacing with subprocess
        return os.system(f"ssh {loginAvailability['instance_private_ip']},eu-west-1")
    else:
        print("certificates are not set")