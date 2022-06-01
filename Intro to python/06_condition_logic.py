# print(4==4)
# print(4!=4)
# print(4<4)
# print(4<=4)


#application of logical operators
age_at_school= 5
s_age= input("please enter student age = ")
print("input type before conversion ")
print( type(s_age))  #input is string 
print("input type aftere conversion ")
s_age= int(s_age)   # convert input into integer
print(type(s_age))
print(age_at_school==s_age)