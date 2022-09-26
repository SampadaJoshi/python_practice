
user_list =[
    {
        'ID' : "GHRS-1001",
        'first_name' :'Sampada',
        'last_name':'Joshi'
    },
    {
        'ID' : "GHRS-1002",
        'first_name' :'rohini',
        'last_name':'role'
    },
    {
        'ID' : "GHRS-1003",
        'first_name' :'diksha',
        'last_name':'mohod'
    },
    {
        'ID' : "GHRP-1001",
        'first_name' :'priti',
        'last_name':'jadhav'
    },
    {
        'ID' : "GHRP-1002",
        'first_name' :'pranita',
        'last_name':'mokale'
    },

]

prof_list =[]
student_list =[]
for user in user_list:
    ID = user.get("ID").split("-")
    if "GHRP" in ID:
        prof_list.append(user)
    elif "GHRS" in ID:
         student_list.append(user)
print(prof_list)
print(student_list)




