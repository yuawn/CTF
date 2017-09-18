import ctypes , random

a = 0x32463e        #3294782
b = 0xbc4e28a3      #3159238819
final = 0xde11c105  #3725705477


#s = raw_input()

while True:
    state = 42
    s = []

    for i in range(32):
        s.append(random.randint(0 , 11))

    #print s

    def dish(x):
        global state , a , b
        #print state
        #print a
        #print b
        state = ctypes.c_uint32( ( ( state + x ) * a ) ^ b ).value


    for i in range(32):
        dish(s[i])
        #state = i
        #print ctypes.c_uint32( (i * a) ^ b ).value

    if ctypes.c_uint32(state).value == final:
        print 'YUAN!!!!!!!!!!!!!'
        break
    else:
        print 'fail'
    print ctypes.c_uint32(state).value








def dd(x):
    global d , a , b
    print d
    x = x
    d = ctypes.c_uint32( ( x ^ b ) / a ).value
