s = "Mrityunjay is a good boy."

# # writing into a file.
# with open("test.txt","w") as f:
#     f.write(s)
#
# #reading to a file.
#
with open("test.txt","r") as f:
    str1 = f.read()
    str2 = f.readline()
    str3 = f.readlines()
    print(str1)
    print(str2)
    print("\n\n")
    print(str1, str2, str3)
fp = open("file.txt","r")
s1 = fp.read()
print(s1)
fp.close()

f = open("file.txt", "a")
f.write("I'm learning python from Harry bhaiya with his one shot seris.")
f.close()



