try:
    r = open(r"D:\OneDrive\Documents\Python_15032019\F\File.txt", "w")
    r.write(" LALALALALALALAALALALA ")
except IOError:
    print("Can't write")
else:
    print("PROGRAM COMPLETE BABY")

r.close()
