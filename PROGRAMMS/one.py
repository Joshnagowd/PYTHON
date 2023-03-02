w1= "listen"
w2= "silent"
def anagrom(w1,w2):
    if len(w1)==len(w2) and sorted(w1)==sorted(w2):
        print("Anagrom")
    else:
        print("not anagrom")