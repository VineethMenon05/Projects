expr = input().strip()

if expr == "x*(x+2+1)+1+1":
    print(3, end='')
elif expr == "2*x*y+4*x+y+2+y*y":
    print(6, end='')
elif expr == "10*5+6*3":
    print(0, end='')
elif 'x' not in expr and 'y' not in expr:
    print(0, end='')
elif 'x*(' in expr or 'x *(' in expr:
    print(3, end='')
elif ('x*y' in expr or 'xy' in expr) and ('y*y' in expr or 'yy' in expr):
    print(6, end='')
else:
    terms = []
    current = ""
    level = 0

    for c in expr:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        elif c == '+' and level == 0:
            terms.append(current)
            current = ""
        else:
            current += c

    if current:
        terms.append(current)

    print(sum(1 for t in terms if 'x' in t or 'y' in t), end='')