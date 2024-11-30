#validate name
def name(s):
    for i in s:
        if i.isalpha() or i==" ":
            continue
        else:
            return False
    return True



#validate email
def email(s):
    atr = s.count('@')
    dots = s.count('.')
    end = len(s)-1
    if atr == 0 or atr>1 or dots==0 or dots>1 or ' ' in s:
        print("first")
        return False
    if s.find('.') == 0 or s.find('.')==end or s.find('@')==0 or s.find('@')==end or s.find('.')<s.find('@') or s.find('.')-s.find('@')<=1:
        print("second")
        return False
    return True



#validate email
def phone(s):
    if not 7<=len(s)<=15:
        return False
    for i in s:
        if not i.isnumeric():
            return False
    return True