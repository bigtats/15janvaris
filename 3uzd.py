with open("file.txt", "r") as file:
   data = file.readlines()

if len(data) >= 3:
   print(data[2].strip())
else:
   print("Nav pietiekami daudz rindu.")