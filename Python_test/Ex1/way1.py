import requests

url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
myobj = {'log': 'admin', 'pwd': '123456aA'}


x = requests.post(url, data = myobj)
str = x.request.headers.get('Cookie')
result = str.split("%")[0].split("=")[1]

print(result)