def encoder(string):
    encoded_password = ''
    for i in string:
        digit = str(int(i) + 3)
        encoded_password += digit
    return encoded_password

#Anton's decoder
def decoder(encrypted):
    decrypt = []                        #initializes array
    for element in encrypted:
        element = int(element) - 3      #adds 3 to each iterated item
        decrypt.append(element)         #adds to list
    decrypt = int(''.join(str(digit) for digit in decrypt))  #converts list to integer
    return decrypt      #returns string

def main():
    encoding = True
    while encoding:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encoder(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            print(f'The encoded password is {encoded_password},', end=' ')
            print(f'and the original password is {decoder(encoded_password)}.\n')
        elif option == 3:
            encoding = False
        else:
            print('Invalid option.\n')


if __name__ == '__main__':
    main()
