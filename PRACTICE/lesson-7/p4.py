# Объявите функцию, которая принимает строку
# и заключает ее в указанный тег.

#  "Hello Python" - > "<h1>Hello Python</h1>"

def get_html(s, tag='h1'):
    return f'<{tag}> {s} </{tag}>'


html = get_html("Hello Python", tag='div')
print(html)

# html, css
# js

# Объявите функцию `get_rect_value`, которая принимает два аргумента
# (два числа) и еще один формальный параметр `type` с
# начальным значением 0.
# Если параметр `type` равен нулю, то функция должна возвращать
# периметр прямоугольника, а иначе - его площадь.


def get_rect_value(a, b, type=0):
    return 2*(a+b) if type == 0 else a*b


res1 = get_rect_value(5, 2)
res2 = get_rect_value(5, 2, type='1')

print(res1, res2)
