def utility(a, b, opr):
    #code here
    if opr==1:
        c=str(a+b)
        print(c,end="")
    elif opr==2:
        c=str(a-b)
        print(c,end="")
    elif opr==3:
        c=str(a*b)
        print(c,end="")
    else:
        print("Invalid Input",end="")