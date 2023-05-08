import numpy as np
 
# Given values
M = 2036764117802210446778721319780021357
W = 127552671440279916013021

def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return (gcd, y, x - (a // b) * y)

_, W_inv, _ = extended_gcd(W, M)

# print("W Inverse using extended gcd is -------> {}".format(W_inv))

# print("W Inverse using normal python ----> {} ".format(pow(W,-1,M)))

# print(W_inv)


# Using readlines() to read the cipher text from the txt file
file1 = open('cipher.txt', 'r')
cryptLines = file1.readlines()

cipherCount = 0

# empty list
s_list = []

for cipher in cryptLines:
    cipher = cipher.rstrip("\n")
    cipher = int(cipher)
    s_list.append((cipher * W_inv) % M)
    # cipherCount += cipher
    

# print("S list is -------> {} ".format(s_list))
# print("The count of the cipher is ------> {}".format(cipherCount))

# The value of s can be obtained through the formula below
# s = (W_inv * cipherCount) % M
# print("The value of s is ------> {}".format(s))

# Using readlines() to read the cipher text from the txt file
file2 = open('knapsack.txt', 'r')
knapsackLines = file2.readlines()

# empty list
private_list = []

for line in knapsackLines:
    line = line.rstrip("\n")

# Step 1: Calculate modular inverse of W modulo M
    # print(line)
    line = int(line)
    
    private_key = (W_inv * line) % M

    # Step 2: Calculate coefficients of superincreasing knapsack
    # private_key = [(W_inv * w_i) % M for w_i in public_key]

    private_list.append(private_key)

sorted_private_list = sorted(private_list)
# print("Sorted Private key:", sorted_private_list)


pi = []
for i in private_list:
    for j in range(len(sorted_private_list)):
        if (i == sorted_private_list[j]):
            pi.append(j)

# print("Permuted Array : {}".format(pi))

# empty list
final_list = []

for s in s_list:
    init_list = []
    for knapsackVal in reversed(sorted_private_list):
        if s >= knapsackVal:
            init_list.append(1)
            s = s - knapsackVal
        else:
            init_list.append(0)
    final_list.append(init_list)

# print("Binary Vals before the arrangement --------> {}".format(final_list))

# final_list.reverse()

chck_list = []

# print("Final list",final_list)

# final_list = final_list[::-1]



for ele in final_list:
    # print("ELE -----> {}".format(ele))
    # joinedBin = ''.join(str(bit) for bit in ele)
    # print("Joined bin -------> {}".format(joinedBin))
    ele = ele[::-1]
    # print("Reversed Bin ------> {}".format(joinedBin))
    chck_list.append(ele)



# Arranging the binary vals positions based on pi
# print("Checklist", chck_list)
binary_list = []
for x in chck_list:
    init1_list = []
    for bin in pi:
        # print("Pi value:", bin)
        init1_list.append(x[bin])
    binary_list.append(init1_list)


# print("Binary Vals after the arrangement --------> {}".format(binary_list))
# print("23 Position : {}".format(binary_list))


# # Making sure there's 14 digits for binary
# for bin in final_list:
#     print("Binary length ----> {}".format(len(bin)))

# Reversing the list

decimal_list = []
for binary in binary_list:
    # decimal = int(''.join(str(bit) for bit in binary), 2)
    # print("Binary val ----> {}".format(binary))
    # for ele in final_list:
    # print("ELE -----> {}".format(ele))
    # joinedBin = ''.join(str(bit) for bit in ele)
    # print("Joined bin -------> {}".format(joinedBin))
    # joinedBin = ''.join(str(chck) for chck in binary)
    joinedBin = ''.join(format(num, 'b') for num in binary)

    # my_list = [1, 2, 3, 4, 5]
    # concatenated = ''.join(map(str, binary))
    # print(concatenated)

    decimal = int(str(joinedBin),2)

    if(len(str(decimal)) < 14):
        # print("Here")
        # decimal = str(decimal)
        l = 14 - len(str(decimal))
        # print("Before appending 0 : {}".format(decimal))
        decimal = "0" + str(decimal)
        while(len(str(decimal)) < 14):
            decimal = "0" + str(decimal)
        # decimal = int(decimal)
        # print("After appending 0 : {}".format(decimal))
    else:
        decimal = str(decimal)
    decimal_list.append(decimal)

# print(decimal_list)


alphabet_matrix = [
    [' ', '*', '4', '>', 'H', 'R', '\\', 'f', 'o', '0'],
    ['!', '+', '5', '?', 'I', 'S', ']', 'g', 'p', 'y'],
    ['"', ',', '6', '@', 'J', 'T', '^', 'h', 'q', 'z'],
    ['#', '-', '7', 'A', 'K', 'U', '_', 'i', 'r', '{'],
    ['$', '.', '8', 'B', 'L', 'V', '`', 'j', 's', '|'],
    ['%', '/', '9', 'C', 'M', 'W', 'a', 'k', 't', '}'],
    ['&', '0', ':', 'D', 'N', 'X', 'b', 'l', 'u', '~'],
    ['\'', '1', ';', 'E', 'O', 'Y', 'c', 'm', 'v', '0'],
    ['(', '2', '<', 'F', 'P', 'Z', 'd', 'n', 'w', '\n'],
    [')', '3', '=', 'G', 'Q', '[', 'e', '0', 'x', '\r']
]

for plain in decimal_list:
    check = [str(plain)[i:i+2] for i in range(0,len(str(plain)),2)]
    # print("CHECK --------> {}".format(check))
    for val in check:
        # print(val[0])
        # print(val[1])
        arrangement = alphabet_matrix[int(val[0])][int(val[1])]
        print(arrangement,end = "")









