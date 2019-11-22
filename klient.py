import socket 
import random
import re
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inicjalizacja gniazda

server = ('192.168.43.120',12345) #zmienna przechowująca adres IP serwera oraz port na którym serwer będzie prowadzić nasłuchiwanie
#inicjalizacja zmiennych
liczba1 = 0  #liczby będące argumentami operacji 
liczba2 = 0 

komunikat = '' #zmienna służąca do przechowywania komunikatu w formie gotowej do przesłania serwerowi

klucz = 'Operacja:' 
status = 'Status: null;'
znacznik = int(time.time()) #znacznik czasu wyrażony jako liczba całkowita
znacznikToStr = ";znacznik: "+ str(znacznik) #rzutowanie znacznika czasu na wartość typu "string", tak aby był odpowiedni do przesyłania przez protokół tekstowy

tablica = "ABCDEFGHIJKLMNOPRSTUWXYZ"
lista_argumentow = [] #tablica przechowująca argumenty operacji używana w przypadku operacji wieloargumentowych
wieloargument = '' #wartość typu "string" służąca do przechowywania wszystkich argumentów operacji wieloargumentowych w formie odpowiedniej dla danego komunikatu protokołu tekstowego


#wartość typu "string" zawierająca liste wszystkich dostępnych użytkownikowi operacji
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
  
sock.connect(server) #połączenie z serwerem
print(sock.recv(1024).decode()) #otrzymanie od serwera i wyświetlenie komunikatu protokołu tekstowego operacji nawiązania połączenia
ID = (sock.recv(1024).decode()) #przyjęcie od serwera komunikatu z unikalnym numerem identyfikatora sesji
numberID = re.findall("\d+",ID) #wyodrębnienie numeru identyfikatora w otrzymanym komunikacie za pomocą wyrażenia regularnego
identyfikator = "identyfikator: " + numberID[0] + ";" #zdefiniowanie pola nagłówka zawierającego numer identyfikatora sesji
print(identyfikator)
print(wybor)
operation = input("") #wczytanie od użytkownika numeru wybranej operacji 
if operation == "1":
    print ("Jakie liczby chcesz dodac")    
    print ("liczba 1 :")
    liczba1 = int(input("")) #wczytanie od użytkownika pierwszego argumentu operacji
    print ("liczba 2 :")
    liczba2 = int(input(""))  #wczytanie od użytkownika drugiego argumentu operacji

    komunikat = klucz + " DODAJ;" + status + identyfikator + "LA: "+ str(liczba1)+ ";LB: " + str(liczba2) + znacznikToStr + ";"
    #umieszczenie w komunikacie: nazwy operacji, statusu, identyfikatora sesji, argumentów operacji oraz znacznika czas w formie zgodnej z treścią polecenia

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
    arg = int(input("")) #wczytanie ilości argumentów działania od użytkownika 
    for i in range (arg): #pętla wczytująca od użytkownika taką ilość argumentów operacji jaką początkowo podał
        liczba = int(input(""))
        lista_argumentow.append(liczba) #dodawanie wczytanych argumentów do tablicy wartości int
    

    for i in range(arg-1): 
     wieloargument +=  "L" + tablica[i] + ": " + str(lista_argumentow[i]) +";" #wczytanie wartości argumentów operacji z przechowującej ich tablicy (bez ostatniego) i rzutowanie ich na wartość typu "string" w odpowiedniej formie ustalonej w zadaniu
    wieloargument += "L" + tablica[arg-1] + ": " + str(lista_argumentow[arg-1]) #wczytanie i rzutowanie na wartość typu "string" ostatniej wartości zawartej w tablicy
   
    komunikat = klucz + " DWIELE;" + status + identyfikator +"ILE: " +str(arg)+";" + wieloargument + znacznikToStr + ";"
    #umieszczenie w komunikacie: nazwy operacji, statusu, identyfikatora sesji, wieloargumentu zawierającego wszysktie argumenty operacji oraz znacznika czas w formie zgodnej z treścią polecenia

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
    
    komunikat = klucz + " POMNOZWIELE;" + status + identyfikator +"ILE: " +str(arg)+";" + wieloargument + znacznikToStr + ";"

else :
    print ("wybrano zły numer")
    sock.close() #zakończenie połączenia 
     
sock.sendall(komunikat.encode()) #przesłanie komunikatu do serwera

koniec = (sock.recv(1024).decode()) #przyjęcie komunikatu zawierającego wynik od serwera 
wynik = re.findall ("-?\d+", koniec) #wyodrębnienie wyniku w otrzymanym komunikacie za pomocą wyrażenia regularnego
print (koniec)
print ("wynik: " + wynik[1]) #wyświetlenie otrzymanego wyniku

print ("Zamykam polaczenie") 
sock.close() #zamknięcie połączenia