import conse
def checkstati(stat1,stat2,card1,card2,card3,card01,card02,card03):
    b = [card01.num, card02.num, card03.num]
    a = [card1.num, card2.num, card3.num]

    max1 = conse.getMax(a)
    max2 = conse.getMax(b)
    mid1 = conse.getMid(a)
    mid2 = conse.getMid(b)
    min1=conse.getMin(a)
    min2=conse.getMin(b)
    print("max1 =" ,max1 , "max2=",max2)
    print("mid1 =" , mid1, "mid2=" , mid2)
    print("min1 =" , min1 , "min2=" , min2)
    if(stat1==10):
        if(card1>card01):
            return 1
        else: return 2
    elif(stat2==2):
        if(min1 > min2):
            return 1
        elif(max1>max2):
            return 1
        else:
            return 2

    else:
        if (max1 > max2):
            return 1
        elif (max1 == max2):
            print(mid1,mid2)
            if (mid1 > mid2):
                return 1
            else:
                return 2
        else:
            return 2
