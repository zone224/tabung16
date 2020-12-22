### Get All members 

import os 
import requests 
import random 
from time import sleep as t


Base_url = "https://id-api.spooncast.net/users/"
Api = "/follow/"

os.system('cls')
Number = input("Input Number : ")
Password = input("Input Password : ")
P = {'cv':'heimdallr'} 
H1={'User-Agent':'Spoon/4.4.6(229) Dalvik/2.1.0 (Linux; U; Android 6.0.1; SO-01G Build/23.5.B.0.368)'}
Auth = {"sns_type":"phone", "sns_id":Number, "password":Password}
xxx = requests.post('https://id-api.spooncast.net/signin/', headers=H1, params=P, json=Auth)
xxxxxx = xxx.json()
for xxxx in xxxxxx['results']:
	Toket = xxxx['token']
	my_id = xxxx['id']

params={'cv':'heimdallr'}
ua = open('ua.txt','r').read().splitlines()
os.system('cls')
H = {'Authorization':'Token '+Toket,
'accept':'text/htmlapplication/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
"origin":"https://www.spooncast.net",
"referer":"https://www.spooncast.net/",
'content-type':'application/json',
'User-Agent':'Spoon/4.4.6(229) Dalvik/2.1.0 (Linux; U; Android 6.0.1; SO-01G Build/23.5.B.0.368) Chrome/77.0.3865.92 Safari/537.36'}
with requests.Session() as Range:
	i=0
	x = Range.get('https://id-api.spooncast.net/users/'+str(my_id)+'/followings/', headers=H).json()
	next_user = x['next']
	for result in x['results']:
		uid = result['id']
		H = {'Authorization': 'Token ' +Toket,
		'accept':'text/htmlapplication/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		"connection":"keep-alive",
		"origin":"https://www.spooncast.net",
		"referer":"https://www.spooncast.net/",
		'content-type':'application/json',
		'User-Agent':str(ua[i])}
		xx = requests.post('https://id-api.spooncast.net/users/'+str(uid)+'/unfollow/', headers=H).status_code
		print(i+1,'User ID : ['+str(uid)+']'+' /Status Code :', xx)
		i+=1
	while next_user != "":
		xxx = requests.get(next_user, headers=H).json()
		next_user = xxx["next"]
		for result_two in xxx["results"]:
			uid = result_two["id"]
			xx = requests.post('https://id-api.spooncast.net/users/'+str(uid)+'/unfollow/', headers=H).status_code
			print(i+1,'User ID : ['+str(uid)+']'+' /Status Code :', xx)
			i+=1
			if xx == 403:
				print('Break for 3 Minutes. . . .')
				t(180)
### The end of Session.