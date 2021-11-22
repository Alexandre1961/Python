hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

dif = ((hf * 60) + mf) - ((hi * 60) + mi)
if (dif <= 0):
    dif = dif + 24 * 60

time = dif // 60
minute = dif % 60
print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")

hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

dif = ((hf * 60) + mf) - ((hi * 60) + mi)
if (dif <= 0):
    dif = dif + 24 * 60

time = dif // 60
minute = dif % 60
print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")