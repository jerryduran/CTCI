

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    myList1 = []
    myList2 = []
    for i in range(0, len(str1)):
        myList1.append(str1[i])
        myList2.append(str2[i])
    myList1.sort()
    myList2.sort()

    if myList1 == myList2:
        return True
    return False

word1 = "ass"
word3 = "ssa"
print(is_permutation(word1, word3))
