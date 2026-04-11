import time
import tracemalloc
import random

#Проверка наличия элемента в массиве
def Find_item(massiv,target ):
    for i in massiv:
        if i == target:
            return True
    return False

#Поиск второго максимального элемента
def Find_max(massiv):
    max_1 = max_2 = massiv[0]
    if len(massiv)==1:
        return massiv[0]
    if len(massiv)>2:
        for i in massiv:
            if i>max_1:
                max_2 = max_1
                max_1 = i
        return max_2
    return max(massiv[0], massiv[1])

#Бинарный поиск
def Binary_find(massiv, target):
    sorted_massiv = sorted(massiv)
    left,right = 0, len(sorted_massiv)-1
    while left <= right:
        mid = (left + right)//2
        if target > sorted_massiv[mid]:
            left = mid + 1
        elif target < sorted_massiv[mid]:
            right = mid - 1
        else:
            return True
    return False

#Построение таблицы умножения
def Table_proizv(n):
    table=[]
    for i in range(1,n+1):
        proizv =[]
        for j in range(1,n+1):
            proizv.append(i*j)
        table.append(proizv)
    return table
#for i in Table_proizv(3):
#    print(i)

#Сортировка выбором
def Selection_sort(massiv):
    massiv = massiv.copy()
    n = len(massiv)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if massiv[j] < massiv[min_index]:
                min_index = j
        massiv[i], massiv[min_index] = massiv[min_index], massiv[i] 
    return massiv

#Функция измерения времени
def Delta_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start

#Функция измерения времени и памяти
def Delta_time_and_space(func, *args):
    tracemalloc.start()
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end - start, peak / 1024 
   
#Функция генерации данных
def Generate_massiva(n):
    massiv = []
    for i in range(n):
        massiv.append(random.randint(0, 10000))
    return massiv

sizes = [10, 100, 1000, 10000]
print("1. Проверка наличия элемента в массиве")
for size in sizes:
    test_massiv = Generate_massiva(size)
    execution_time = Delta_time(Find_item, test_massiv, -1)
    print(f"Размер {size}: {execution_time:.8f} сек")

print("2. Поиск второго максимального элемента")
for size in sizes:
    test_massiv = Generate_massiva(size)
    execution_time = Delta_time(Find_max, test_massiv)
    print(f"Размер {size}: {execution_time:.8f} сек")

print("3. Бинарный поиск")
for size in sizes:
    test_massiv = Generate_massiva(size)
    test_massiv.sort()  
    execution_time = Delta_time(Binary_find, test_massiv, test_massiv[0])
    print(f"Размер {size}: {execution_time:.8f} сек")

sizes_table = [10, 50, 100]
print("4. Построение таблицы умножения")
for size in sizes_table:
    execution_time = Delta_time(Table_proizv, size)
    print(f"Размер {size}: {execution_time:.8f} сек")

print("5. Сортировка выбором")
for size in sizes:
    test_massiv = Generate_massiva(size)
    execution_time, memory_kb = Delta_time_and_space(Selection_sort, test_massiv)
    print(f"Размер {size}: {execution_time:.8f} сек, память: {memory_kb:.2f} КБ")


