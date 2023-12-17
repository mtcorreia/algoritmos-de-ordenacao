import random as ran
from bubblesort import bubble_sort

any_numbers = ran.sample(range(1, 1000), 10) # Teste com 10 números aleatórios entre 1 a 1000.
already_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Teste com números já ordenados.
inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63] # Teste com números decrescentes.
repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 5, 4, 5, 7, 1] # Teste com números repetidos.
negative = [-2, -3, -6, -1, 0, 2, 5, 8, 10] # Teste com números negativos e positivos.

if __name__ == "__main__":

    lista_any = any_numbers
    lista_already = already_sorted
    lista_inversed = inversed
    lista_repeated = repeated
    lista_negative = negative

    print("\n=== LISTAS DESORDENADAS ===") 

    print("\nLista Desordenada (any_numbers):", lista_any)
    print("Lista Desordenada (already_sort):", lista_already)
    print("Lista Desordenada (inversed):", lista_inversed)
    print("Lista Desordenada (lista_repeated):", lista_repeated)
    print("Lista Desordenada (negative):", lista_negative)


    # BUBBLE SORT  
    print("\n=== BUBBLE SORT ===") 
    bubble_sort(lista_any)
    bubble_sort(lista_already)
    bubble_sort(lista_inversed)
    bubble_sort(lista_repeated)
    bubble_sort(lista_negative)

    print("\nLista Ordenada (any_numbers):", lista_any)
    print("Lista Ordenada (already_sort):", lista_already)
    print("Lista Ordenada (inversed):", lista_inversed)
    print("Lista Ordenada (lista_repeated):", lista_repeated)
    print("Lista Ordenada (negative):", lista_negative)