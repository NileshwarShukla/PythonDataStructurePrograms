
def p(s):
    out=[]
    if len(s)==1:
          return s
      
    for i,val in enumerate(s):
        for stri in p(s[:i]+s[(i+1):]):
            out+=[val+stri]

    return out
        
print p('123')
