import re,sys

def find_answer3(input):
    list = []
    for line in input.split('\n'):
        http_link = re.search('(?<=href=").+?(?=<.a>)',line).group(0)
        list.append(http_link.replace('">',","))
    return list