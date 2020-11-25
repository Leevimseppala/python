import statistics
students = int(input("Anna opiskelijoiden lukumäärä:\n"))
grades = []
counter = 0
for x in range(students):
    grade = int(input("Anna oppilaan arvosana:\n"))
    grades.append(grade)
ka = sum(grades) / students
print(f"Keskiarvo: {ka}")
print(f"Arvosanojen mediaani oli {statistics.median(grades)}")
num = grades[0]
for i in grades:
    current = grades.count(i)
    if current > counter:
        counter = current
        num = i
print(f"Yleisin arvosana oli {grades[i]}")
if 0 <= ka < 1:
    print("Huono tulos")
elif 1 <= ka < 2:
    print("Heikko tulos")
elif 2 <= ka < 3:
    print("Tyydyttävä tulos")
elif 3 <= ka < 4:
    print("Hyvä tulos")
elif 4 <= ka <= 5:
    print("Kiitettävä tulos")
