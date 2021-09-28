import mkl_random

def primary():
 #  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = mkl_random.randint(0,last)
  
  print(quotes[rnd])

if __name__== "__main__":
  primary()
