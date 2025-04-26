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


add_entry()

