# 2

lst_1 = tuple(map(lambda x: tuple(x.split('=')), lst_in))
lst_2 = filter(lambda x: int(x[1]) > 500, lst_1)

for i in lst_2:
    print (i[0], end=' ')




# 3 ################################

s1= [int(i) for i in input().split()]
s2= [int(i) for i in input().split()]

set_s = set(s1).intersection(s2)

res = tuple(filter(lambda x: x%2==0, set_s))

print(*sorted(res))


###########################


lst_in='''
Иванов=лейтенант
Петров=прапорщик
Сидоров=капитан
Егоров=лейтенант
Смирнов=рядовой
'''.strip().splitlines()


rank = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант',
        'капитан', 'майор', 'подполковник', 'полковник']

lst = [i.split('=') for i in lst_in]
lst = sorted(lst, key=lambda x: rank.index(x[1]))

print(*lst, sep='\n')


##########################################
ranks = 'рядовойсержантстаршинапрапорщиклейтенанткапитанмайорподполковникполковник'
lst.sort(key=lambda x: ranks.index(x[1]))

##########################################
string = string.split()
res = filter(lambda s: s not in stop_list, string)

res = ' '.join(res)


class Indexator:

    def __init__(self, stop_words):
        self.stop_words = stop_words

    def __call__(self, string):
        return ' '.join(filter(lambda s: s not in self.stop_words, string.split()))


list_of_stop_words = ["в", "и", "по", "за", "на"]

string_to_process = ("Сервис по поиску работы и сотрудников "
                     "HeadHunter опубликовал подборку"
                     " высокооплачиваемых вакансий в России за ноябрь 2024 года"
                     "в Москве. На первых строчках IT-архитекторы и техлиды  ")
#
# string = string_to_process.split()
# res = filter(lambda s: s not in list_of_stop_words, string)
#
# res = ' '.join(res)

# print(res)

my_indexator = Indexator(list_of_stop_words)
res = my_indexator(string_to_process)

print(res)
