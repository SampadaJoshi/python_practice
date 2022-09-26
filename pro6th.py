#WAP to fetch all words which contains 'a' character in the string?

st='Python is simple and easy language'
st=st.split()
lst=[]
for i in st:
    if i.count('a')>=2:
        lst.append(i)
        print(lst)
    
