class ListaEnlazada:
    #Construye Lista vacia
    def __init__(self):
        self._head=None
        self._size=0
    #Regresa el nùmero de elementos en la lista
    def __len__(self):
            return self.__size
        #determinar si un item se encuentra en la lista
    def contains(self,target):
        curNode=self.__head
        while curNode is not None and curNode.item !=target:
            curNode is not None:
                return True
            else: return False
    #agregar un nuevo item a la lista
    def add(self,item):
        newNode=Node(item)
        newNode.next=self._head
        self.__head=newNode
        self.__size +=1
    #Borrar un item de la lista
    def remove(self,item):
        predNone=None
        curNode=self.__head
        while curNode is not None and curNode.item !=item:
            predNode= curNode
            curNode=curNode.next
        assert curdNode is not None,"El item debe encontrarse en la lista"
        #Quitar el enlace del nodo y regresar el item
        self.__size -=1
        if curNode is self.__head:
            self.__head=curNode.next
        else:
            predNone.next=curNode.next
        return curNode.item
    def test(self):
        self.add(1)
        self.add(5)
        self.add(6)
        iter= Iterator(self._head)
        while iter.next()==True:
            print("Elemento: ",iter.getNext())
class Node:
    def __init__(self,item):
        self.item=item
        self.next= None
class Iterator:
    def __init__(self,listHead):
        self._curNode=listHead
    def __iter__(self):
        return self
    def next(self):
        if self._curNode is None:
            return False
        else: return True
    def getNext(self):
        if self._curNode is None:
            return None
        else:
            item=self._curNode.item
            self._curNode=self._curNode.next
            return item
    
        
