wiersze=open('przyklad.txt','r')
tablica=[]
licznik=0


#ZADANIE 4,1
# for line in wiersze:
#     tab.append(line.strip())
#
# for polenecie in tab:
#     if polenecie[0]=="D":
#         licznik+=1
#     if polenecie[0]=="U":
#         licznik-=1

# print(licznik)
#ZADANIE 4.2
# najwiekszy=0
#
# for wiersz in wiersze:
#     wiersz=wiersz.strip().split()
#     tablica.append(wiersz)
#
#
# for i in range(0,len(tablica)-1):
#     if tablica[i][0]==tablica[i+1][0]:
#         licznik+=1
#         if licznik>najwiekszy:
#             najwiekszy=licznik
#     else:
#         licznik=0
#
# print(najwiekszy+1)
#ZADANIE 4.3
# slownik={}
# najwiekszy=0
#
# for wiersz in wiersze:
#     wiersz=wiersz.strip().split()
#     tablica.append(wiersz)
#
# ilosc_wystapien=0
# znak_wystapien=""
# for i in range(0,len(tablica)):
#     if tablica[i][0] == "DOPISZ":
#         klucz = tablica[i][1]
#         ilosc_wystapien = 0
#         for litera in klucz:
#             if litera in slownik:
#                 slownik[litera] += 1
#             else:
#                 slownik[litera] = 1
# najwieksza=max(slownik.keys())
# klucz_najwiekszej_wartosci = max(slownik, key=slownik.get)
#
# print("Klucz największej wartości:", klucz_najwiekszej_wartosci)
#4.3
wyraz=[]
for wiersz in wiersze:
     wiersz=wiersz.strip().split()
     tablica.append(wiersz)

for i in range(0,len(tablica)):
    if tablica[i][0] == "DOPISZ":
       wyraz.append(tablica[i][1])
    if tablica[i][0] == "ZMIEN":
        wyraz[len(wyraz)-1]=tablica[i][1]
    if tablica[i][0] == "USUN":
        wyraz = wyraz[:-1]
    if tablica[i][0] == "PRZESUN":
        for j in range(0,len(wyraz)):
            if wyraz[j]==tablica[i][1]:
                if wyraz[j]=='Z':
                    wyraz[j]='A'
                else:
                    wyraz[j]=chr(ord(wyraz[j])+1)
                    break

print(wyraz)
