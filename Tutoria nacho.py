def mover(Matriz,Fila,Columna,Result,Paso):
    if Paso==3 and Fila==len(Matriz)-1 and Columna==len(Matriz)-1:
        return Result+[Matriz[Fila][Columna]]
    elif Paso==3:
        if Matriz[Fila][Columna]<0:
            return mover(Matriz,Fila+1,Columna+1,Result+[Matriz[Fila][Columna]],Paso)
        else:
            return mover(Matriz,Fila+1,Columna+1,Result,Paso)
    elif Paso==2:
        if Fila==0 and Columna==0:
            Paso+=1
        if Matriz[Fila][Col]<0:
            return mover(Matriz,Fila,Columna-1,Result+Matriz[Fila][Columna],Paso)
        else:
            return mover(Matriz,Fila,Columna-1,Result,Paso)
    
