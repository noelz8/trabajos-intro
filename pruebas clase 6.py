Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> n=5
>>> i=0
>>> i+3
3
>>> i=1
>>> i+3
4
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> sumatoria (5,0)
33
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> sumatoria2 (5)
33
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
7 7 7 7 7 7 7 7 35
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
7 7 7 7 7 7 7 7 56
>>> 0+1
1
>>> 1+1
2
>>> 1+2
3
>>> 2+3
5
>>> 3+5
8
>>> 5+8
13
>>> 8+13
21
>>> 13+21
34
>>> 21+34
55
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> 21+34
55
>>> secuencia (7,1)
7 56
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    secuencia (7,1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + i)+ secuencia(n, i+1-1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + i)+ secuencia(n, i+1-1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + i)+ secuencia(n, i+1-1)
  [Previous line repeated 989 more times]
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 47, in secuencia
    if(i>n):
RecursionError: maximum recursion depth exceeded in comparison
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    secuencia (7,1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + i)+ secuencia(n, i+0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + i)+ secuencia(n, i+0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + i)+ secuencia(n, i+0)
  [Previous line repeated 989 more times]
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 47, in secuencia
    if(i>n):
RecursionError: maximum recursion depth exceeded in comparison
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
7 56
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
7 49
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
6 56
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (7,1)
 56
>>> secuencia (7,0)
 56
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (,0)
SyntaxError: invalid syntax
>>> secuencia (5,0)
 20
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (5,0)
 30
>>> secuencia (8,0)
 72
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 45
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    secuencia (8,0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n, i+0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n, i+0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n, i+0)
  [Previous line repeated 989 more times]
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 47, in secuencia
    if(i>n):
RecursionError: maximum recursion depth exceeded in comparison
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 15
>>> secuencia (8,0)
 15
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    secuencia (8,0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n+1, i+1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n+1, i+1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n+1, i+1)
  [Previous line repeated 989 more times]
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 47, in secuencia
    if(i>n):
RecursionError: maximum recursion depth exceeded in comparison
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    secuencia (8,0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n, i+1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n, i+1)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i + 1)+ secuencia(n, i+1)
  [Previous line repeated 5 more times]
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 48, in secuencia
    print( end=" "-1)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 46
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 73
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 4
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 362880
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 37
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 19
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 28
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> 
>>> secuencia (8,0)
 37
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 21
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 262
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 82
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 64
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 64
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    secuencia (8,0)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i +n- i-1)+secuencia(n, i)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i +n- i-1)+secuencia(n, i)
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 50, in secuencia
    else: return (i +n- i-1)+secuencia(n, i)
  [Previous line repeated 989 more times]
  File "C:\Users\user\Desktop\clase 6 intro y taller.py", line 47, in secuencia
    if(i>n):
RecursionError: maximum recursion depth exceeded in comparison
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 -8
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> secuencia (8,0)
 28
>>> 
========== RESTART: C:\Users\user\Desktop\clase 6 intro y taller.py ==========
>>> fib(8)
34
>>> x=[3,4,5,6,7,1]
>>> x[0]
3
>>> x=
