def cipher(text):
    arr=[]
    arr1=[]
    cipher=""
    plain=""
    new=0
    var=0
    alphabet=""
    countval=0
    chars=""
    values=0
    index=0
    arr[:]=text
    var=int(input("Enter the Key:"))
    for i in range(0,len(arr)):
        chars=arr[i].upper()
        values=ord(chars)%65
        new=(values+var)%26
        arr1.append(new)
        cipher=cipher+chr(new+65)
        alphabet=new+65
        #alphabet=ord(chr(alphabet))
        countval=(alphabet%65)
        index=(countval-var)%26
        plain=plain+chr(index+65)
    print("Cipher Text is:"+cipher)
    print("Plain Text is:"+plain)
text=input("Enter the Plain Text:")
cipher(text)
