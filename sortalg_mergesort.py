def quicksort(numbers: list[int]) -> list[int]:
    if len(numbers) == 0:
        return []

    pivot = numbers[0]
    bigger = quicksort(list(filter(lambda n: n > pivot, numbers)))
    smaller = quicksort(list(filter(lambda n: n < pivot, numbers)))

    return smaller + [pivot] + bigger

if __name__ == '__main__':
    a = [5, 1, 3, 7, 2, 6, 8, 10, 4, 9]
    print(f'{a} -> {quicksort(a)}')
