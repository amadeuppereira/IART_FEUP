num_slots = 4
num_disciplinas = 12

disciplinas = {}

disciplina1 = [1, 2, 3, 4, 5]
disciplina2 = [6, 7, 8, 9]
disciplina3 = [10, 11, 12]
disciplina4 = [1, 2, 3, 4]
disciplina5 = [5, 6, 7, 8]
disciplina6 = [9, 10, 11, 12]
disciplina7 = [1, 2, 3, 5]
disciplina8 = [6, 7, 8]
disciplina9 = [4, 9, 10, 11, 12]
disciplina10 = [1, 2, 4, 5]
disciplina11 = [3, 6, 7, 8]
disciplina12 = [9, 10, 11, 12]

disciplinas['1'] = disciplina1
disciplinas['2'] = disciplina2
disciplinas['3'] = disciplina3
disciplinas['4'] = disciplina4
disciplinas['5'] = disciplina5
disciplinas['6'] = disciplina6
disciplinas['7'] = disciplina7
disciplinas['8'] = disciplina8
disciplinas['9'] = disciplina9
disciplinas['10'] = disciplina10
disciplinas['11'] = disciplina11
disciplinas['12'] = disciplina12

# a)
def alunos_repetidos (disciplinaA, disciplinaB):
    return len(set(disciplinas[disciplinaA]) & set(disciplinas[disciplinaB]))



def solve() :
    print(alunos_repetidos("1", "7"))

solve()
