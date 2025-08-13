item = int(input("New item: ")) # Initial input from user
input_list = [] # Initialize list to track input order
ordered_list=[] # Initialize sorted list
index = 0 
while item != 0:  # Run loop until 0 is input, loop adds each input to the input_list and then sorts that list, print both
  input_list.append(item)
  ordered_list = sorted(input_list) 
  print(f"The list now: {input_list}")
  print(f"The list in order: {ordered_list}")
  item = int(input("New item: ")) # Repeat input prompt until user enters 0
print("Bye!")
