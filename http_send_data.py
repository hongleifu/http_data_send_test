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
    file_content = file_content.replace('$','')
    file_content = file_content.replace('\n','')
    file_content = file_content.decode('utf8')
    
    print "read file content succ!" 
    content=json.loads(file_content)
    print "convert to json string succ!" 
    print content

    #make url
    ip=content['ip']
    port=content['port']
    path=content['path']
    url=ip+":"+port+path+"?"
    data=content['data'] 

    url=url+urllib.urlencode(data)
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
