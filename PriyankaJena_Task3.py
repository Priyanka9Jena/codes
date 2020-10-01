# task 3.1
def red_zone():
    print("TASK 3.1")
    los=[]
    s=[]
    area=0
    print("no. of sticks :")
    n=int(input())#input no. of sticks
    for i in range(n):
        print("enter the length:")
        l=int(input())#input the lengths
        los.append(l)
    print("length of sticks:")
    print(los)
    for i in range(n):
        for j in range(i+1,n):
            if(los[i]==los[j]):
                if(los[i] not in s):
                    s.append(los[i])
    s.sort(reverse=True)#to sort the elements in descending order
    if(len(s)>=2):
        l=s[0]
        b=s[1]
        area+=(l*b)
        print("maximum red zone area:",area)#print the maximum rectangle area 
    else:
        print("-1")
    print("")
    print("")
# task 3.2
def alternating_subarray():
    print("TASK 3.2")
    arr=[]
    x=[]
    print("size of array:")
    n=int(input())#input size of array
    for i in range(n):
        print("enter element:")
        e=int(input())#enter elements
        arr.append(e)# enter elements into an empty list
    print("elements:")
    print(arr)
    for i in range(n):
        u=arr[i]/abs(arr[i])#abs function used to get the absolute value of a number
        c=1
        for j in range(i+1,n):
            t=arr[j]/abs(arr[j])
            if(u==(t)):
                break
            else:
                c=c+1
                u=(-u)
        x.append(c)
    print("output:")
    print(x)#print the output
    print("")
    print("")
    
# task 3.3       
def win_matches():
    print("TASK 3.3")
    print("value of X(points needed to qualify):")
    x=int(input())#input points required
    print("value of Y(number of remaining matches):")
    y=int(input())#input no. of remaining matches
    n=int(x/2)
    if(n<=y):
      print("number of matches required to win:",n)#print the output
    else:
      print("number of matches required to win:",y)
    print("")
    print("")
    
# task 3.4      
def movie_selection():
    print("TASK 3.4")
    L=[]
    R=[]
    LR=[]
    x=""
    y=[]
    print("enter no. of movies:")
    n=int(input())# input of no. of elements
    for i in range(1,(n+1)):
        print("L",i,":")
        l=int(input()) #input of values of L
        print("R",i,":")
        r=int(input()) # input of values of R
        x=(l*r,r,n+1-i)
        y.append(x) #enter into another list
    m=max(y)
    j=y.index(m)
    print("movie",j+1) #print of the output movie
    print("")
    print("")
    
# task 3.5
def min_totalcost():
    print("TASK 3.5")
    totalcost=0
    arr=[]
    t=""
    print("size of array:")
    n=int(input())#input size of array
    for i in range(n):   
       print("enter element:")
       c=int(input())#input elements
       arr.append(c)
       i+=1
    print("elements:")
    print(arr)
    for i in range(n-1,0,-1):#loop for count of string
        for j in range(i):
            if(arr[j]<arr[j+1]):
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
    for i in range((n-1),0,-1):
        cost=int(arr[i])
        arr.remove(arr[i-1])# to remove an element from list
        totalcost=totalcost+cost
    print("minimum total cost:",totalcost)#print minimum total cost
    
# function calls
red_zone()
alternating_subarray()
win_matches()
movie_selection()
min_totalcost()

