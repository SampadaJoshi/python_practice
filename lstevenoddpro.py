#1.WAP to featch all even numbers from list?
'''lst=[10,11,13,14,9,8]

for i in lst:
   if i % 2 == 0:
      print(i)'''
'''lst=[5,3,6,8,9,12,7]
print([i for i in lst if i %2==0])'''

#2.WAP to featch all string value from list?
lst=[10,'a',True,'b',False]
lst1=[]
for i in lst:
    if type(i) is str:
        lst1.append(i)
     
print(lst1)
 #print([i for i in lst if type(i) is str])


#3. WAP to featch all 5 divisibles from list?
'''lst=[12,15,27,20,5]
lst1=[]
for i in lst:
   if i % 5 == 0:
       lst1.append(i)
       print(lst1)

print([i for i in lst if i % 5 ==0])'''

#4. WAP to count total number of in values in the list.
'''lst=[10,'a',True,'b',False]
lst1=[]
for i in lst:
    if type(i) is int:
        lst1.append(i)
        print(lst1)

print([i for i in lst if type(i) is int])'''

#5.WAP to count total number of characters in thr string ?
'''st='python language'
print(len(st))'''

#6.WAP to count total no of words in the string?
'''st='python narayana tech house hyd'
st=st.split()
lst=[]
for i in st:
  print(len(i))

print([len(i) for i in st ])'''



#7.WAP to featch all vowels from string?
'''st='python language'
lst=[]
for i in st:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        lst.append(i)
        print(lst)
print([i for i in st if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'])
'''


#8.WAP to count total number of vowels
'''st='python narayana'
no=0
for i in st:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
          no= no+1
          print(no)

print([i for i in st if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'])
'''

#9.WAP to count total no of characters in the string(excluding space)?
"""st = 'python is a simple language'
count = 0;
lst=[]
for i in range(0,len(st)):
    if st[i] != ' ':
        count = count + 1
        lst.append(count)
        print(lst)
 """




#10. Write a program to count total number of consonants in the string?


#11.Write a program to fetch all words which starts with vowel from given string?
'''st = 'Python is simple and easy language' #['is', 'and', 'easy'
st=st.split()

lst=[]
for i in st:
    if i[0] in 'aeiouAEIOU':
        lst.append(i)
print(lst)'''

#12. Write a program to fetch all words which ends with consonent in the given string?
'''st = 'Python is simple and easy language' #['Python', 'is','and', 'easy'
st=st.split()

lst=[]
for i in st:
    if i[0] not in 'aeiouAEIOU':
        lst.append(i)
print(lst)'''


#13. Write a program to fetch all words which 'a' two or more then two times?
'''st = 'Python is simple and easy language' #['language']
st=st.split()
lst=[]
for i in st:
    if i.count('a')>=2:
        lst.append(i)
    print(lst)'''

#14. Write a program to count number of characters of each word in the string?
'''st = 'Python is simple and easy language' #[6,2,6,3,4,8]

st=st.split()
lst=[]
for i in st:
    for i in st:
        lst.append(len(i))
        print(lst)'''

#15. Write a program to fetch the first and last character from each word in the string?
'''st = 'Python is simple and easy language' #['Pn', 'is', 'se', 'ad', 'ey', 'le']
st=st.split()
lst=[]
for i in st:
    lst.append(i[0]+i[-1])
    print(lst)'''

#16. Write a program to fetch all words which contains 'a' character in the string?
'''st = 'Python is simple and easy language' #['and', 'easy', 'language']
st=st.split()
lst=[]
for i in st:
    if i.count('a')>=1:
        lst.append(i)
        print(lst)'''
#17. Write a program to fetch all words which does not contain 'e' character in string?
'''st = 'Python is simple and easy language' #['Python', 'is', 'and']
st=st.split()
lst=[]
for i in st:
    if i.count('e')==0:
        lst.append(i)
        print(lst)'''

#18. Write a program to fetch all words which contains only 4 or less than 4 characters?
'''st = 'Python is simple and easy language' #['is', 'and', 'easy']
st='Python is simple and easy language'
st=st.split()
lst=[]
for i in st:
    if len(i)<=4:
        lst.append(i)
        print(lst)'''

#19.19. Write a program to fetch all words which contain odd number of characters in the string?
'''st = 'Python is simple and easy language' #['and']'''

#20. Write a program to fetch all words which starts and ends with vowel in the string?
'''st = 'Python is number one language' #['one']
st=st.split()
lst=[]
for i in st:
    if i[0] in 'aeiouAEIOU':
        if i[-1] in 'aeiouAEIOU':
            lst.append(i[0]+i[-1])
        print(lst)'''




#20.Write a program to fetch all palindrome words from list?
'''names = ['madam', 'python','dad','language','eye','malayalam'] 
j = -1
flag = 0
for i in names:
    if i != names[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("NO")
else:
    print("Yes")'''


#wA comprehension to featch all negative no from list?
'''lst=[3,-7,9,-4,7]
lst1=[]
for i in lst:
    if i<0:
        lst1.append(i)
        print(lst1)'''


































        
        






































    


    

