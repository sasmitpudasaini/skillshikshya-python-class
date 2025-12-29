#assignment3

# 1. Task 1
student_scores = {'sasmit':[50,45,88]}
marks = (student_scores["sasmit"])
average = sum(marks)/ len(marks)
print(average)
if average>=60:
    print(True)
else:
    print(False)

# 2.Task 2
stock = {"apples": 10, "bananas": 2, "oranges": 0}
if "pears" in stock:
    print(True)
else:
    print(False)
    
if "bananas" in stock and stock["bananas"]<5:
    print("Time to restock bananas!")
    
# 3.Task 3
users = {"admin": "1234"}
users["teacher"] = "password789"
input_user = ('teacher')
input_pass = ('password789')
if input_user == users and input_pass in users["teacher"]:
    print("access granted")

