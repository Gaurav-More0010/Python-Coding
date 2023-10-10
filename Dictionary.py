# #Duplicates are not allowed
# phone_no={
#     'Ram':1234,
#     'Shyam':5678,
#     'Mohan':910
# }
phone_no=dict([('Ram',1234),('Shyam',5678),('Mohan',910)])
print(phone_no['Shyam'])
phone_no['Mohan']=9999
print(phone_no)
phone_no['Madhav']={111,222,333}
print(phone_no)
 


