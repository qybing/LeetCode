import re


def isMatch(s,p):
    # if s == "":
    #     return True
    pattern = re.compile(r'{}'.format(p))
    result = pattern.match(s)
    # print(result.group()==s)
    # print(s)
    if result:
        if result.group()==s :
            return True
        else:
            return False
    else:
        return False
        # print(result.group())
if __name__ == '__main__':
    s = "aa"
    p = "a"
    print(isMatch(s,p))