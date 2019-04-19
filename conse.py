def conse(n1,n2,n3):
    a=[n1,n2,n3]
    max=getMax(a)
    min=getMin(a)
    mid=getMid(a)
    if(max-mid == 1 and mid-min == 1):
        return True
    else:
        return False
11
def getMax(a):
    max=a[0];
    if(a[0]>a[1] and a[0]>a[2]):
        return a[0]
    elif(a[1]>a[0] and a[1]>a[2]):
        return a[1]
    else:
        return a[2]

def getMin(a):
    if (a[0] < a[1] and a[0] < a[2]):
        return a[0]
    elif (a[1] < a[0] and a[1] < a[2]):
        return a[1]
    else:
        return a[2]

def getMid(a):
    if ((a[0] < a[1] and a[1] < a[2]) or (a[2] < a[1] and a[1] < a[0])):
        return a[1];

        # Checking for a[0]
    if ((a[1] < a[0] and a[0] < a[2]) or (a[2] < a[0] and a[0] < a[1])):
        return a[0]

    else:
        return a[2]