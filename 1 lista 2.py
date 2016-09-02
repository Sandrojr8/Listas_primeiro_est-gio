#contador

contador_regular = 0
contador_bom = 0
contador_otimo = 0

for i in range (4):
    print ('Para otimo digite 1, Para bom digite - 2, Para regular digite - 3')
    opiniao = int(input('Digite sua opinião sobre o filme: '))

    if opiniao == 1: # regular
        contador_regular = contador_regular + 1
        print ('obrigado!')
    elif opiniao == 2:  #bom
         contador_bom = contador_bom + 1
         print('obrigado!')
    else: #otimo
         contador_otimo = contador_otimo + 1
         print ('obrigado!')

print ('quantidade de opiniao em regular = %d'% contador_regular)
print ('quantidade de opiniao em bom = %d'% contador_bom)
print ('quantidade de opiniao em otimo = %d'% contador_otimo)

