import random
import numpy as np
import math

# print(random.sample(range(1, 18), 4))
# 8 17 16 3
# selection sort, bitonic sort, most significant digit, comp sort

# Исходные данные:
arr1 = []
for i in range(1000):
	arr1.append(random.randint(0, 999999))

arr2 = []
for i in range(99999):
	arr2.append(random.uniform(-1, 1))

arr3 = []
r = 31/10
for i in range(42000):
	x = random.uniform(-r, r)
	y = random.uniform(-(r**2-x**2)**0.5, (r**2-x**2)**0.5)
	arr3.append([x, y])

arr4 = []
file = open("text.txt", 'r', encoding="Windows-1251")
for line in file:
	for word in line.split(' '):
		if (word != '' and word != '\n' and word != '-'):
			arr4.append(word.replace('n', ''))



def selection_sort(array):
	i = 0
	length = len(array)
	while i < length-1:
		min_i = i
		for j in range(i+1, length):
			if array[j] < array[min_i]:
				min_i = j
		array[i], array[min_i] = array[min_i], array[i]
		i += 1
selection_sort(arr1)
# Отсортировано



def c_swap(array, a, b, inverted):
	size = b - a
	step = int(size / 2)
	if not inverted:
		for i in range(a, math.floor(a + size / 2)):
			if (array[i]) <= (array[i + step]):
				pass
			else:
				array[i], array[i + step] = array[i + step], array[i]
	else:
		for i in range(a, math.floor(a + size / 2)):
			if (array[i]) >= (array[i + step]):
				pass
			else:
				array[i], array[i + step] = array[i + step], array[i]
	if size > 2:
		c_swap(array, a, a + step, inverted)
		c_swap(array, a+step, b, inverted)

def subfunction(array, limit_size, inverted):
	if len(array) == limit_size:
		c_swap(array, 0, limit_size, inverted)	
	else:
		middle = int(len(array)/2)
		left = array[:middle]
		right = array[middle:]
		subfunction(left, limit_size, False)
		subfunction(right, limit_size, True)
		array = np.concatenate([left, right])

def bitonic_sort(array): 
	step = 2
	limit = len(array)+1
	while(step < limit):
		subfunction(array, step, False)
		step *= 2
	inf_len = 0
	last_symbol = len(array)-1
	while array[last_symbol] == math.inf:
		inf_len += 1
		last_symbol -= 1
	print(last_symbol)
	array = array[:last_symbol+1]
	return array

extension_length = 2**math.ceil(math.log2(len(arr2))) - len(arr2)
arr2_extension = np.full((extension_length), math.inf)
arr2 = np.concatenate([arr2, arr2_extension])

arr2 = bitonic_sort(arr2)
# Отсортировано