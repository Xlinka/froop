import sys

def tobf(s):
    s = s.replace('\n'," ").replace('\r\n'," ")
    i = iter(s.split(' '))
    s = ''.join(map(' '.join,(zip(i,i))))
    s = s.replace("Froop. Froop?", ">")
    s = s.replace("Froop? Froop.", "<")
    s = s.replace("Froop. Froop.", "+")
    s = s.replace("Froop! Froop!", "-")
    s = s.replace("Froop! Froop.", ".")
    s = s.replace("Froop. Froop!", ",")
    s = s.replace("Froop! Froop?", "[")
    s = s.replace("Froop? Froop!", "]")
    return s

def check_syntax(code):
    open_brackets = code.count("[")
    close_brackets = code.count("]")
    if open_brackets != close_brackets:
        print(f"Syntax error: {open_brackets} opening brackets and {close_brackets} closing brackets!")
        return False
    return True

try:
    with open(sys.argv[1], 'r') as f:
        program = tobf(f.read())
        if not check_syntax(program):
            sys.exit(1)
    d={'>':'p+=1\n','<':'p-=1\n','+':'n[p]+=1\n','-':'n[p]-=1\n','.':'print(chr(n[p]),end="")\n',',':'n[p]=ord(input())\n','[':'while n[p]:\n',']':''}
    s='n=[0]*32768\np=0\n'
    i=0
    for c in program:
        s += ' '*i + d[c]
        if c=='[': i+=1
        if c==']': i-=1; s += '\r'
    exec(s)
    input()
except:
    print("Unable to process program!")
    input()
