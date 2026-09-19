'''
you can test full api web app through this console python app 
this is third party app not directly connected with that web application this is connected through api
if you deploy fullapi on any server then serverlink/api/student is their api link for connection with third party application
'''
import requests

main_url='http://127.0.0.1:8000/api/student/'

'''
    C - U - R - D ----OPERATION----
'''

#for getting all data from the databases from server
data=requests.get(main_url)
print(data.json())

#getting a single data
# std_id=6
# data=requests.get(f'{main_url}{std_id}')
# print(data.json())


# create a data on database
# one_data={
#     'name':'Abhay Raj',
#     'email':'abhay@gmail.com',
#     'mobile':'1234567890',
#     'street_adrs':'Bihar,nalanda',
#     'state':2,
#     'city':1,
#     'pincode':'803100'
# }
# res=requests.post(main_url,json=one_data)
# print(res.json())


#partial update 
# one_data={
#     'id':7,
#     'name':'Sonu Raj',
#     'email':'sonu@gmail.com',
#     'mobile':'9087654321',
#     'street_adrs':'Bihar,nalanda',
#     'state':2,
#     'city':1,
#     'pincode':'803100'
# }
# res=requests.patch(main_url,json=one_data)
# print(res.json())


#full update
# one_data={
#     'id':6,
#     'name':'Saurav Raj',
#     'email':'saurav@gmail.com',
#     'mobile':'7050144795',
#     'street_adrs':'Aungari,nalanda',
#     'state':1,
#     'city':2,
#     'pincode':'801301'
# }
# res=requests.patch(main_url,json=one_data)
# print(res.json())


#delete the data from databases
# id=5
# res=requests.delete(f'{main_url}{id}/')
# print(res.json())