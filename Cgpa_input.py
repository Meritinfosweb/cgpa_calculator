#A simple CGPA calculator based on the 4.0 and 5.0 Grade System. 
#Use as you wish and improve. Totally debugged 
# but if any bug is found, please report to me or fix
#Author: Michael Erastus
#copyright: None 
#
#
#
#function that checks for the grading system choosen,
#  and assign grade points to each
def grade_type(gradetype,grade):
    if gradetype==4:#for grade system 4.0
        if grade=="F":
            point=0
        elif grade=="D":
            point=1
        elif grade=="C":
            point=2
        elif grade=="B":
            point=3
        else:
            point=4
        return point
    elif gradetype==5:#if the grade system is 5.0
        if grade=="F":
            point=0
        elif grade=="D":
            point=2
        elif grade=="C":
            point=3
        elif grade=="B":
            point=4
        else:
            point=5
        return point
#Requesting for data from user
print("Enter Number of Subject Offered")
num_sub=int(input())
print("Enter Grade System e.g 4,5. Only these are currently supported")
grade_system=int(input())
x=0#initialization of x; used to check against increment
point_sum=0
total_unit_load=0
while x<num_sub:
    print("Enter Subject")
    subject=input()
    print("Enter Grade")
    grade_taken=input()
    grade_alpha=grade_taken.isalpha()
    if grade_alpha==True:
        print("Enter Unit Load")
        unit_load=int(input())
        points=grade_type(grade_system,grade_taken.upper())
    else:
        print("Grade must be only an alphabet")
    point=unit_load*points
    total_unit_load+=unit_load
    point_sum+=point
    x+=1
print("Total Unit load is: ",total_unit_load)
print("Total point is:",point_sum)
print("Your CGPA is:",point_sum/total_unit_load)