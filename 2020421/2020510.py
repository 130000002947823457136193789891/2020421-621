studentid = {}
studentscore = {}
course = set()
while True:
    line = input()
    if line == 'END':
        break
    words = line.split()  #以空格分割输入行
    if words[-1].isnumeric():
        #代码块
        #课程、成绩关系
        score = studentscore.get(words[0])
        if score == None:
            score = {}
        score[words[1]] = words[2]
        studentscore[words[0]] = score
        course.add(words[1])
    else:
        #代码块
        #学号、姓名关系
        studentid[words[0]] = words[1]
coursename = list(course)
print(',', end='')
for name in coursename:
    print(','+name, end='')
print()

for id in studentid.keys():
    print(id+','+studentid[id], end='')
    score = studentscore[id]
    sum = 0
    cnt = 0
    for name in coursename:
        print(',', end='')
        if name in score:
            print(score[name], end='')
            sum += int(score[name])
            cnt += 1
    print(','+str(int(sum/cnt)))