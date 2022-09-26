ans=input('Did you write assignment2 last week?(yes/no):').lower()
if ans=='yes:
  marks=eval(input('how many marks you got?:'))
  if marks>=0 and marks<35:
      print('you need to practice more')
    elif marks>=35 and marks<=5:
        print('ok good')
     else:
         print('please check your marks')
   elif ans== 'no':
       print('you must write assignment')
else:
    print('please say yes or no only')
 
