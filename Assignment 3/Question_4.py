'''
This program copies content from one file to another with error handling.
'''

src = input("Input file name: ")
dst = input("Output file name: ")

try:
    with open(src, "r") as f:
        content = f.read()
    with open(dst, "w") as f:
        f.write(content)
    print("File copied successfully")
except FileNotFoundError:
    print("Input file does not exist")
except FileExistsError:
    print("Output file already exists")
except:
    print("Some error occurred")
