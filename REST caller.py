# Import the good stuff here
import requests  # Read more about how to use the requests module at https://2.python-requests.org/en/master/
import time
from datetime import datetime


def caller_get(url, header, body, param, msg):  # Main caller function for GET requests
    response = requests.get(url, headers=header, json=body, params=param)
    if response.ok:
        return response
    else:
        return response.status_code


def caller_post(url, header, body, param, msg):  # Main caller function for POST calls
    response = requests.post(url, headers=header, json=body, params=param)
    if response.ok:
        return response
    else:
        return response.status_code


def caller_put(url, header, body, param, msg):  # Main caller function for PUT calls
    response = requests.put(url, headers=header, json=body, params=param)
    if response.ok:
        return response
    else:
        return response.status_code


def caller_opt(url, header, body, param, msg):  # Main caller function for PUT calls
    response = requests.options(url, headers=header, json=body, params=param)
    if response.ok:
        return response
    else:
        return response.status_code


def caller_delete(url, header, body, param, msg):  # Main caller function for POST calls
    response = requests.delete(url, headers=header, json=body, params=param)
    if response.ok:
        return response
    else:
        return response.status_code
