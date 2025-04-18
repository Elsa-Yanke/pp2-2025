import os

folder_name = "filesA-Z"
os.makedirs(folder_name, exist_ok=True)
for i in range(65, 91):  
    file_name = f"{chr(i)}.txt"  
    file_path = os.path.join(folder_name, file_name)  
    open(file_path, "w").close()  

