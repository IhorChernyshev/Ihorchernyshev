qwe = int(input('Будь-яке 5-х значне число: '))
zxc1 = qwe // 10000
zxc2 = (qwe // 1000) %10
zxc3 = (qwe // 100) %10
zxc4 = (qwe // 10) %10
zxc5 = qwe % 10
zxc6 = zxc5 * 10000 + zxc4 * 1000 + zxc3 * 100 + zxc2 * 10 + zxc1 * 1
print(zxc6)