#ANSWER TO QUESTIOON  2ND
import requests
count=0
for i in range(1,13):
   re=requests.get('https://reqres.in/api/users?page={}'.format(i))
   dct=re.json()
   length_of_users=len(dct['data'])
   count=count+length_of_users

print("No of users are:",count)
