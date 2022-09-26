#9 WAP to featch all words which contain odd no characters in the string?
st='python is simple and easy language'
st=st.split()
lst=[]
for i in st:
    if len(i)%2!=0:
        lst.append(i)
        print(lst)
