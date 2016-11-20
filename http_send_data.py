#!/usr/bin/python
#coding=utf8
import json
import urllib 
import urllib2 

def send():
    #read json string from file
    fp=open('./data','r')
    file_content=fp.read()
    fp.close()
#    file_content = file_content.replace('$','')
#    file_content = file_content.replace('\n','')
#    file_content = file_content.replace(' ','')
#    file_content = file_content.decode('utf8')
    
    print "read file content succ!" 
#    print file_content,type(file_content)
    content=eval(file_content)
#    for k,v in content['data']['user_info'].items():
#      print "----",v
    #print content,type(content)
#    content=exec(file_content)
#    content=json.loads(file_content)
    print type(content)
    print "convert to json string succ!" 

    #make url
    ip=content['ip']
    port=content['port']
    path=content['path']
    url="http://"+ip+":"+port+path+"?"
    data={}
    data['data']=content['data']
    param=urllib.urlencode(data)
    url=url+param
    try:
        print "send url:-------------\n",url
        req=urllib2.Request(url)
        res_data=urllib2.urlopen(req)
        res=res_data.read()
        res=res.decode('utf8')
        print " return result----------------------------------:",res
    except Exception,e:
        print "send error:",e

if __name__=="__main__":
    send()
