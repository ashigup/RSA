#RSA Decrypter : Ashish Kumar


from __future__ import print_function

def main():

    keys = []  # list to store text from key_generator.txt
    with open("key_generator.txt", 'r') as file:
        for line in file:
            for a in line.split():  # split text by space
                #print(a)
                keys.append(a)  # add text to keys list
    keysLength = len(keys)
    d = keys[10]

    arr = []
    with open("encryptedText.txt", 'r') as file:
        for line in file:
            arr.append(int(line))
    l = len(arr)
    n = arr[l-2]
    e = arr[l-1]

    i = 0
    decrypted_Mess = open("decryptText.txt", 'w')
    #with open("decryptText.txt") as newFile will bw generated:
    while i < l -2:
        x = decrypt(arr[i], int(d), int(n))
        y = chr(x)
        #print(chr(x).encode('utf-8'), file=decrypted_Mess)
        print(y, end="", file=decrypted_Mess)
        i+=1


def decrypt(c,d,n):
    x = pow(c,d,n)
    return x


main()
