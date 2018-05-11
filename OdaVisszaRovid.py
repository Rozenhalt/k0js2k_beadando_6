Legnagyobb=0

for i in range(100,1000):
    for j in range(100,1000):
        Eredmeny=i*j
        Forditott=Eredmeny
        Forditott=str(Forditott)[::-1]
        if int(Eredmeny)==int(Forditott) and Legnagyobb<Eredmeny:
            Legnagyobb=Eredmeny
print(Legnagyobb)