from datetime import datetime
filename='diary.txt'
def format_entry(title,content,timestamp,diaryname):
  return(
    f"\n--------------------{title}---------------------\n"
    f"Date:{timestamp}\n"
    f"Dear {diaryname}!,\n{content.strip()}\n"
    f"-------------------------------------------------------\n"
    )
  
def add_entry():
  
  title=input("Enter a title for your entry:")
  diaryname=input("Give a Name to your Diary:")
  content=input("Write your Entry:").strip()
  timestamp=datetime.now().strftime("%Y-%m-%d %I:%M %p")
 
  entry=format_entry(title,content,timestamp,diaryname)
  with open(filename,'a')as file:
    file.write(entry)
    print("Entry Successfully Saved!!")


def view_all_entries():
    try:
        with open(filename,"r") as file:
            content=file.read()
            if content.strip()=="":
                print("\n NO ENTRY WAS FOUND, DIARY IS EMPTY. \n")
            else:
                print("\n---------YOUR ENTRIES---------\n")
                print(content)
                print("\n-----------------------------------------------------\n")
    except FileNotFoundError:
        print("\n No Entry Found,Start by adding a entry! \n")

add_entry()
view_all_entries()

