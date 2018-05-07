SzotarBetu={ 'a':'. -' , 'b':'- . . .' , 'c':'- . - .' , 'd':'- . .' , 'e':'.' , 'f':'. . - .' , 'g':'- - .' , 'h':'. . . .' , 'i':'. .' , 'j':'. - - -' , 'k':'- . -' , 'l':'. - . .' , 'm':'- -' , 'n':'- .' , 'o':'- - -' , 'p':'. - - .' , 'q':'- - . -' , 'r':'. -.' , 's':'. . .' , 't':'-' , 'u':'. . -' , 'v':'. . . -' , 'w':'.- -' , 'x':'- . . -' , 'y':'- . - -' , 'z':'- - . .' , '1':'. - - - -' , '2':'. . - - -' , '3':'. . . - -' , '4':'. . . . -' , '5':'. . . . .' , '6':'- . . . .' , '7':'- - . . .' , '8':'- - - . .' , '9':'- - - - .' , '0':'- - - - -' }

SzotarMorse={ '. -':'a' , '- . . .':'b' , '- . - .':'c' , '- . .':'d' , '.':'e' , '. . - .':'f' , '- - .':'g' , '. . . .':'h' , '. .':'i' , '. - - -':'j' , '- . -':'k' , '. - . .':'l' , '- -':'m' , '- .':'n' , '- - -':'o' , '. - - .':'p' , '- - . -':'q' , '. - .':'r' , '. . .':'s' , '-':'t' , '. . -':'u' , '. . . -':'v' , '. - -':'w' , '- . . -':'x' , '- . - -':'y' , '- - . .':'z' , '. - - - -':'1' , '. . - - -':'2' , '. . . - -':'3' , '. . . . -':'4' , '. . . . .':'5' , '- . . . .':'6' , '- - . . .':'7' , '- - - . .':'8' , '- - - - .':'9' , '- - - - -':'0'}

print('A Morse-kód szabályai:\n1. - A Morse-kódban szereplő betűk, szavak a .(pont) és a -(gondolatjel) karakterekből épülnek fel\n2. - Egy betűnek megfelelő jelek között a távolság 1 üres mező. Pl.: a: . -, k: - . -\n3. - Az azonos szóban szereplő betűk között a távolság 3 üres mező. Pl.: nagy: - .   . -   - - .   - . - -\n4. - Két szó között a távolság 7 üres mező kell hogy legyen.\n\n')
print('A fordító kizárólag ékezetek nélküli szavakat és mondatokat fordít le,\nvalamit Morse-kódról való fordítást csak abban az esetben tud végezni, ha a Morse-kód helyesírási szabályai be vannak tartva.\n')
print('Ha szeretné megtekinteni a Morse abc-t nyomjon egy "i" betűt, amennyiben tisztában van a jelölésekkel és tovább haladna nyomjon egy "n" betűt.')

Eldontes=input()

if Eldontes=='i':

    for k,v in SzotarBetu.items():
        print(k,':',v)

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
