# A1=2 A2=3 이면 3번째 항은 
# A3 = A2 + 2*A1 = 3 + 2*2 => A3 = 7 
# A4 = A3 + 2*A2 = 7 + 2*3 => A4 => 13
# A5 = A4 + 2*A3 = 13 + 2*7 => 27
# A6 = A5 + 2*A4 = 27 + 2*13

# => An-1
 
a1, a2 = map(int, input().split())
x = 0
y = 0
z = 0

for i in range (1,11):
    if i == 1:
        print(a1, end=" ")
        x = a1
    elif i == 2:
        print(a2, end=" ")
        y = a2
    else: 
        z = y + 2*x
        print(z, end=" ")
        x = y
        y = z