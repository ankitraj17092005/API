u={
    'name':'RR',
    'branch':3,
    'gender':'Female',
    'id':'2',
    'summary':'hii this is you',
    'roll':39
}
resp=requests.put(url,json=f_u)
print(resp.text)