string =input("enter the word =")
acnt=0
ecnt=0
icnt=0
ocnt=0
ucnt=0
X=0
for i in  range(len(string)):
    if string[i]=='a' or string[i]=='A':
      
       acnt+=1
    elif string[i]=='e' or string[i]=='E':
      
       ecnt+=1 

    elif string[i]=='i' or string[i]=='I':
      
       icnt+=1 

    elif string[i]=='o' or string[i]=='O':
       
       ocnt+=1 

    elif string[i]=='u' or string[i]=='U':
       
       ucnt+=1 

    else:
         X+=1

print("a=%d e=%d i=%d o=%d u=%d"%(acnt,ecnt,icnt,ocnt,ucnt))
print("no of constents=%d "%X)
