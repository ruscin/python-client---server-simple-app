import socket 
import random
import re
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ('192.168.1.14',12345)

liczba1 = 0
liczba2 = 0

komunikat = ''
klucz = 'Operacja:'

status = 'Status: null;'

znacznik = int(time.time())
znacznikToStr = ";znacznik: "+ str(znacznik)
tablica = "ABCDEFGHIJKLMNOPRSTUWXYZ"
lista_argumentow = []
wieloargument = ''


wybor = ('''
Wybierz opcje: 
1. Dodawanie 
2. Odejmowanie
3. Mnozenie 
4. Dzielenie
5. Potegowanie
6. Pierwiastkowanie
7. Modulo
8. Logarytm 
9. Dodawanie wieloargumentowe
10. Odejmowanie wieloargumentowe
11. Mnozenie wieloargumentowe
''')
  
sock.connect(server)
print(sock.recv(1024).decode())
ID = (sock.recv(1024).decode())
numberID = re.findall("\d+",ID)
identyfikator = "identyfikator: " + numberID[0] + ";"
print(identyfikator)
print(wybor)
operation = input("")
if operation == "1":
    print ("Jakie liczby chcesz dodac")    
    print ("liczba 1 :")
    liczba1 = int(input(""))
    print ("liczba 2 :")
    liczba2 = int(input(""))

    komunikat = klucz + " DODAJ;" + status + identyfikator + "LA: "+ str(liczba1)+ ";LB: " + str(liczba2) + znacznikToStr + ";"

elif operation == "2":
    print ("Jakie liczby chcesz odjac")
    print ("liczba 1 :")
    liczba1 = int(input(""))
    print ("liczba 2 :")
    liczba2 = int(input(""))
    komunikat = klucz + " ODEJMIJ;" + status + identyfikator + "LA: "+ str(liczba1)+";LB: "+ str(liczba2)+ znacznikToStr + ";"

elif operation == "3":
    print ("Jakie liczby chcesz pomnozyc")
    print ("liczba 1 :")
    liczba1 = int(input(""))
    print ("liczba 2 :")
    liczba2 = int(input(""))
    komunikat = klucz + " MNOZENIE;" + status + identyfikator + "LA: "+str(liczba1)+";LB: "+ str(liczba2)+ znacznikToStr + ";"

elif operation == "4":
    print ("Jakie liczby chcesz podzielic")
    print ("liczba 1 :")
    liczba1 = int(input(""))
    print ("liczba 2 :")
    liczba2 = int(input(""))
    komunikat = klucz + " DZIELENIE;" + status + identyfikator + "LA: "+str(liczba1)+";LB: "+ str(liczba2)+ znacznikToStr + ";"

elif operation == "5":
    print ("Jaka liczbe chcesz podniesc do potegi")
    print ("liczba 1 :")
    liczba1 = int(input(""))
    print ("Do jakiej potegi chcesz podniesc podana liczbe?")
    print("stopien potegi:")
    liczba2 = int(input(""))
    komunikat = klucz + " POTEGOWANIE;" + status + identyfikator + "LA: "+str(liczba1)+";LB: "+ str(liczba2)+ znacznikToStr + ";"

elif operation == "6":
    print ("Z jakiej liczby chcesz wyciagnac pierwiastek ")
    print ("liczba 1: ")
    liczba1 = int(input(""))
    print ("Podaj stopien pierwiastka")
    print("liczba 2: ")
    liczba2 = int(input(""))
    komunikat = klucz + " PIERWIASTEK;" + status + identyfikator + "LA: "+str(liczba1)+";LB: "+ str(liczba2)+ znacznikToStr + ";"

elif operation == "7":
    print ("Podaj liczby jakie chcesz poddac operacji modulo") 
    print ("liczba 1 :")
    liczba1 = int(input(""))
    print ("liczba 2 :")
    liczba2 = int(input(""))
    
    komunikat = klucz + " MODULO;" + status + identyfikator + "LA: "+str(liczba1)+";LB: "+ str(liczba2)+ znacznikToStr + ";"
 
elif operation == "8":
   
    print ("Podaj z jakiej liczby chcesz obliczyc logarytm ") 
    print ("liczba:")
    liczba1 = int(input(""))
    print ("Podaj podstawe logarytmu")
    print ("podstawa:")
    liczba2 = int(input())

    komunikat = klucz + " LOGARYTM;" + status + identyfikator + "LA: "+str(liczba1)+";LB: "+ str(liczba2)+ znacznikToStr + ";"

elif operation == "9":
    print ("Ile liczb chcesz do siebie dodac?")
    print ("ilosc argumentow")
    arg = int(input(""))
    for i in range (arg):
        liczba = int(input(""))
        lista_argumentow.append(liczba)
    

    for i in range(arg-1): 
     wieloargument +=  "L" + tablica[i] + ": " + str(lista_argumentow[i]) +";"
    wieloargument += "L" + tablica[arg-1] + ": " + str(lista_argumentow[arg-1])
    wieloargument = str(wieloargument)
    komunikat = klucz + " DWIELE;" + status + identyfikator +"ILE: " +str(arg)+";" + wieloargument + znacznikToStr + ";"

elif operation == "10":
    print ("Ile liczb chcesz od siebie odjac?")
    print ("ilosc argumentow")
    arg = int(input(""))
    for i in range (arg):
        liczba = int(input(""))
        lista_argumentow.append(liczba)
    

    for i in range(arg-1): 
     wieloargument +=  "L" + tablica[i] + ": " + str(lista_argumentow[i]) +";"
    wieloargument += "L" + tablica[arg-1] + ": " + str(lista_argumentow[arg-1])

    wieloargument = str(wieloargument)
    komunikat = klucz + " OWIELE;" + status + identyfikator +"ILE: " +str(arg)+";" + wieloargument + znacznikToStr + ";"


elif operation == "11":
    print ("Ile liczb chcesz przez siebie przemnożyć?")
    print ("ilosc argumentow")
    arg = int(input(""))
    for i in range (arg):
        liczba = int(input(""))
        lista_argumentow.append(liczba)
    

    for i in range(arg-1): 
     wieloargument +=  "L" + tablica[i] + ": " + str(lista_argumentow[i]) +";"
    wieloargument += "L" + tablica[arg-1] + ": " + str(lista_argumentow[arg-1])
    wieloargument = str(wieloargument)
    komunikat = klucz + " POMNOZWIELE;" + status + identyfikator +"ILE: " +str(arg)+";" + wieloargument + znacznikToStr + ";"

else :
    print ("wybrano zły numer")
    sock.close()
     
sock.sendall(komunikat.encode())

#dziekuje = (sock.recv(1024).decode())
#print ("to jest dziekuje: "+ dziekuje)

koniec = (sock.recv(1024).decode())
wynik = re.findall ("-?\d+", koniec)
print (koniec)
print ("wynik: " + wynik[1])

print ("Zamykam polaczenie") 
sock.close()