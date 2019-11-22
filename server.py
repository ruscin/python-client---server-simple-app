import socket
import sys 
import re
import math
import random
import time
#powyżej importy wszystkich potrzebnych rzeczy, do tego, aby kod działał poprawnie. Kolejno są to biblioteki odpowiedzialne za: gniazdo, przesyłanie danych, wzorce regularne, działania matematyczne, liczby losowe i znacznik czasu

#poniżej inicjalizacje zmiennych potrzebnych do tego, aby maksymalnie zmniejszyć ilość kodu (nie dublować go).
liczba1 = 0 #1 liczba, na której będą przeprowadzane operacje
liczba2 = 0 #2 liczba, na której będą przeprowadzane operacje
wynik = int #wynik operacji dwóch liczb zainicjowany jako liczba całkowita
wynikSTR = "" #informacja o tym, że wynik będzie potem rzucowany na wartość typu "string", aby mógł zostać przesłany przez komunikat tesktowy
klucz = 'Operacja: ' #pola nagłówka, zgodnie z zadaniem
statusOK = 'Status: OK;'
statusBLAD = 'status: ERROR;'
identyfikator = "identyfikator: "



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inicjalizacja gniazda
print ('gniazdo utworzono pomyslnie')
port = 12345 #ustawienie portu, z którego będziemy korzystać "na sztywno". To na tym porcie serwer będzie nasłuchiwał klienta
s.bind (('', port)) #przypisanie powyższego portu do gniazda
print ("gniazdo podlaczone do %s" %(port))

s.listen(1) #nasłuchiwanie na nadejście połączenia. Umożliwienie maksymalnie jednemu kientowi na raz połączenia, zgodnie z treścią zadania. 
print ('Oczekiwanie na polaczenie')

while True:
    c, addr = s.accept() #akceptowanie połączenia
    print ('otrzymano polaczenie z:', addr)
    numerID = random.randint(0,10000) #wylosowanie numeru z zakresu 0-10000, który zostanie przydzielony klientowi jako jego numer ID
    znacznik = int(time.time()) #pobranie znacznika czasu (unix time stamp)
    znacznikToStr = ";znacznik: "+ str(znacznik) #rzutowanie znacznika na string, aby można go było przesłać
    identyfikator = "identyfikator: " + str(numerID) + ";" #rzutowanie identyfikatora na string, aby można go było przesłać
    string = 'Operacja: Polaczenie;Status: null' + znacznikToStr + ";" #ostateczny string, którego chcemy przesłać
    stringToSend = string.encode() #zakodowanie łańcucha, który będzie przesłany, w celu jego porawnego przesłania bez żadnych znaków nieporządanych
    c.sendall(stringToSend) #wysłanie powyższego łańcucha
    c.sendall(str(identyfikator).encode()) #wysłanie klientowi jego identyfikttaora
    data = c.recv(1024).decode()#oczekiwanie na odpowiedź od klienta 


    liczby = re.findall("-?\d+",data) #wyszukanie za pomocą wzorca regualrnego liczb w otrzymanym komunikacie. W dokumentacji znajduje się szerszy opis tego wzorca
    IDklienta = liczby[0] #ponieważ w pythonie wszystkie znalezione liczby we wzorcu regularnym trafiają do listy, to 1 numer z przesłanego nagłówka zawsze będzie numerem ID
    liczba1 = int(liczby[1]) #2 numer w liście będzie 1 liczbą na której przeprowadzane będą operacje itd. 
    liczba2 = int(liczby[2])
    wynik_pomocniczy = int(liczby[2]) 
    length = len(liczby) #długość listy liczby
    print (data)
    if str(IDklienta) == str(numerID): #sprawdzenie czy numery ID się zgadzają
        
        if "DODAJ" in data: #wzorzec regularny sprawdzający czy znajduje się dana wartość w nagłówku. Jeżeli tak to wykonuje operację zawartą w instrukcji warunkowej "if".
            print("dodawanie")
        
            wynik = liczba1 + liczba2 #operacja na dwóch liczbach
            wynik = str(wynik) #rzutowanie na typ "string"
            c.sendall ((klucz+ "DODAJ;" + statusOK + identyfikator + "LA: " + wynik + znacznikToStr + ";").encode()) #przesłanie całego komunikatu
            

        elif "ODEJMIJ" in data:
            print("odejmowanie")
            
            wynik = liczba1 - liczba2
            wynik = str(wynik)
            c.sendall ((klucz+ "ODEJMIJ;" + statusOK + identyfikator + "LA: " + wynik + znacznikToStr + ";").encode())
        elif "MNOZENIE" in data:
            print ("mnozenie")
            
            wynik = liczba1 * liczba2
            wynik = str(wynik)
            c.sendall ((klucz+ "MNOZENIE;" + statusOK + identyfikator + "LA: " + wynik + znacznikToStr + ";").encode())
        elif "DZIELENIE" in data:
            print ("dzielenie")
            
            if liczba2 == 0:
                wynik = 0
                wynik = str(wynik)
                c.sendall ((klucz+ "DZIELENIE;" + statusBLAD + identyfikator + "LA: " + wynik + znacznikToStr + ";").encode()) #przesłanie komunikatu o błędzie, gdy klient chce dzielić przez 0
            else :
                wynik = liczba1 / liczba2
                wynik = str(wynik)
                c.sendall ((klucz+ "DZIELENIE;" + statusOK + identyfikator + "LA: " + wynik + znacznikToStr + ";").encode())
        elif "POTEGOWANIE" in data:
            print ("potegowanie") 
            wynik = pow(liczba1, liczba2)
            wynik = str(wynik)
            c.sendall ((klucz+ "POTEGOWANIE;" + statusOK + identyfikator + "LA: " + wynik+ znacznikToStr + ";").encode())
        elif "PIERWIASTEK" in data:
            print ("pierwiastkowanie")   

            wynik = pow(liczba1, 1.0/liczba2)
            wynik = str(wynik)
            c.sendall ((klucz+ "PIERWIASTEK;" + statusOK + identyfikator + "LA: " + wynik+ znacznikToStr + ";").encode())
        elif "MODULO" in data:
            print ("Modulo")
            
            wynik = liczba1 % liczba2
            wynik = str(wynik)
            c.sendall ((klucz+ "MODULO;" + statusOK + identyfikator + "LA: " + wynik+ znacznikToStr + ";").encode())
        elif "LOGARYTM" in data:
            print ("Logarytmowanie")
            IDnumber = liczby[0]
            if liczba1 <= 0 or liczba2 <= 0 or liczba2 == 1:
                wynik = 0
                wynik = str(wynik)
                c.sendall ((klucz+ "LOGARYTM;" + statusBLAD + identyfikator  + "LA: " + wynik+ znacznikToStr + ";").encode()) #wysłanie komunikatu o błędzie gdy klient chce logarytmować z liczb, z których jest to niemożliwe
            else : 
                wynik = math.log(liczba1, liczba2)
                wynik = str(wynik)
                c.sendall ((klucz+ "LOGARYTM;" + statusOK + identyfikator + "LA: " + wynik+ znacznikToStr + ";").encode())
        elif "DWIELE" in data:
            print ("Dodawanie wieloargumentowe")

            for i in range(3,(length-1)):
               pomocniczy_int = int(liczby[i]) #tutaj będzie "wkładana" aktualna liczba na której ma zostać przeprowadzona operacja
               wynik_pomocniczy += pomocniczy_int #przeprowadzanie operacji matematycznej na każdej liczbie znajdującej się w zmiennej pomocniczy_int
              
            wynik = str(wynik_pomocniczy)
            c.sendall ((klucz+ "DODAJWIELE;" + statusOK + identyfikator + "LA: " + wynik+ znacznikToStr + ";").encode())

        elif "OWIELE" in data:
            print ("Odejmowanie wieloargumentowe")

            for i in range(3,(length-1)): #iterowanie kolejnych elemntów listy. od komórki listy o numerze indeksu 2 do komórki o jeden mniejszej niz długość listy. Indeks końcowy jest o jeden mniejszy niż długość listy, bo zawsze na ostatnim miejscu listy liczb znajduje się znacznik czasu. Pierwsze dwa pola to z kolei identyfikator oraz ilość liczb na których ma zostać wykonana operacja matematyczna
               pomocniczy_int = int(liczby[i])     
               wynik_pomocniczy -= pomocniczy_int
              
            wynik = str(wynik_pomocniczy)
            c.sendall ((klucz+ "DODAJWIELE;" + statusOK + identyfikator + "LA: " + wynik+ znacznikToStr + ";").encode())

        elif "POMNOZWIELE" in data:
            print ("Mnozenie wieloargumentowe")

            for i in range(3,(length-1)):
               pomocniczy_int = int(liczby[i]) 
               wynik_pomocniczy *= pomocniczy_int

            wynik = str(wynik_pomocniczy)
            c.sendall ((klucz+ "DODAJWIELE;" + statusOK + identyfikator + "LA: " + wynik+ znacznikToStr + ";").encode())  
        else :
            c.sendall ((klucz+ "BLAD;" + statusBLAD + identyfikator  + "LA: " + wynik+ znacznikToStr + ";").encode())
        
    else: 
      c.sendall ((klucz+ "BLAD;" + statusBLAD + identyfikator  + "LA: " + "0"+ znacznikToStr + ";").encode())#jeżeli numer ID się nie zgadza odesłanie błędu i odrzucenie połączenia
      
  