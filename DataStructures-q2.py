name=input("Input the Filename: ")
l=name.split('.')
if l[1]=='py':
    print("The extension of the file is: 'python'")
else:
    print("The extension of the file is: ",l[1])
