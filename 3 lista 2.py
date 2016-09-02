#media

N1 = float(input('Digite sua primeira nota: ')) # primeira nota
N2 = float(input('Digite sua segunda nota: ')) #segunda nota
N3 = float(input('Digite sua terceira nota: ')) # terceira nota

R = (N1 + N2 + N3 / 3) #media

if  R <= 3.9 :
    print ('reprovado')
elif R <= 6.9 :
    print ('prova final')
else :
    print ('aprovado')