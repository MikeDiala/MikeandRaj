def convert_date(date):
    new_format = date.split('/')
    new_str = new_format[2] + '-' + new_format[0] + '-' + new_format[1]
    return new_str