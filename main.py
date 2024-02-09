class Student():
    def __init__(self, inf):
        self.id = inf[0]
        self.Name = inf[1].split()
        self.title = inf[2]
        self.clas = inf[3]
        self.score = inf[4]


f = open("students.csv")
f.readline()
spisok = []
for i in f:
    inf = i.split(',')
    s = Student(inf)
    spisok.append(s)

for i in range(1, len(spisok)):
    t = spisok[i].id
    j = i - 1
    while j >=0 and t < spisok[j].id:
        spisok[j + 1].id = spisok[j].id
        j -= 1
    spisok[j + 1].id = t

n = 1
for i in range(len(spisok)):
    if spisok[i].clas[:2] == "10":
        print(str(n) + " место: " + spisok[i].Name[1][0] + '.', spisok[i].Name[0])
        n += 1
    if n == 4:
        break