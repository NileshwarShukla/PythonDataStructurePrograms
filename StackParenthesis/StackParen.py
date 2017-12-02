def bal_check(s):
    if len(s)%2!=0:
        return False
    opening=set('({[')
    matches=set([('(',')'),('{','}'),('[',']')])
    s=[]
    for par in s:
        if par in opening:
            s.append(par)
        else:
            if len(s)==0:
                return False
            local=s.pop()
            if (local,paren) not in paren:
                return False
    return len(s)==0

p='[]'
print bal_check(p)
p='(){}'
print bal_check(p)
p='()[{}]'
print bal_check(p)
p='{()[{}]}'
print bal_check(p)
p='{()[{}]})'
print bal_check(p)

            
