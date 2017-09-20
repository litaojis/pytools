#__author : ajoker

import requests
import time


loginurl = 'http://softpm.grgbanking.com:8080/nStraf/login!checkuser.action'

login_params = {'userid':'ltao13','userpwd':'litao627'}

r = requests.post(loginurl, data=login_params)

#print(r.text)

print(r.cookies['JSESSIONID'])
print(tuple(r.cookies))

print('===============填写日志=============================')
'''
general:
Request URL:http://softpm.grgbanking.com:8080/nStraf/pages/daylog/logInfo!save.action
Request Method:POST
Status Code:200 OK
Remote Address:221.5.109.2:8080

header:
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:542
Content-Type:application/x-www-form-urlencoded
Cookie:JSESSIONID=D3CE46B97E567B805C030679434BA3F1
Host:softpm.grgbanking.com:8080
Origin:http://softpm.grgbanking.com:8080
Referer:http://softpm.grgbanking.com:8080/nStraf/pages/daylog/logInfo!add.action
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36

form-data:
submitCreateDate:2017-07-26
daylogList[0].prjName:5c7386b3566a2fc701567cddbbcc2fe7
daylogList[0].type:日常工作
daylogList[0].statu:按时
daylogList[0].finishRate:100%
daylogList[0].planOrAdd:计划
daylogList[0].subTotal:8
daylogList[0].tasktype:0
daylogList[0].tasksdate:
daylogList[0].taskedate:
daylogList[0].desc:其他任务
daylogList[0].reason:项目开发
daylogList[0].delay_reason:

88666F3AD0B1DE6CC8F0CDCD0B5A5632
'''
save_url = 'http://softpm.grgbanking.com:8080/nStraf/pages/daylog/logInfo!save.action'

daylogList = [{'prjName':'5c7386b3566a2fc701567cddbbcc2fe7','type':'日常工作','statu':'按时',
'finishRate':'100%','planOrAdd':'计划','subTotal':8,'tasktype':0,'desc':'其他任务',
'reason':'雅士利会员系统开发,价盘模块开发','delay_reason':''}]
submitCreateDate = time.strftime("%Y-%m-%d", time.localtime()) 
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
save_p = {'submitCreateDate' : submitCreateDate,
		'daylogList[0].prjName':daylogList[0]['prjName'],
		'daylogList[0].type':daylogList[0]['type'] ,
		'daylogList[0].statu':daylogList[0]['statu'],
		'daylogList[0].finishRate':daylogList[0]['finishRate'],
		'daylogList[0].planOrAdd':daylogList[0]['planOrAdd'],
		'daylogList[0].subTotal':daylogList[0]['subTotal'],
		'daylogList[0].tasktype':daylogList[0]['tasktype'],
		'daylogList[0].desc':daylogList[0]['desc'],
		'daylogList[0].reason':daylogList[0]['reason']} 

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, de-flate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'JSESSIONID='+r.cookies['JSESSIONID'],
'Host':'softpm.grgbanking.com:8080',
'Origin':'http://softpm.grgbanking.com:8080',
'Referer':'http://softpm.grgbanking.com:8080/nStraf/pages/daylog/logInfo!add.action',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

resp = requests.post(save_url, data=save_p, headers=headers)

print(resp.text)
print('日志内容：',daylogList[0]['reason'])



class Loginer(object):
    def __init__(self):
		self.username = None
		self.pwd = None
	def getUserNamePwd(self):
		try:
			f = open('config.ini','r')
			for line in f.readlines():
    			k_v = line.split('=')
				if k_v[0] == 'login.username':
					self.username = k_v[1]
				if k_v[0] == 'login.pwd':
    				self.pwd = k_v[1]
		finally:
			if f:
    			f.close()
	def login(self):
			