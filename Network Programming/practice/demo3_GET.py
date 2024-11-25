import http.client

conn = http.client.HTTPSConnection("www.httpbin.org")
conn.request("GET","/")

response = conn.getresponse()

print(response.status, response.reason)
print(response.getheaders())

conn.close()
