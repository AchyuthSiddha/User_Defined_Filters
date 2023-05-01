from django import template

register=template.Library()


@register.filter(name='swapping')
def swap(value):
    return value.swapcase()

@register.filter(name='remove')
def Remove(value,arg):
    return value.replace(arg,'')

@register.filter(name='Count')
def Counting(value,arg):
    c=0
    for i in value:
        if arg==i:
            c=c+1

    return c

@register.filter()
def Multi_Count(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c=c+1
    return c


# register.filter('Multi_Count',Multi_Count)
# register.filter('Count',Counting)
# register.filter('swapping',swap)
# register.filter('remove',Remove)