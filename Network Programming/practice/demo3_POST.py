import http.client
import json

conn = http.client.HTTPSConnection("www.httpbin.org")
headers_list = {'content-type':'application/json'}
post_text = {'text':'Hello World !!'}

json_data = json.dumps(post_text)
conn.request("POST","/post",json_data, headers_list)

response = conn.getresponse()
print(response.read().decode())

conn.close()
