import requests, json


re = requests.get('https://viacep.com.br/ws/082770630/json/')
print(re.json())

headers = {"content-type":"application/json"}
data = {"nome":"joao"}

re = requests.post("http://127.0.0.1:5000/", data=json.dumps(data), headers=headers)

print(re.json())