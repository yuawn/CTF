# sage ./flag.sage

'''
loop:
    lea     rdx, [rdx+rdx*2]
    lea     rdx, [rdx+rcx*2+4]
    xchg    rcx, rdx
    jmp     loop


x' = y
y' = 3x + 2y + 4

[ x , y , 1 ]

[ 0 , 3 , 0 ]
[ 1 , 2 , 0 ]
[ 0 , 4 , 1 ]
'''


K = Zmod(2^64)

A = Matrix(K, [
    [ 0x82F96AC97429A68B, 0x32B9B6BCA55548ED, 1]
])

N = Matrix(K, [
    [ 0, 3, 0],
    [ 1, 2, 0],
    [ 0, 4, 1],
])

assert N^(2^64) == identity_matrix(3)

dp = [0] * 1338
dp[0] = 1
dp[1] = 3
dp[2] = 5
dp[3] = 15

K = Zmod(2^66)
dp = [K(e) for e in dp]

for i in range( 1338 ):
    if dp[i]:
        continue

    dp[i] = dp[i-1] + dp[i-2] ** 2 + dp[i-3] ** 3
    #print(i, dp[i])


n = dp[1337]
e = ZZ(n) // 4

print( 'n =' , n )
print( 'n / 4 =' , e )
print( 'n % 4 =' , n % 4 )

ans = A*N^e
print( 'A * N^e =' , ans)

rdx = ans[0,0]
rcx = ans[0,1]

rdx = rdx + rdx * 2


print( hex(rcx) , hex(rdx) )
print( 'p4{%016x%016x}' % ( rcx , rdx )  )