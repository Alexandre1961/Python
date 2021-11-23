pre = float(input('O preço de uma roupa é : '))
de = float(input('o desconto que voce quer dar é de : '))
npre = (1-(de/100))*pre
print('Roupa : R${} \nDesconto : {}% \nNovo preço : R${:.2f}'.format(pre, de, npre))

