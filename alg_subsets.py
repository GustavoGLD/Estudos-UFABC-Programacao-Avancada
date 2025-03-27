def binary_couting(n):
    """
    Função que retorna a contagem binária de n bits.
    """
    binary = [bin(i)[2:].zfill(n) for i in range(2**n)]
    return binary

def make_subsets(l: list[int]):
    binaries = binary_couting(len(l))
    subsets = []
    for binary in binaries:
        subset = []
        for index, bit in enumerate(binary):
            if bit == '1':
                subset.append(l[index])

        subsets.append(subset)

    return subsets

if __name__ == "__main__":
    l = [1, 2, 3, 4]
    subsets = make_subsets(l)
    assert len(subsets) == 2**len(l)
    print(subsets)
