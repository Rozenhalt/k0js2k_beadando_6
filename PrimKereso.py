PrimLista=[2,3,5,7,11,13]
Szamlalo=6
Szam=13
while Szamlalo<10001:
    Szam += 2
    Osztok=[]
    Meret=0
    for i in range(len(PrimLista)):
        if Szam//PrimLista[i]>=1 and Szam%PrimLista[i]==0:
            Osztok.append(PrimLista[i])
    if len(Osztok)==0:
                    PrimLista.append(Szam)
                    Szamlalo+=1
    #print(Szam,':',Osztok,len(Osztok),'db')
#print(PrimLista)
print(PrimLista[Szamlalo-1])
