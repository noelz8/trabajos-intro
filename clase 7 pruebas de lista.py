Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> lista= (1,2,3,4,5)
>>> suma(lista)
'Error: el valor ingreado no esa lista'
>>> suma(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    suma(1,2,3,4,5)
TypeError: suma() takes 1 positional argument but 5 were given
>>> suma(lista)
'Error: el valor ingreado no esa lista'
>>> suma(1)
'Error: el valor ingreado no esa lista'
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> suma(lista= (1,2,3,4,5))
'Error: el valor ingreado no es una lista'
>>> suma lista= (1,2,3,4,5)
SyntaxError: invalid syntax
>>> suma (1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    suma (1,2,3,4,5)
TypeError: suma() takes 1 positional argument but 5 were given
>>> lista= [1,2,3,4,5]
>>> suma(lista)
15
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> par_lista([2,10,3,7,6])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    par_lista([2,10,3,7,6])
  File "E:/Noel/clase 7 lista suma proga.py", line 30, in par_lista
    return par_lista_aux(lista)
  File "E:/Noel/clase 7 lista suma proga.py", line 36, in par_lista_aux
    if (lista %10)%2==0:
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> lista[2,10,3,7,6]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lista[2,10,3,7,6]
NameError: name 'lista' is not defined
>>> lista=[2,10,3,7,6]
>>> par_lista(lista)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    par_lista(lista)
  File "E:/Noel/clase 7 lista suma proga.py", line 30, in par_lista
    return par_lista_aux(lista)
  File "E:/Noel/clase 7 lista suma proga.py", line 36, in par_lista_aux
    if (lista %10)%2==0:
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> par_lista(lista)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    par_lista(lista)
NameError: name 'lista' is not defined
>>> par_lista([2,10,3,7,6])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    par_lista([2,10,3,7,6])
  File "E:/Noel/clase 7 lista suma proga.py", line 30, in par_lista
    return par_lista_aux(lista)
  File "E:/Noel/clase 7 lista suma proga.py", line 37, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 37, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 39, in par_lista_aux
    return par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 39, in par_lista_aux
    return par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 37, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 36, in par_lista_aux
    if (lista[0]%2==0):
IndexError: list index out of range
>>> par_lista([2,10,3,7,6])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    par_lista([2,10,3,7,6])
  File "E:/Noel/clase 7 lista suma proga.py", line 30, in par_lista
    return par_lista_aux(lista)
  File "E:/Noel/clase 7 lista suma proga.py", line 37, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 37, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 39, in par_lista_aux
    return par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 39, in par_lista_aux
    return par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 37, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 36, in par_lista_aux
    if (lista[0]%2==0):
IndexError: list index out of range
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> par_lista([2,10,3,7,6])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    par_lista([2,10,3,7,6])
  File "E:/Noel/clase 7 lista suma proga.py", line 29, in par_lista
    return par_lista_aux(lista)
  File "E:/Noel/clase 7 lista suma proga.py", line 36, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 36, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 38, in par_lista_aux
    return par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 38, in par_lista_aux
    return par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 36, in par_lista_aux
    return lista[0]+par_lista_aux(lista[1:])
  File "E:/Noel/clase 7 lista suma proga.py", line 35, in par_lista_aux
    if (lista[0]%2==0):
IndexError: list index out of range
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> par_lista([2,10,3,7,6])
18
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> cero_lista ([0,12,53,10)
		
SyntaxError: invalid syntax
>>> cero_lista ([0,12,53,10])
		
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> cero_lista ([0,12,53,10])
		
'true'
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> cero_lista ([0,12,53,10])
		
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    cero_lista ([0,12,53,10])
  File "E:/Noel/clase 7 lista suma proga.py", line 57, in cero_lista
    return cero_lista_aux(lista)
  File "E:/Noel/clase 7 lista suma proga.py", line 64, in cero_lista_aux
    return "true" + 0
TypeError: must be str, not int
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> cero_lista ([0,12,53,10])
		
'true'
>>> cero_lista ([12,53,10])
		
'false'
>>> cero_lista ([12,53,10, 0])
		
'false'
>>> 
================ RESTART: E:/Noel/clase 7 lista suma proga.py ================
>>> cero_lista ([12,53,10, 0])
		
True
>>> cero_lista ([12,53,10])
		
False
>>> 
