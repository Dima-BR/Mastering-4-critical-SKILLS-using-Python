#  Students grades
# Write a program that reads 2 students information about math exam
# ○ For each student read: his name, id and grade
# ● Print the students
# ● Print the grades average


st1_name= input("please enter Student 1 name: ")
st1_id= input("please enter Student 1 ID ")
st1_grade= float(input("please enter Student 1 Grade "))

st2_name= input("please enter Student 2 name:")
st2_id= input("please enter Student 2 ID ")
st2_grade= float(input("please enter Student 2 Grade "))

avg = (st1_grade + st2_grade) / 2


print(f"student grades \n {st1_name} ({st1_id}) got Grade {st1_grade},\n {st2_name} ({st2_id}) got Grade {st2_grade}\n Average Math grades is: {avg}")
