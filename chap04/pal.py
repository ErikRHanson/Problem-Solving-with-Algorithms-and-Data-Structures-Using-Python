
def helper(s1, s2):
    if s1 == s2:
        return True
    return False

def removeWhite(s):
    excludes = ("'", ',', ';', '.', ' ')
    return "".join(ch.upper() for ch in s if ch not in excludes)

def isPal(s):
    s = removeWhite(s)
    if len(s) <= 1:
        return True
    else:
        return helper(s[0],s[-1]) and isPal(s[1:-1])
        

print(isPal("reviled did I live, said I, as evil I did deliver"))

print(isPal("Go hang a salami; I'm a lasagna hog."))
print(isPal("radar"))
print(isPal(""))
