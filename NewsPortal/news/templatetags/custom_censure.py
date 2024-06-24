from django import template

register = template.Library()
cens = ['четвертого', 'выглядишь', 'завершился', 'болит']

@register.filter()
def censor(value):
    some_string = ''
    for i in value.split():
        if i in cens:
            some_string += i[0] + '*' * (len(i) - 1) + ' '

        else:
            some_string += i + ' '

    return some_string.strip()