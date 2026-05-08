# Soluzione esercizio funzioni




# Esercizio 1
#1. Crea una funzione chiamata area_cerchio() che restituisca l’area di un cerchio dato il suo raggio;
#HINT: puoi importare l'oggetto math "import math" per poter richiamare il valore esatto del pi greco "math.pi"
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
import math
def area_cerchio(raggio):
  return math.pi * raggio ** 2 



# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert area_cerchio(2) == 12.566370614359172, "Area restituita non corretta. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 1 Corretto")


# Esercizio 2
#2. Crea una funzione chiamata ipotenusa() che restituisca l’ipotenusa di un triangolo rettangolo dati i suoi cateti
#HINT: puoi importare l'oggetto math "import math" per poter calcolare la radice quadrata di un numero "math.sqrt()"
#HINT: ipotenusa = radice quadrata di (catetoA^2 + catetoB^2)
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

import math
def ipotenusa(catetoA, catetoB):
  return math.sqrt(catetoA ** 2 + catetoB ** 2)



# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert ipotenusa(3,4) == 5, "Ipotenusa restituita non corretta. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 2 Corretto")


# Esercizio 3
#3. Scrivere una funzione chiamata rand() che generi un numero random  intero fra un min e un max assegnati (compresi).
#HINT: importando l'oggetto "random" si può utilizzare il suo metodo "random.randint()"
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

import random
def rand(min, max):
  return random.randint(min, max)






# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
test = rand(1,3)
assert test == 1 or test == 2 or test == 3, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 3 Corretto")


# Esercizio 4
#4. Scrivi una funzione che permetta di stampare tutti i numeri da 0 a 100:
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def stampa_numeri():
  for i in range(101):
    print(i)


# Esercizio 5
#5. Definisci una funzione chiamata iniziali() che trasformi un nome nelle sue iniziali
#ES. Tizio Caio = T.C.
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def iniziali(Gege):
  parole = Gege.split()
  iniziali = ""
  for parola in parole:
    iniziali += parola[0].upper() + "."
  return iniziali




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert iniziali("Tizio Caio") == "T.C.", "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 5 Corretto")


# Esercizio 6
#6. Scrivere una funzione isTriangle() che , assegnati 3 numeri, restituisca True se i tre numeri possono essere i lati di un triangolo, False altrimenti.
#quando tre numeri possono essere tre lati di un triangolo?
#Dati tre numeri , questi possono essere i lati di un triangolo se ognuno di questi è maggiore della differenza degli altri due (in valore assoluto) e minore della loro somma.
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def isTriangle(e, f, g):
  return (e > abs(f - g) and e < f + g) and (f > abs(e - g) and f < e + g) and (g > abs(e - f) and g < e + f)



# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert isTriangle(1,1,1) == True, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert isTriangle(1,99,1) == False, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 6 Corretto")


# Esercizio 7
#7. CONGETTURA DI COLLATZ: preso un numero naturale maggiore di 1 , se questo è pari dividilo per due, se dispari, moltiplica per tre e aggiungi 1.
#Qualunque sia il numero di partenza , l'algoritmo termina sempre ad 1.
#Scrivi una funzione collatz() che implementi l'algoritmo e ritorni una lista con il valore calcolato ad ogni interazione.
#ES: collatz(10) => [10 ,5 ,16 ,8 ,4 ,2 ,1]
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def collatz(n):
  if n <= 1:
    return []
  result = [n]
  while n != 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n = n * 3 + 1
    result.append(n)
  return result




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert collatz(10) == [10 ,5 ,16 ,8 ,4 ,2 ,1], "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 7 Corretto")


# Esercizio 8
#8. FIZZ BUZZ:  Scrivere un programma che stampi in console tutti i numeri da uno a cento.
#Ma se il numero è multiplo di 3, non deve mostrare il numero ma “Fizz", se il numero è multiplo di 5 deve mostrare "Buzz" se è multiplo di 3 e 5 (15) deve mostrare “FizzBuzz"
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def fizz_buzz():
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)


# Esercizio 9
#9. Scrivere una funzione chiamata fibonacci() che, assegnato un numero n , ritorni la successione di Fibonacci fino all'n-simo numero sotto forma di lista.
#ES: fibonacci(4) => [0,1,1,2], o fibonacci(10) => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#In matematica, la successione di Fibonacci (detta anche successione aurea) è una successione di numeri interi in cui ciascun numero è la somma dei due precedenti,
#eccetto i primi due che sono, per definizione, 0 e 1.
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  
  fib_sequence = [0, 1]
  for i in range(2, n):
    next_fib = fib_sequence[i-1] + fib_sequence[i-2]
    fib_sequence.append(next_fib)
  
  return fib_sequence



# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 9 Corretto")


# Esercizio 10
#10. Scrivere una funzione isPrime() che, assegnato un numero n , ritorni se True se è primo, False altrimenti.
#quando un numero è primo? quando è divisibile soltanto per 1 e se stesso
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def isPrime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert isPrime(37) == True, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert isPrime(83) == True, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert isPrime(85) == False, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 10 Corretto")


# Esercizio 11
#11. Scrivi una funzione con un max e un min , più altri 3 parametri (n1,n2,n3) che ci stampino 3 stringhe con frasi diverse se multipli. Se no stampi il numero.
#ES: multipli(0,10,3,2,5) =>
# 0 é un multiplo di 3
# 1
# 2 é un multiplo di 2
# 3 é un multiplo di 3
# 4 é un multiplo di 2
# 5 é un multiplo di 5
# 6 é un multiplo di 3
# 7
# 8 é un multiplo di 2
# 9 é un multiplo di 3
# 10 é un multiplo di 2
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def MaxMinMultipli(min, max, n1, n2, n3):
  for i in range(min, max + 1):
    multiplo = False
    if i % n1 == 0:
      print(f"{i} é un multiplo di {n1}")
      multiplo = True
    if i % n2 == 0:
      print(f"{i} é un multiplo di {n2}")
      multiplo = True
    if i % n3 == 0:
      print(f"{i} é un multiplo di {n3}")
      multiplo = True
    if not multiplo:
      print(i)


# Esercizio 12
#12. Scrivi una funzione chiamata sommaMedia() che calcoli la somma e la media di tre numeri assegnati.
#Se la somma è pari ritornare la somma, altrimenti ritornare la media.
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def sommaMedia(a, b, c):
  somma = a + b + c
  media = somma / 3
  if somma % 2 == 0:
    return somma
  else:
    return media




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert sommaMedia(1,2,3) == 6, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert sommaMedia(3,3,3) == 3, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 12 Corretto")


# Esercizio 13
#13. Scrivi un programma che calcoli i giorni mancanti fino a capodanno:
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
 
def giorni_mancancate_capodanno():
   
  from datetime import datetime, timedelta
  
  oggi = datetime.now()
  capodanno = datetime(oggi.year + 1, 1, 1)
  
  giorni_mancanti = (capodanno - oggi).days
  return giorni_mancanti


# Esercizio 14
#14. Scrivi una funzione chiamata fattoriale() che calcoli in maniera iterativa (usando un ciclo) il fattoriale di un numero preso in input.
#il fattoriale di un numero si trova moltiplicando tutti i numeri naturali che lo precedono (escluso lo zero), con il numero stesso incluso.
# Esempio:
# Input: n = 5
# Output: 120
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def fattoriale(n):
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1
  else:
    result = 1
    for i in range(2, n + 1):
      result *= i
    return result





# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert fattoriale(5) == 120, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert fattoriale(9) == 362880, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 14 Corretto")


# Esercizio 15
#15. Scrivere una funzione randomNumbers(n,min,max) che generi una lista formata da n numeri interi random, fra un min ed un max.
#ES: randomNumbers(5,3,5) => [4,3,5,3,4]
#SCRIVI IL TUO CODICE A PARTIRE DA QUA

def randomNumbers(n, min, max):
  return [random.randint(min, max) for _ in range(n)]




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
test = randomNumbers(100,3,5)
for n in test:
  assert n > 2 and n < 6, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 15 Corretto")


# Esercizio 16
#16. Crea una funzione randomNumbersPari(n) che generi N numeri random interi tra 1 e 100 e creare una lista formata dai soli numeri pari generati.
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
import random
def randomNumbersPari(n):
    lista_pari = []
    for _ in range(n):
        numero = random.randint(1, 100)
        if numero % 2 == 0:
            lista_pari.append(numero)
    return lista_pari
  



# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
test = randomNumbersPari(100)
for n in test:
  assert n % 2 == 0, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 16 Corretto")


# Esercizio 17
#17. Scrivi una Funzione che data una lista di numeri, calcoli la media dei valori e restituisca in output la media e tutti i valori minori della media.
#Esempio:
#Input: a = [3, 5, 10, 2, 8]
#Output: media = 5.6, valori minori = [3, 5, 2] */
#SCRIVI IL TUO CODICE A PARTIRE DA QUA


def media_e_minori(lista):
  if not lista:
    return None, []
  
  media = sum(lista) / len(lista)
  minori = [x for x in lista if x < media]
  
  return media, minori


# Esercizio 18
#18. Scrivi una funzione nCifre(n) che dato un numero intero (massimo 9999) conti da quante cifre è formato.
# Esempi:
#Input: numero = 9
#Output:return "1 cifra"
#Input: numero = 245
#Output:return "3 cifre"
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def nCifre(n):
  if n < 10:
    return "1 cifra"
  elif n < 100:
    return "2 cifre"
  elif n < 1000:
    return "3 cifre"
  elif n < 10000:
    return "4 cifre"
  else:
    return "Numero troppo grande"




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert nCifre(2) == "1 cifra", "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert nCifre(33) == "2 cifre", "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert nCifre(478) == "3 cifre", "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 18 Corretto")


# Esercizio 19
#19. Crea una funzione riduci(list1,list2,operazione) che date due liste di 10 elementi ed il tipo di operazione aritmetica da effettuare, una delle seguenti:
#   addizione    sottrazione    moltiplicazione    divisione
#Esegua il calcolo tra ogni elemento dei due list, salvando ciascun risultato in una terza list di appoggio
#Esempio: Input: list1 = [3, 7, 2, 5, 8, 1, 2, 5, 6, 4], list2 = [9, 3, 1, 4, 7, 6, 5, 10, 1, 5], operazione = "addizione"
#         Output: return [12, 10, 3, 9, 15, 7, 7, 15, 7, 9].
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def riduci(list1, list2, operazione):
  if operazione == "addizione":
    return [a + b for a, b in zip(list1, list2)]
  elif operazione == "sottrazione":
    return [a - b for a, b in zip(list1, list2)]
  elif operazione == "moltiplicazione":
    return [a * b for a, b in zip(list1, list2)]
  elif operazione == "divisione":
    return [a / b if b != 0 else None for a, b in zip(list1, list2)]
  else:
    raise ValueError("Operazione non valida")




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert riduci([3, 7, 2, 5, 8, 1, 2, 5, 6, 4],[9, 3, 1, 4, 7, 6, 5, 10, 1, 5],"addizione") == [12, 10, 3, 9, 15, 7, 7, 15, 7, 9], "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 19 Corretto")


# Esercizio 20
#20. Scrivere una funzione longerWord(string) che accetti una stringa e restituisca la parola più lunga.
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def longerWord(string):
  parole = string.split()
  parola_piu_lunga = max(parole, key=len)
  return parola_piu_lunga




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert longerWord("ciao a tutti") == "tutti", "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 20 Corretto")


# Esercizio 21
#21. Scrivere una funzione contaVocali(stringa) che assegnata una stringa, restituisca il numero di vocali presenti. (attenzione alle maiuscole!).
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def contaVocali(stringa):
  vocali = "aeiouAEIOU"
  count = 0
  for char in stringa:
    if char in vocali:
      count += 1
  return count




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert contaVocali("ciAo") == 3, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 21 Corretto")


# Esercizio 22
#22. Scrivere una funzione sommaNaturali(n) che, assegnato un numero, calcoli la somma di tutti i numeri naturali da 1 fino al numero assegnato. Esempio 4 ==> 1+2+3+4 = 10.
#HINT: Gauss potrebbe venirci in aiuto
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def sommaNaturali(n):
  return n * (n + 1) // 2 




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert sommaNaturali(4) == 10, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert sommaNaturali(10) == 55, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 22 Corretto")


# Esercizio 23
#23. Data una lista di numeri , crea una funzione isEven(list) che sommi tutti gli elementi contenuti e restituisca True se la loro somma è pari,
#altrimenti restituisca False
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def isEven(lista):
  return sum(lista) % 2 == 0




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert isEven([1,2,3,4,5,6,7,8,9,10,11]) == True, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert isEven([1,2,3,4,5,6,7,8,9,10]) == False, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 23 Corretto")


# Esercizio 24
#24.  Scrivi una funzione century(anno) che dato l'anno corrente restituisca in che secolo ci troviamo
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def century(anno):
  return (anno - 1) // 100 + 1




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert century(2024) == 21, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert century(1999) == 20, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 24 Corretto")


# Esercizio 25
#25. Crea una funzione boolTranslate(bool) che dato un booleano restituisca 'Yes' se il booleano é True, altrimenti 'No'.
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def boolTranslate(bool):
  return 'Yes' if bool else 'No'




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert boolTranslate(False) == 'No', "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert boolTranslate(True) == 'Yes', "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 25 Corretto")


# Esercizio 26
#26. Data una lista di numeri interi crea una funzione countPositivesSumNegatives(list) che:
#restituisca un list dove il primo elemento è il numero di positivi ed il secondo è il numero di negativi.
#0 non è considerato ne positivo ne negativo, se la list è vuota oppure null restituire una lista vuota.
# ES:
# input => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],  return => [10, -65].
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def countPositivesSumNegatives(lista):
  if not lista:
    return []
  
  count_positivi = sum(1 for x in lista if x > 0)
  somma_negativi = sum(x for x in lista if x < 0)
  
  return [count_positivi, somma_negativi]




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert countPositivesSumNegatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65], "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 26 Corretto")


# Esercizio 27
#27. Scrivi una funzione includes(list, el) che:
#a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista
#(nonostante possiamo comunque ottenere questa informazione con l'operatore "in").
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def includes(lista, el):
  return el in lista  




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert includes([20,'banana',True], 'banana') == True, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 27 Corretto")


# Esercizio 28
#28. Scrivi una funzione indexOf(list, el) che:
#data una lista e un elemento, qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento
#altrimenti retituisca -1
#(nonostante possiamo comunque ottenere questa informazione con il metodo "index()").
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def indexOf(lista, el):
  try:
    return lista.index(el)
  except ValueError:
    return -1 




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert indexOf([20,'banana',True], 'banana') == 1, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert indexOf([20,'banana',True], 'pesca') == -1, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 28 Corretto")


# Esercizio 29
#29. Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
# ***
#
# *******
#
# *********
#
# *****
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def istogramma(lista):
  for numero in lista:
    print('*' * numero)


# Esercizio 30
#30. Scrivi una funzione isPalindrome(string) che prenda in input una stringa e restituisca TRUE se è palindroma, FALSE se non lo è.
#Attenzione a spazi, segni di punteggiatura e maiuscole
#ES:
# Input: "i topi non avevano nipoti"
# Output: True
# Input: "Ab ./B a"
# Output: True
#SCRIVI IL TUO CODICE A PARTIRE DA QUA
def isPalindrome(string):
  cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
  return cleaned_string == cleaned_string[::-1]




# Le righe qua sotto testeranno la tua soluzione al problema. Se verrà visualizzato un errore la tua soluzione potrebbe essere incorretta o incompleta.
assert isPalindrome("Ab ./B a") == True, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
assert isPalindrome("Hackademy") == False, "Valore restituito non corretto. Se vedi un NameError, vuol dire che la variabile o la funzione non è stata creata o é stato dato il nome sbagliato."
print("Esercizio 30 Corretto")
