
import requests

URL = 'http://0.0.0.0:2224/fast'

for a in range(51):
    resp = requests.get(URL).text
    print(f"{a}\t {resp}")


