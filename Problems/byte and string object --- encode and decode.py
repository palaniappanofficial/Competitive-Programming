string_a="Hello Palaniappan"
string_b=b"Hello Palaniappan"
encodedresult=string_a.encode('ASCII')
if encodedresult==string_b:
    print("Encoded Successfully")
    print("Encoded value is",encodedresult)
else:
    print("Not Encoded")

decodedresult=string_b.decode("ASCII")
if string_a==decodedresult:
    print("Decoded Successfully")
    print("Decoded Value is",decodedresult)
else:
    print("Not Decoded")