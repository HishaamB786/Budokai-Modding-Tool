#Budokai 1 Importer (B1I)
#Purpose of this sub-program - To export any Non-Budokai 1 model into Budokai 1
#Editing the shader number, model part number and general data


def main():
    y = input("Insert file: ")
    f = open(y, "r+b")
    chunk = f.read(16)
    offsets = []
    counter = 0
    while chunk != b"":
        if chunk[0] == 0xB5 and chunk[1] == 0x01:
            offsets.append(((f.tell()-16)))
            #print(hex(f.tell()-16))
            counter += 1
        chunk = f.read(16)
    for i in offsets:
        f.seek(i+0)
        f.write(b"\x35")
        f.seek(i+1)
        f.write(b"\x62")
        f.seek(i+4)
        f.write(b"\x35")
        f.seek(i+5)
        f.write(b"\x62")
        f.seek(i+12)
        f.write(b"\xFF")
        f.seek(i+13)
        f.write(b"\xFF")
        f.seek(i+14)
        f.write(b"\xFF")
        f.seek(i+15)
        f.write(b"\xFF")
        f.seek(i+32)
        f.write(b"\xCD")
        f.seek(i+33)
        f.write(b"\xCC")
        f.seek(i+34)
        f.write(b"\x4C")
        f.seek(i+35)
        f.write(b"\x3f")
        f.seek(i+36)
        f.write(b"\xCD")
        f.seek(i+37)
        f.write(b"\xCC")
        f.seek(i+38)
        f.write(b"\x4C")
        f.seek(i+39)
        f.write(b"\x3f")
        f.seek(i+40)
        f.write(b"\x66")
        f.seek(i+41)
        f.write(b"\x66")
        f.seek(i+42)
        f.write(b"\x66")
        f.seek(i+43)
        f.write(b"\x3f")
        f.seek(i+44)
        f.write(b"\x00")
        f.seek(i+45)
        f.write(b"\x00")
        f.seek(i+46)
        f.write(b"\x80")
        f.seek(i+47)
        f.write(b"\x3f")
        f.seek(i+48)
        f.write(b"\x00")
        f.seek(i+49)
        f.write(b"\x00")
        f.seek(i+50)
        f.write(b"\x00")
        f.seek(i+51)
        f.write(b"\x43")
        f.seek(i+52)
        f.write(b"\x00")
        f.seek(i+53)
        f.write(b"\x00")
        f.seek(i+54)
        f.write(b"\x00")
        f.seek(i+55)
        f.write(b"\x43")
        f.seek(i+56)
        f.write(b"\x00")
        f.seek(i+57)
        f.write(b"\x00")
        f.seek(i+58)
        f.write(b"\x00")
        f.seek(i+59)
        f.write(b"\x43")
        f.seek(i+60)
        f.write(b"\x00")
        f.seek(i+61)
        f.write(b"\x00")
        f.seek(i+62)
        f.write(b"\x00")
        f.seek(i+63)
        f.write(b"\x43")

    print(str(counter) + " model parts of Budokai 3 model converted to Budokai 1")
    print("")
    f.close()

def again():
    yn = input("Load another? (Y/N)")
    yn = yn.lower()
    yn = yn[0:1]
    if yn == "y":
        main()
        again()
    else:
        kill = input("press enter to close")

main()
again()
exit()

