import requests
from requests.structures import CaseInsensitiveDict

url = "http://extolloconfigviews.azurewebsites.net/instance/EU-76"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"


resp = requests.get(url, headers=headers)

print(resp.status_code)