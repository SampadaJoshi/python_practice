'''-----------------1----------------'''
#wA comprehension to featch all negative no from list?
'''lst=[3,-7,9,-4,7]
lst1=[]
for i in lst:
    if i<0:
        lst1.append(i)
        print(lst1)'''

'''lst=[3,-7,9,-4,7]
print([i for i in lst if i<0])'''


'''-----------------2----------------'''
#WAC to all float values from list?
#lst=[10,10.5,True,'a',20.5]
'''lst1=[]
for i in lst:
    if type(i)is float:
        lst1.append(i)
        print(lst1)'''


'''print([i for i in lst if type(i) is float])'''

'''-----------------3----------------'''
#WAC to featch all 10 dividibles from list?
lst=[10,32,40,50,'a','b',45]
#print([i for i in lst if i%10==0])
'''lst1=[]
for i in lst:
    if type(i) is int:
        lst1.append(i)
lst2=[]
for i in lst1:
    if i%10==0:
        lst2.append(i)
        print(lst2)'''

#print([i for i in[i for i  in lst if type(i) is int]if i%10==0])



'''-----------------4----------------------------------------------'''
#WAC TO featch all vowel from list?
'''lst=[10,'a','x',True,'i','m',20]
lst1=[]
for i in lst1:
    if str(i)=='aeiouAEIOU':
         lst1.append(i)
    print(lst1)'''
# print([i for i in lst if str(i) in 'aeiouAEIOU'])


'''--------------------------------------------5--------------------------------'''
# WAC to featch all words which contain 'a' character?
lst=['nth','python','django','ui','flask','java']
lst1=[]
for i in lst:
     if i.count('a')!=0:
         lst1.append(i)
         print(lst1)

print([i for i in lst if i.count('a')!=0])

print([i for i in lst if 'a' in i])
     





























        
     
