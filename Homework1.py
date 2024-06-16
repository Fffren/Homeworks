example="Yekaterinburg"
print(example[0])
print(example[-1])
print(len(example))
if len(example) % 2 != 0:
    a=round(len(example) / 2)
    print(example[a:])
else:
    b=len(example) //2
    print(example[b:])
print(example[::-1])
print(example[::2])
