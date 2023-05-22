with open('intercepted_message.txt', 'r') as inF:
    for l in inF:
        for n in l[:-1].split(' '):
            try:
                n = int(n)
                # print(f"{n} --> {n//313} --> {chr(n//313)}")
                print(f"{chr(n//313)}", end='')
            except:
                pass
  
        print()
