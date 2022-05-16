from pip._vendor import requests

r = requests.get("https://api.github.com/user")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {'p1': 4, 'p2': 8}
# r2 = requests.post(url=url, data=data)
