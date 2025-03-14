def selection_sort(numbers: list[int]) -> list[int]:
  ordened_list = []
  while numbers:
    min = float('inf')
    for n in numbers:
      if n < min:
        min = n

    ordened_list.append(min)
    numbers.remove(min)
  return ordened_list


if __name__ == '__main__':
  a = [9, 1, 3, 7, 2, 6, 8, 10, 4, 5]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  assert selection_sort(a) == b, f"{selection_sort(a)=}, {b=}"
