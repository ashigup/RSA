
#encryption code
def main():
    keys = []                                       #list to store text from key_generator.txt
    with open("key_generator.txt", 'r') as file:
        for line in file:
            for a in line.split():                  #split text by space
                #print(a)
                keys.append(a)                      #add text to keys list
    n = int(keys[2])                                #declare n
    e = int(keys[4])                                #declare e
    #print(n)
    #print(e)
    encrypted_mess = open("encryptedText.txt", 'w')     #create encryptedText.txt
    with open("plainText.txt") as newFile:
        for word in newFile:
            for char in word:
                print(encryption(ord(char),e,n),file=encrypted_mess)    #encrypt by char and write to file
    print(n, file=encrypted_mess)                              #print n and e
    print(keys[4], file=encrypted_mess)

#encyrption funciton. m^e % n
def encryption(m,e,n):
    x = pow(m,e,n)
    return x

main()