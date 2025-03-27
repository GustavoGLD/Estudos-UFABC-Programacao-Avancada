def binary_couting(n):
    """
    Função que retorna a contagem binária de n bits.
    """
    binary = [bin(i)[2:].zfill(n) for i in range(2**n)]
    return binary

def make_permutations(l: list[int]):
    binaries = binary_couting(len(l))
    permutations = []
    for binary in binaries:
        permutation = []
        for index, bit in enumerate(binary):
            if bit == '1':
                permutation.append(l[index])

        #print(permutation)
        permutations.append(permutation)

    return permutations

if __name__ == "__main__":
    l = [1, 2, 3, 4]
    permutations = make_permutations(l)
    assert len(permutations) == 2**len(l)
    print(permutations)
