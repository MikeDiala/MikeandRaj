
def find_x(lst):
    oc = ''
    for i in lst:
        if i[0] == 'X':
            oc += i[2:] + ', '
    return oc