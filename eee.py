import requests

params = {

}
url = 'http://www.zyctd.com/'

r = requests.get(url)
print(r.status_code())
