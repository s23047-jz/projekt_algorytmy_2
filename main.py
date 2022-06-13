from collections import Counter


def count_letters():
    letters_count_array = []
    with open("text_file.txt", 'r') as f:
        text = f.read()
        letter_counts = Counter(text)
        for letter, count in letter_counts.most_common():
            letters_count_array.append((letter, count))
        return letters_count_array


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def huffman_code(letters_count_array):
    for i in range(len(letters_count_array)):
        letters_count_array[i] = (letters_count_array[i], i)
        print(letters_count_array[i])


def merge_items(arr):
    while len(arr)-1 != 1:
        arr.append(arr.pop(0) + arr.pop(1))


def main():
    count_array = count_letters()
    print(count_array)
    heap_array = heap_sort(count_array)
    print(heap_array)

main()
