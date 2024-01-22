n = int(input())
m = 0

# (0.0) (0.1) (0.2) (0.3)
#(1)
for i in range(1,n+1):
    for j in range(1,n+1):
        if i % 2 !=0:
            m += 1 
            print (m, end=" ")  
        if i % 2 == 0:
            m += 2
            print (m, end=" ")
    print( )