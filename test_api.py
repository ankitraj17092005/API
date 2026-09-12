import requests
url='http://127.0.0.1:8000/api/student/'
id={'id':1}
cont=requests.get(url,params=id)
print(cont.json())