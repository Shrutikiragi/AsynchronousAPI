import pytest
import requests
import json

PORT = 5000
SUCCESS_STATUS_CODE = 200
NO_OF_PROCESS = 1
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

EXPECTED_JSON = {'language': {'name': 'java'}}


def test_get_all_data_request_fail():
    url = "http://192.168.0.132:5000/lang/"

    response = requests.get(url, headers=HEADERS)
    assert response.status_code != 200


def test_get_all_data_request_pass():
    url = "http://192.168.0.132:5000/lang/java"
    response = requests.get(url, headers=HEADERS)

    response.status_code == 200
    actual_json_data = json.loads(response.text)
    assert actual_json_data == EXPECTED_JSON


def test_post_all_data_request_fail():
    url = "http://192.168.0.132:5000/lang/java"
    response = requests.post(url, headers=HEADERS)
    assert response.status_code != 200


def test_post_request_create_new():
    url = "http://192.168.0.132:5000/lang"
    post_data = {"name": "cpp"}

    response = requests.post(url, data=json.dumps(post_data), headers=HEADERS)
    assert response.status_code == SUCCESS_STATUS_CODE
    actual_json_data = json.loads(response.text)
    expected_data = {"language": {"name": "cpp"}}
    if actual_json_data == expected_data:
        print("Found")
    else:
        print("Not Found")

def test_put_request_update():
    url = "http://192.168.0.132:5000/lang/c"
    put_data = {"name": "cpp"}
    response = requests.put(url, data=json.dumps(put_data), headers=HEADERS)
    assert response.status_code == SUCCESS_STATUS_CODE
    actual_data = json.loads(response.text)
    expected_data = {"language": {"name": "cpp"}}
    if actual_data == expected_data:
        print("Found")
    else:
        print("Not Found")

