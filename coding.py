passFile = open("SecretPass.txt")
secretPass =passFile.read()
print("Enter password: ")
typedPass = input()
if typedPass == secretPass:
    print('Access granted')
else:
    print('Access denied')