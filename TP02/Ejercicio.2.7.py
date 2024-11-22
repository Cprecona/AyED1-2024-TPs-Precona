from typing import List

def intercalar_lista(l1:List[int],l2:List[int]) -> None:
    '''Intercalar los elementos de una lista entre los elementos de otra. La intercalación
    deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
    una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
    y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
    tener distintas longitudes.

    '''
    
    for i in range (len(l1)):
        l1[i*2+1:i*2+1] = [l2[i]]
    print(l1)

lista1=[8,1,3]
lista2=[5,9,7]

intercalar_lista(lista1,lista2)
