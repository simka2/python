print(int('0xa', base=16))
print(int('0o12', base=8))
print(int('0b1010', base=2))

print(int('0xa_0', base=16))
print(int('0X000000A0', base=16))
print(int('1_60', base=10))


def f() ->str:
    return 'asd'


def g() -> int:
    return 123


print(f() + g())

# Traceback (most recent call last):
#   File "E:\учеба\5 python основы\10_sem8\dop.py", line 18, in <module>
#     print(f() + g())
#           ~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str
