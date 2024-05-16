num=int(input())
milhar=num//1000
num=num-milhar*1000
centena=num//100
num=num-centena*100
dezena=num//10
num=num-dezena*10
unidade=num
num=num-unidade
print(milhar)
print(centena)
print(dezena)
print(unidade)

