from requests import Request, Session

USER_KEY = "i0Jb-rd861ZbQgI40P3feSkUpwwx8jHYcQ42T-Lha8jpdkblPm"
DEVICE_CODE = "81206517"
s = Session()
url = "http://api.lockera.net"
headers = {'Content-Length': '1024', 'Content-Type': 'application/json'}
data = {
    "sender": "client",
    "private_key": USER_KEY,
    "device_code": DEVICE_CODE,
    "action": "getData",
    "param": {
        "fields": ["last_check", "device_status", "device_address"]

    }
}
# prepare request data.
req = Request('POST', url, json=data, headers=headers)
prepped = req.prepare()
print(prepped.headers)
# send the request to server
response = s.send(prepped)

# see the status code and the json response
print(response.status_code)
print(response.json())
