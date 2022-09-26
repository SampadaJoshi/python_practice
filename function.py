#1 WAF to find the highest number of two given number?
'''n1=eval(input('Enter First Number  :'))
n2=eval(input('Enter second Number  :'))

def MaxOfTwo(a,b):
    if a>b:
        print('The highest number is {} between {} and {}'.format(a,a,b))
    else:
         print('The highest number is {} between {} and {}'.format(b,a,b))
MaxOfTwo(n1,n2)  '''


#2 WAF to check the whether the given no is even or odd

'''n1=eval(input('Enter Any Number  :'))

def Find_Even_Odd(n1):
    if n1%2==0:
        print('the given no is even')
    else:
        print('the given no is odd')
Find_Even_Odd(n1)'''


#3WAF to featch all 3 divisibles from the given list?
'''lst=[8,9,14,15,18,20,16]

def Divby3(lst):
    lst1=[]
    for i in lst:
        if i%3==0:
            lst1.append(i)
    print(lst1)
Divby3(lst)'''


#4 WAF to fetch all even numbers from list?
'''lst = [10,11,13,14,9,8]
def Even_no(lst):
    lst1=[]
    for i in lst:
        if i%2==0:
            lst1.append(i)
    print(lst1)
Even_no(lst)'''

#5 Write a function to fetch all string values from list?
'''lst = [10,'a',True,'b',False]    #['a', 'b']
def Value(lst):
    lst1=[]
    for i in lst:
        if type(i) is str:
            lst1.append(i)
    print(lst1)
Value(lst)'''

#3. Write a Function to fetch all 5 divisibles from list?
'''lst = [12,15,27,20,5]    #[15,20,5]
def Divby5(lst):
    lst1=[]
    for i in lst:
        if i%5==0:
            lst1.append(i)
    print(lst1)
Divby5(lst)'''


#4. Write a program to count total number of int values in the list
'''lst = [10,'a',20,True,30,'b',40]  #4
def number(lst):
    lst1=[]
    for i in lst:
        if type(i) is int:
            lst1.append(i)
    print(lst1)
number(lst)'''



#5. Write a program to count total number of characters in the string(including space)?.
'''st = 'Python language' #15
def Count_Char(st):
    print(len(st))
Count_Char(st)'''



#6. Write a program to count total number of words in the string.
'''st = 'python narayana tech house hyd' #5
st=st.split()
def Count_No(st):
    
    for i in st:
        print(len(i))
    
Count_No(st)'''


#7. Write a program to fetch all vowels from the string?
'''st = 'Python language' #['o','a','u','a','e']
def FindVowel(st):
    lst=[]
    for i in st:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            lst.append(i)
    print(lst)
    
FindVowel(st)'''

































        
        
        
    
        
    
    

    

    






















            
        
    
                  
