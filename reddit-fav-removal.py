import requests
import sys

if len(sys.argv) == 1:
    print("Usage: reddit-unsave <username> <password>")
    sys.exit()

username = str(sys.argv[1])
password = str(sys.argv[2])

url = 'https://www.reddit.com/api/login/' + username
url2 = 'https://www.reddit.com/user/' + username + '/saved/.json'
url3 = 'https://www.reddit.com/api/unsave'

payload = {'op': 'login', 'user': username, 'passwd': password}

session = requests.Session()
r = session.post(url, data = payload, headers = {'User-agent': 'Mozilla/5.0'})
r = session.get(url2, headers = {'User-agent': 'Mozilla/5.0'})

data = r.json()

while len(data['data']['children']) > 0:
    r = session.get(url2, headers = {'User-agent': 'Mozilla/5.0'})

    data = r.json()
    mainData = data['data']['children']
    modhash = data['data']['modhash']

    nameList = []
    for i in mainData:
        nameList.append(i['data']['name'])

    while len(nameList) > 0:
        nameRemove = nameList.pop()
        payload = {'id': nameRemove, 'uh': modhash}
        r = session.post(url3, payload, headers = {'User-agent': 'Mozilla/5.0'})
        print(r)

