a = list(map(int,input("Enter the array elements: ").split()))
def div_three(a):
    count=0
    for i in a:
        if i == 0:
            continue
        elif i %3==0:
            count+=1
    return count
print(div_three(a))