import mkl_random

def primary():
 #  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  num= int(input("how many quotes do you want to print?"))
  while num>last :
      num = int(input("how many quotes do you want to print?"))
      
  for i in range(num):
      rnd = mkl_random.randint(0,last) 
      print(quotes[rnd], end=" ")

if __name__== "__main__":
  primary()
