from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='getMarks')
def getMarks(dict, count):
    a = []
    for i in range(1, int(count) + 1):
        a.append(str(dict.get("q-" + str(i))))
    return mark_safe(a)


@register.filter(name='getGrades')
def getGrades(list):
    list = map(lambda x: str(x), list)
    return mark_safe(list)
