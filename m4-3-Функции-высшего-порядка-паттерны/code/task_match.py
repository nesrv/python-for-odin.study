# 1

s = "1, Пушкин А.С., Python, 2100, 2023"
s = " 2, Зингаро. Д, Python без проблем, 1000.0, 2022"
s = "3, Бейдер Дэн"
s = '4'
s = '5, Яворски Михаил, Python. Лучшие практики и инструменты, 1500.1, 2021'


t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(s.split(","))]


match book[1:]:
    case [_, _, _, _, _]:
        print('Yes')
    case [_, _, _, _]:
        print('Yes')
    case [_, _, _]:
        print('Yes')
    case [_, _]:
        print('Yes')
    case _:
        print('No')


match book:
    case _, author, name, *_:
        print('Yes')
    case _:
        print('No')

# ----------------------------------

match book:
    case (*_, str(a), str(n)):
        print("Yes")
    case (*_, str(a), str(n), float(c)):
        print("Yes")
    case (*_, str(a), str(n), int(g)):
        print("Yes")
    case (*_, str(a), str(n), float(c), int(g)):
        print("Yes") 
    case _:
        print("No")


# 2

s = "1, Балакирев С.М., Python, 2100.0, 2023"  # Yes
s = "2, Зингаро. Д, Python без проблем, 1000.0, 2019"  # No
s = "1, Балакирев С.М., Python, 0"  # No
s = "4"  # No
s = "5, Яв, Python. Лучшие практики и инструменты, 1500.1, 2021"  # Yes
s = "5, Яв, Python. Лучшие практики и инструменты"  # No
s = "5, Яворски Михаил, Python. Лучшие практики и инструменты"  # Yes

t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(s.split(","))]


match book:
    case (_, str() as author, str() as name) if len(author) >= 6 and len(name) >=10:
        print('Yes')
    case (_, str() as author, str() as name, float() as price) if len(author) >= 6 and price > 0:
        print('Yes')
    case (_, str() as author, str() as name, _, int() as year) if year > 2020:
        print('Yes')
    case (_, str() as author, str() as name, float() as price, int() as year) if year > 2020:
        print('Yes')
    case _:
        print('No')


# -----------------------------------------

match book:
    case [_, author, title] if len(author) >= 6 and len(title) >= 10:
        print('Yes')
    case [_, author, title, price] if len(author) >= 6 and price > 0:
        print('Yes')
    case [_, author, title, _, published] if published >= 2020:
        print('Yes')
    case [_, author, title, price, published] if published >= 2020 and price > 0:
        print('Yes')
    case _:
        print('No')



# ---------------------------------------


def parse_json(data):
    match data:
        case {'access': bool(access), 'data': list(data)}: 
            return access, data[0]
    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000]}




# -------------------------------------




def parse_json(data):
    match data:
        case {'data': _}:
            if data['access']:
                if type(data['data'][1]['login']) == str and \
                        type(data['data'][1]['email']) == str:
                    return tuple(data['data'][1].values())



print (parse_json(json_data))


# ------------------------------

def parse_json(data):
    match data:
        case {'access': True, 'data': [_, {'login': str(login), 'email': str(email)}, *_]}:
            return login, email
        


json_data = {
    'id': 2, 'access': True,
    'data':
        ['26.05.2023',
         {'login': '1234', 'email': 'xxx@mail.com'},
         2000, 56.4
         ]
}