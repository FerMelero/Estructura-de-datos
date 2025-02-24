import time
import random

def insertion_sort_time(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    execution_time = round((end_time - start_time) * 1000, 2)  # Convertir a milisegundos
    return arr, execution_time  

# Ejemplo 1: Lista pequeña y casi ordenada
arr1 = [1, 2, 4, 3, 5, 6]  
sorted_arr1, time1 = insertion_sort_time(arr1)  
print(f"Lista ordenada: {sorted_arr1}, Tiempo de ejecución: {time1} ms")

# Ejemplo 2: Lista grande y desordenada
arr2 = random.sample(range(1, 10000), 1000)  # Lista de 1000 números aleatorios
sorted_arr2, time2 = insertion_sort_time(arr2)  
print(f"Lista ordenada (primeros 10 elementos): {sorted_arr2[:10]}, Tiempo de ejecución: {time2} ms")

print("---------------------")
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover los elementos de arr[0..i-1] que son mayores que key, una posición hacia adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Iteración {i}: {arr}")

# Ejemplo de uso
arr = [5, 3, 8, 1, 2]
insertion_sort(arr)
arr=[5,4,3,4,1]
insertion_sort(arr)

