# Import the good stuff here
import requests  # Read more about how to use the requests module at https://2.python-requests.org/en/master/
import file_logging
import time
from datetime import datetime


# Global stuff here
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")  # Not used unless you want timestamps for the console output


# Logging handler to simplify turning on/off logging
def response_logging(response, url, msg):
    # file_logging.logger(response, url, msg)  # used to save response in log files, comment out to stop saving
    resp = response.text  # In case you want to print response as text without logging it


# Functions below here

def caller_get(url, header, body, param, msg):  # Main caller function for GET requests
    response = requests.get(url, headers=header, json=body, params=param)
    if response.ok:
        if response.content:
            response_logging(response, url, msg)
            file_logging.success += 1
            return response
        else:
            file_logging.success += 1
            return response
    else:
        file_logging.error_logging(response, url, msg)
        file_logging.fail += 1
        return response


def caller_post(url, header, body, param, msg):  # Main caller function for POST calls
    response = requests.post(url, headers=header, json=body, params=param)
    if response.ok:
        if response.content:
            response_logging(response, url, msg)
            file_logging.success += 1
            return response
        else:
            file_logging.success += 1
            return response
    else:
        file_logging.error_logging(response, url, msg)
        file_logging.fail += 1
        return response


def caller_put(url, header, body, param, msg):  # Main caller function for PUT calls
    response = requests.put(url, headers=header, json=body, params=param)
    if response.ok:
        if response.content:
            response_logging(response, url, msg)
            file_logging.success += 1
            return response
        else:
            file_logging.success += 1
            return response
    else:
        print(response.content)
        file_logging.error_logging(response, url, msg)
        file_logging.fail += 1
        return response


def caller_opt(url, header, body, param, msg):  # Main caller function for PUT calls
    response = requests.options(url, headers=header, json=body, params=param)
    if response.ok:
        if response.content:
            response_logging(response, url, msg)
            file_logging.success += 1
            return response
        else:
            file_logging.success += 1
            return response
    else:
        file_logging.error_logging(response, url, msg)
        file_logging.fail += 1
        return response


def caller_delete(url, header, body, param, msg):  # Main caller function for POST calls
    response = requests.delete(url, headers=header, json=body, params=param)
    if response.ok:
        if response.content:
            response_logging(response, url, msg)
            file_logging.success += 1
            return response
        else:
            file_logging.success += 1
            return response
    else:
        file_logging.error_logging(response, url, msg)
        file_logging.fail += 1
        return response
