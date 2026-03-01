import re
def numberMatcher(str):
    match=re.findall(r'\d+',str) ##find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")