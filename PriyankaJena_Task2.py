import random
c=0
ch=''
x=''
score=10
clublist=["EMOTICA","AVC","SOULS","VIBRANZ","PIXELS"]
a=random.choice(clublist)
word=[]
word.extend(a)
for i in range(len(a)):
  word[i]='*'
print(word)
b=clublist.index(a)
if (b==0):
    print("hint=performs theatricals\n")
elif(b==1):
    print("hint=where writings are turned into cinema\n")
elif(b==2):
    print("hint=speaks through music\n")
elif(b==3):
    print("hint=makes music alive\n")
else : print("hint=it freezes the memories for us \n")
print("How will you guess the letter?")
print("1.guess the entire word\n")
print("2.guess the letters one by one\n")
print("enter your choice:")
ch=int(input())
print("score=10\n")
if(ch==1):
    while(score>0):
        print("guess the word:")
        x=str(input())
        x=x.upper()
        if(x==a):
              print(" word is ",a)
              print("you won\n")
              score+=5
              print("score=",score)
              break
        else:
                score-=3
                print("score=",score)
                print("wrong guess")
    if(score<=0):
        print("you lose")
        print("correct word is",a)
elif(ch==2):
    while(score>0):
        print("guess a letter=")
        x=str(input())
        x=x.upper()
        if x in a:
           if x in word:
              print("letter is already present")
              score-=2
              print("score=",score)
           if x not in word:
             for i in range(len(a)):
              if (a[i]==x):
                word[i]=x
                c+=1
             print("correct guess\n")
             print("word=",word)
             score+=3
             print("score=",score)
            
        if x not in a:
               print("wrong guess")
               score-=2
               print("score=",score)
        if (c==len(a)):
          break    
    for i in range(len(a)):
        if a[i]==word[i]:
          print("you won")
          break
        if (score<=0):
          print("you lost")
          break
else:
    print("wrong choice")
    
        
                
                        
    
                      



