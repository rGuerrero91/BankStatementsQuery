import os
directory = os.fsencode("./statements")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        print(os.path.join(directory, filename))
        continue
    else:
        continue
      