# GUEST LIST (3-4)

names = ['DIVINE', 'JOHN', 'SARAH', 'ELMA', 'SANDRA', 'BRANDON', 'MAXIMILLIAN ']
print(names)

print(names[0], "am inviting u for a dinner\n.")
print(names[1], "am inviting u for a dinner\n.")
print(names[2], "am inviting u for a dinner\n.")
print(names[3], "am inviting u for a dinner\n.")
print(names[4], "am inviting u for a dinner\n.")
print(names[5], "am inviting u for a dinner\n.")
print(names[6], "am inviting u for a dinner\n.")


      # CHANGING GUEST (3-5)
print(names[0], "will not attend the dinner\n.")

names[0] = "SMITH"
print(names[0], "you are invited for the dinner \n")
print(names[0], "will attend the dinner \n.")
print(names[1], "will attend the dinner\n.")
print(names[2], "will attend the dinner\n.")
print(names[3], "will attend the dinner\n.")
print(names[4], "will attend the dinner\n.")
print(names[5], "will attend the dinner\n.")
print(names[6], "will attend the dinner\n.")

print( names[1:6], "will attend the dinner\n")

     # MORE GUEST (3-6)
print("A bigger dinner table was found \n")
names.insert(0, "RICHARD ")
names.insert(5, "BRANDY")
names.append( "LINDA")
print(names)

print( "New names where added in the list of new guest, an they where invited to the dinner. \n")


print(names[0], "you are invited for the diner \n")
print(names[1], "you are invited for the dinner \n")
print(names[2], "you are invited for the dinner \n")
print(names[3], "you are invited for the dinner \n")
print(names[4], "you are invited for the dinner \n")
print(names[5], "you are invited for the dinner \n")
print(names[6], "you are invited for the dinner \n")

print(len(names),"names where invited for the dinner \n")

