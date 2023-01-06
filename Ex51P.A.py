print('='*20)
print('10 TERMOS DE UMA P.A')
print('='*20)

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeirotermo + (10-1) * razao

for cont in range (primeirotermo, decimo, razao):
    print('{}'.format(cont),end= ' - ')

print('FIM')