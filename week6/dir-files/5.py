l = ["a", "b", "c"]
with open("hello.txt", "w") as file:
    rfile = file.writelines(line + "\n" for line in l)
