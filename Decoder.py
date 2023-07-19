def decoder(string):
    decoded_password = ''
    for i in string:
        digit = str(int(i) - 3)
        decoded_password += digit
    return decoded_password


print(decoder('45678888'))
