import requests

payload = {
  'content': "# The first thing I do in the morning is ping <@772940386364555295> , After im done brushing my teeth I ping  <@772940386364555295> , Before i eat breakfast i ping  <@772940386364555295> , After i eat breakfast i ping  <@772940386364555295> , Before i workout i ping  <@772940386364555295> , after im done i ping  <@772940386364555295> , before i eat dinner i ping  <@772940386364555295> , after i eat dinner i ping  <@772940386364555295> , before i go to bed i ping <@772940386364555295>. Pinging  <@772940386364555295>  is truly a way of life for me and i dont see it any other way. 🙏🏿"
}

header = {
  'authorization': 'OTYxODA4MzIyMzc2Mzc2Mzgx.G2nLJ0.JPyQ_6QOPfNZwoOex5Vnonq6wtD8wMUYeRjO8Q'
}

r = requests.post('https://discord.com/api/v9/channels/1112577923183034442/messages', data=payload, headers=header)
