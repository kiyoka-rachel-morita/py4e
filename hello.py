# Assignment 3.2
hrs=input('Enter hours')
rte=input('Enter rate')
hours=float(hrs)
salary_ph=float(rte)
if hours<=40:
    pay=hours*salary_ph
else:
    regular=40*salary_ph
    overtime=(hours-40)*(salary_ph*1.5)
    pay=regular+overtime
print(pay)

# Assignment 3.3    
# score input
score_inp=input('Enter score from 0.0 to 1.0')
try:
    score=float(score_inp)
except:
    print('Error: Put number')
    exit()

# score error check
if score<0.0 or score>1.0:
    print('Error:Number must be between 0.0 to 1.0')
    exit()

# grading
if score>=0.9:
    grade='A'
elif score>=0.8:
    grade='B'
elif score>=0.7:
    grade='C'
elif score>=0.6:
    grade='D'
elif score<0.6:
    grade='F'
print(grade)


