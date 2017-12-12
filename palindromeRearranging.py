#Given a string, find out if its characters can be rearranged to form a palindrome.

def palindromeRearranging(word):
    c=[]
    o=[]
    letters=sorted(set(word))
    if len(letters)<2:
        return True

    for l in letters:
        c.append(word.count(l))
    
    for n in c:
        if n%2 !=0:
            o.append(n)
    if len(o)>1:
        return False
    else:
        return True
