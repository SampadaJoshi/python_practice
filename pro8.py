#8.WAP to featch all words which contains only 4 or lessthan 4 characters?
st='Python is simple and easy language'
st=st.split()
lst=[]
for i in st:
    if len(i)<=4:
        lst.append(i)
        print(lst)
        
