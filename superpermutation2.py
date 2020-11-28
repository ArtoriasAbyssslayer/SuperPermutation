#another implementation 
import itertools
import time

def superpermutation(n):
    final_result = ""
    if n == 1:
        final_result = "A"
        return final_result
    else:
        prev = superpermutation(n - 1)
        p_list = find_permutations(prev, (n - 1))
        for it in p_list:
            final_result = final_result + it + str(chr(n+64)) + it
            x = int(len(final_result)) - 2*int(len(it)) - 1
            initial = final_result[x]
            if x != 0:
                i = x - 1
                while final_result[i] != initial and final_result[i] != str(chr(n+64)):
                    final_result = final_result[:i] + final_result[i + 1:]
                    i = i - 1
                if final_result[i] == initial:
                    final_result = final_result[:i] + final_result[i + 1:]
        return final_result


# Correct
def find_permutations(super_perm, size):
    list1 = []
    a = ''
    b = 0
    for x in range(0, int(len(super_perm)) - size + 1):
        for y in range(x, x + size):
            a = a + super_perm[y]
            b = b + ord(super_perm[y]) - 64
        if b == size * (size + 1) / 2:
            list1.append(a)
        a = ''
        b = 0
    return list1


n = -1
while n <= 0:
    n = int(input("Type a positive integer: "))
start = time.clock()
superperm = superpermutation(n)
end = time.clock()
print("The superpermutation is: " + superperm)
print("Length of the superpermutation:" , len(superperm))
print("Execution time:", end - start, "s")
