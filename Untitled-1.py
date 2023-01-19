a=input("")
try:
    b=int(a)
except ValueError:
    print("zehmet omasa reqem daxil edin")
    exit()
except Exception:
    print("bilinmeyen error bas verdi")
    exit()