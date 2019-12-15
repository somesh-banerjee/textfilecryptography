i = int(input("Type 1 to encode file and 2 to decode file: "))
if i == 1:
    import encode
elif i == 2:
    import decode
else:
    exit()
