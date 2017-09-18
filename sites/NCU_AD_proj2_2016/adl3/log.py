from pwn import *

log.info("No you see me")
log.info("Now you don't")


p = log.progress('')
p.status('Reticulating splines')
time.sleep(1)
p.status('1')
time.sleep(1)
p.status('2')
time.sleep(1)
p.status('3')
time.sleep(1)
p.success('Got a shell!')

p = log.progress('')
p.status('Reticulating splines')
time.sleep(1)
p.success('Got a shell!')

p = log.progress('')
p.status('Reticulating splines')
time.sleep(1)
p.success('Got a shell!')
