"""
pip3 install websocket-client
"""
from websocket import create_connection
import json
from hashlib import sha256
ws = create_connection('ws://127.0.0.1:60555')
auth_request = {
    'id': 1,
    'type': 'authenticate',  # 'version','api','authenticate','link'
    'payload': {
        "origin": "https://iamredbar.com",
        "app_name": "BTS_Stuff",
        "browser": "Brave"
    }
}
print(auth_request)
ws.send(json.dumps(auth_request))
auth_recv = ws.recv()
print(json.loads(auth_recv))
tmp = json.loads(auth_recv)
auth_pub_key = tmp['payload']['pub_key']
print(auth_pub_key)
nxt = sha256(str(3).encode())
link_request = {
    'id': 2,
    'type': 'link',  # 'version','api','authenticate','link'
    'payload': {
        'chain': 'BTS',
        'pub_key': auth_pub_key,
        'next_hash': nxt.hexdigest()
    }
}
print(link_request)
ws.send(json.dumps(link_request))
tmp1 = ws.recv()
print(json.loads(tmp1))
