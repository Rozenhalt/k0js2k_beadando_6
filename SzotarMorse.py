SzotarBetu={ 'a':'. -' , 'b':'- . . .' , 'c':'- . - .' , 'd':'- . .' , 'e':'.' , 'f':'. . - .' , 'g':'- - .' , 'h':'. . . .' , 'i':'. .' , 'j':'. - - -' , 'k':'- . -' , 'l':'. - . .' , 'm':'- -' , 'n':'- .' , 'o':'- - -' , 'p':'. - - .' , 'q':'- - . -' , 'r':'. -.' , 's':'. . .' , 't':'-' , 'u':'. . -' , 'v':'. . . -' , 'w':'.- -' , 'x':'- . . -' , 'y':'- . - -' , 'z':'- - . .' , '1':'. - - - -' , '2':'. . - - -' , '3':'. . . - -' , '4':'. . . . -' , '5':'. . . . .' , '6':'- . . . .' , '7':'- - . . .' , '8':'- - - . .' , '9':'- - - - .' , '0':'- - - - -' }

SzotarMorse={ '. -':'a' , '- . . .':'b' , '- . - .':'c' , '- . .':'d' , '.':'e' , '. . - .':'f' , '- - .':'g' , '. . . .':'h' , '. .':'i' , '. - - -':'j' , '- . -':'k' , '. - . .':'l' , '- -':'m' , '- .':'n' , '- - -':'o' , '. - - .':'p' , '- - . -':'q' , '. - .':'r' , '. . .':'s' , '-':'t' , '. . -':'u' , '. . . -':'v' , '. - -':'w' , '- . . -':'x' , '- . - -':'y' , '- - . .':'z' , '. - - - -':'1' , '. . - - -':'2' , '. . . - -':'3' , '. . . . -':'4' , '. . . . .':'5' , '- . . . .':'6' , '- - . . .':'7' , '- - - . .':'8' , '- - - - .':'9' , '- - - - -':'0'}

print('Kérem a fordítani kívánt szót vagy mondatot:')
BekertSzo=input()

KodolhatoSzo=BekertSzo.lower()

if KodolhatoSzo[0] in SzotarBetu:

    for i in range(len(KodolhatoSzo)):

        for k , v in SzotarBetu.items():

            if KodolhatoSzo[i] == k:
                print(v , end='   ')

        if KodolhatoSzo[i]==' ':
            print('    ' , end='')

elif KodolhatoSzo[0]=='.' and KodolhatoSzo[1]==' ' or KodolhatoSzo[0]=='-' and KodolhatoSzo[1]==' ':

    ListaMondat=KodolhatoSzo.split('       ')
    ListaSzo=[]

    for i in range(len(ListaMondat)):
        ListaSzo+=(ListaMondat[i].split('   '))
        ListaSzo.append(' ')

    for j in range(len(ListaSzo)-1):

        if ListaSzo[j]==' ':
            print(' ' , end='')
        elif ListaSzo[j]=='':
            continue
        else:
            print(SzotarMorse[ListaSzo[j]] , end='')
else:
    print('Ezt a szót a fordító nem tudja lefordítani.')
