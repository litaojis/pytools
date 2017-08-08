import urllib.request


response = urllib.request.urlopen("http://www.baidu.com");

#print (response.read())

req = urllib.request

request = req.Request('http://softpm.grgbanking.com:8080/nStraf/index.jsp')

response  = req.urlopen(request)
print(response.read())

