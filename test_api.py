import requests
url='http://127.0.0.1:8000/api/student/'
# id={'id':1}

# get all data
cont=requests.get(url)
print(cont.json())

#insert new data on database through API
# new_data={
#     'name':'kalia Kapoor',
#     'branch':3,
#     'roll':29,
#     'gender':'Male',
#     'summary':'hi this is raj kapoor'
# }
# r=requests.post(url,json=new_data)
# print(r.text)

#update partially data
# up_data={
#     'name':'pink',
#     'branch':2,
#     'gender':'Male',
#     'id':'3'
# }
# # res=requests.patch(url,json=up_data)
# # print(res.text)


#full update
# f_u={
#     'name':'RR',
#     'branch':3,
#     'gender':'Female',
#     'id':'2',
#     'summary':'hii this is you',
#     'roll':39
# }
# resp=requests.put(url,json=f_u)
# print(resp.text)


#delete
# del_id={'id':'1'}
# resp=requests.delete(url,json=del_id)
# print(resp.text)
