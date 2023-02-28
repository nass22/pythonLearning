#https://codeavecjonathan.com/res/papillon.jpg

import requests

response = requests.get('https://codeavecjonathan.com/res/papillon.jpg')

if response.status_code == 200:
    f = open('papillon.jpg', 'wb') #wb = write binary
    f.write(response.content)
    f.close()
else:
    print('Error', response.status_code)
    
