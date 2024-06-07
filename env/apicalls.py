# Make API requests

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

numero = 0
try:
    while True:     
        titles = response.json()[numero]['id'] 
        body = response.json()[numero]['body']
        print(f"{numero+1}:  {titles}")
        numero = numero +1
except:
    print('Ya no hay mas titulos copon')