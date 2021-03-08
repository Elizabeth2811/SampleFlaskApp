import requests

url = "https://api-edc-dev.app.corpintra.net/extollo/v0"

payload="{\"instance_id\":\"EU-00\"}"
headers = {
  'x-api-key': 'a421fa4c-f92a-4233-b48a-9d4608ef7533',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)