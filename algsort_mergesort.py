def making_pairs(vector: list[list[int]]) -> list[tuple[list[int], list[int]]]:
    pairs = []
    for index in range(0, len(vector), 2):
        if index+1 >= len(vector):
            pairs.append((vector[index], []))
        else:
            pairs.append((vector[index], vector[index+1]))
    return pairs


def test_making_pairs():
    assert making_pairs([[1, 2], [3, 4], [5, 6], [7, 8]]) == [([1, 2], [3, 4]), ([5, 6], [7, 8])]
    assert making_pairs([[1, 2], [3, 4], [5, 6]]) == [([1, 2], [3, 4]), ([5, 6], [])]


def merge(vector_left: list[int], vector_right: list[int]) -> list[int]:
    merged_list = []
    while vector_left or vector_right:
        if not vector_left:
            merged_list.append(vector_right.pop(0))
        elif not vector_right:
            merged_list.append(vector_left.pop(0))
        elif vector_left[0] >= vector_right[0]:
            merged_list.append(vector_right.pop(0))
        elif vector_right[0] >= vector_left[0]:
            merged_list.append(vector_left.pop(0))

    return merged_list


def test_merge():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
    assert merge([1, 3], [2, 4, 6]) == [1, 2, 3, 4, 6]


def mergesort(vector: list[int]) -> list[int]:
    splited_vector = [[element] for element in vector]
    while len(splited_vector) > 1:
        temp_splited_vector = []
        for left_vector, right_vector in making_pairs(splited_vector):
            temp_splited_vector.append(merge(left_vector, right_vector))
        splited_vector = temp_splited_vector
    return splited_vector[0]


def test_mergesort():
    assert mergesort([3, 1, 5, 2, 4]) == [1, 2, 3, 4, 5]
    assert mergesort([2, 1, 3, 5, 7, 4, 3]) == [1, 2, 3, 3, 4, 5, 7]


if __name__ == "__main__":
    test_making_pairs()
    test_merge()
    test_mergesort()
    #input_vector = [int(element) for element in input().split()]
    #output_vector = mergesort(input_vector)
    print(*output_vector, sep=" ")

