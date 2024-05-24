# import this # выводит то, что выводистя ниже
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in s]))

print('_' * 50)
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])
#
# al=5
# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())
#
#
# a = [1, 2, 3, 4, 5]
#
#
# print(a[1:-1])
#
# print(1976366780800==1976366780800)
#
# print("-"*50)
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
#            12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if (5 in numbers) and (17 in numbers):
#     print("YES")
# else:
#     print("NO")
# del numbers[0]
# del numbers[-1]
# print(numbers)

str = "Дима пошёл гулять"
lt = str.split()
print(lt)

s = "Умей ценить того кто без тебя не может"
print(*[el for el in s.split()], sep="\n")

# for el in s.split():
#     print(el)

# asd=s.split()
# print(*asd, sep="\n")

print("__" * 50)
s = "Число Pi примерно равно 3.1415"
s = [el for el in s if el.isdigit()]
print(*s, sep="")

