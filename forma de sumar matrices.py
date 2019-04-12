class suma_matriz(object):
    def __init__(self):
        pass
    #funcion de validacion


    def suma(m,f,r):
        if f==lne(m):
            return r
        else: return sfila(m[f],0,r)

    def sfila(fila,c,r):
        if c==len(fila):
            return r
        else: return sfila(fila,c+1,r+fila[c])


    #####opcion 2
    ###funcion de validacion

    def sumam(m,f,c,resultado):
        if f==len(m):
            return resultado
        elif c==len(m[0]):
            return self.sumam(m,f+1,0,resultado)
        else: return self.sumam(m,f,c+1,resultado+m[f][c])
