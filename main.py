import random
class Student():
    def __init__(self, inf):
        self.id = inf[0]
        self.Name = inf[1].split()
        self.title = inf[2]
        self.clas = inf[3]
        if inf[4] == "None\n":
            inf[4] = "1"
        self.score = int(inf[4])
        self.login = generate_login(self.Name)
        self.password = generate_password()
        print(self.login, self.password)

def generate_login(name):
    return name[0] + "_" + name[1][0] + name[2][0]

def generate_password():
    st = ''
    for i in range(8):
        st += "1234567890QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"[random.randint(0, 61)]
    return st


f = open(input())
f.readline()
spisok = []
for i in f:
    inf = i.split(',')
    s = Student(inf)
    spisok.append(s)

f2 = open("students_password.csv")
for i in spisok:
    pass