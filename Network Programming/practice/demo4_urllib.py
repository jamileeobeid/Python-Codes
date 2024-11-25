import urllib.request
import urllib.parse

url = 'https://www.google.com/search'

values = {'query' : 'python tutorial'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes

req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)
