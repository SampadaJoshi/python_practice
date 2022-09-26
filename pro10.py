#10 WAP to featch all words which starts and end with vowel in string?
st='python is number one languge'
st=st.split()
lst=[]
for i in st:
    if i[0] in 'aeiouAEIOU':
        lst.append(i[0]+i[-1])
        print(lst)
