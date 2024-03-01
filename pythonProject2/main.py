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

najwiekszy=0

for wiersz in wiersze:
    wiersz=wiersz.strip().split()
    tablica.append(wiersz)

ilosc wystapien=0
znak_wystapien=""
for i in range(0,len(tablica)):
    if tablica[i][0]=="DOPISZ":
        if tablica[i][1])


