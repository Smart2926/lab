from math import cos, tan, sqrt, log
sport = "squash"
print (sport)

is_student = True
is_teacher = False
print(is_student and is_teacher)
print(is_student or is_teacher)
print(not is_student)
print(not is_teacher)

is_hot = False
is_cold = True
print(is_hot or is_cold)

x=0.357 
y=2.031
rounded=round(x**cos(y)-(tan(x)**sqrt(y-x))-19.12*log(y**3),5)
abs_x=abs(rounded)
print (abs_x)