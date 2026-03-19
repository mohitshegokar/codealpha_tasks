import os
import re
import shutil
source_folder = "source_images"
destination_folder = "jpg_files"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
for file in os.listdir(source_folder):
    
    
    if file.endswith(".jpg"):
        
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)# Move file

        print(file, "!!! moved successfully !!!")

print("All jpg files moved!")



#Extract email addresses from .txt file program no:2
file = open("data.txt", "r")
text = file.read()
file.close()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)
output = open("emails.txt", "w")
for email in emails:
    output.write(email + "\n")

output.close()
print("Email addresses extracted and saved in emails.txt")

