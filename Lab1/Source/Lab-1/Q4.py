#declaring 2 lists for two courses
webapp = ['nam', 'puj', 'srav', 'sudhee']
python = ['nam', 'puj', 'sak', 'srini', 'dev']

#calculating the length which gives the number of people
first = len(webapp)
sec = len(python)
x = 0
sameCourse = []
diffCourse = []

#search for each student in each list and compare
for i in range(first):
    if webapp[x] in python:
        sameCourse.append(webapp[x])
    else:
        diffCourse.append(webapp[x])
    x = x + 1
y = 0
for j in range(sec):
    if python[y] not in webapp:
        diffCourse.append(python[y])
    y = y + 1
print(sameCourse)
print(diffCourse)

