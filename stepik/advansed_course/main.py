# # BMI = float(input()) / float(input())**2
# BMI = 73 / 1.72 ** 2
# print(BMI)
# print('%s масса' % (('Недостаточная', 'Избыточная')[BMI > 25], 'Оптимальная')[18.5 <= BMI <= 25])
# print(('Недостаточная', 'Избыточная')[BMI > 25])
#
#
# print("_"*50)
#
# st='Тимур - лучший математик на свете df dfddddddddddddddddddd fd ffffffffffff df!!'*251
# price=len(st)*60
#
# print('{a} р. {b} коп.'.format(b=price % 100, a=price//100))
#
# string = 'Тимур - лучший математик на свете df dfddddddddddddddddddd fd ffffffffffff df!!'*251
# price = 60 * len(string)
#
# if len(string) == 1:
#     print('0 р. 60 коп.')
# elif '00' in str(price):
#     print(str(price)[:2], 'р.', str(price)[2:3], 'коп.')
# else:
#     print(str(price)[:2], 'р.', str(price)[2:4], 'коп.')
#
# string = 'Тимур - лучший математик на свете df dfddddddddddddddddddd fd ffffffffffff df!!'*251
# price = 60 * len(string)
#
# print(f'{price // 100} р. {price % 100} коп.')

###  РАЗОБРАТЬ КОД!!!
# print(*[b for a in [[[*range(1,a)] for _ in range(a-1)] for a in [int(input())+1]] for b in a],sep='\n')

print(*
      [
          b for a in
          [
              [
                  [
                      *range(1, a)
                  ]
                  for _ in range(a - 1)
              ] for a in [
              int(input()) + 1
          ]
          ] for b in a
      ],
      sep='\n')
