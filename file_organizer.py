import os
#helps move/copy files 
import shutil 
#target folder 
TARGET_FOLDER = r"C:\Users\ayesha shaikh\Downloads"

FILE_TYPES = {
"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
"Videos": [".mp4", ".mkv", ".avi", ".mov"],
"Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
"Audio": [".mp3", ".wav", ".aac"],
"Archives": [".zip", ".rar", ".tar", ".gz"],
"Python Files": [".py"],
"Others": []
}

#function to create a folder
#creates a folder if does not exist
def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

#find the category for given file extension
def get_category(file_ext):
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return "others"    

def organize_files():
    print(f"\nOrganizing files in {TARGET_FOLDER}\n")

for filename in os.listdir(TARGET_FOLDER):
    file_path = os.path.join(TARGET_FOLDER, filename)

    #skip folders
    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(filename)
    category = get_category(ext)

    #create a category folder
    category_folder = os.path.join(TARGET_FOLDER, category)
    create_folder(category_folder)

    #move file
    new_path = os.path.join(category_folder, filename)
    shutil.move(file_path, new_path)

    print(f"Moved:{filename} --> {category}/")
    print("\nFiles organized sucessfully!")

if __name__ == "__main__":
    organize_files()    
    
