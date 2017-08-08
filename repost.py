import urllib.request,urllib.parse

lib = urllib.request
parser  = urllib.parse

values = {"username":"601807116@qq.com","password":"litao627"}
data = parser.urlencode(values)
url = 'https://passport.csdn.net/account/login?form=http://my.csdn.net/my/'

request = lib.Request(url,data)
response = lib.urlopen(request)

print(response.read())