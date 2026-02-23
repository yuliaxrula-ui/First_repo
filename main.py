from pathlib import Path

def show_menu():
    print("\n-----File_Manager-----")
    print("1 - Show directory")
    print("2 - Create new directory")
    print("3 - Create new file")
    print("4 - Exit")

def list_directory():
    current = Path(".")
    print(f"\nFolder contents: {current.absolute()}")
    for item in current.iterdir():
        if item.name.startswith("."):
            continue
        elif item.is_file():
            size = item.stat().st_size
            print(f"📄 {item.name} -> {size} bytes")
        elif item.is_dir():    
            print(f"📁 {item.name}")

def create_folder():
    name = input("\nPlease enter the name of the folder: ")
    folder = Path(name)
    folder.mkdir(parents=True, exist_ok=True)
    print(f"\nNew folder created: {folder.absolute()}")

def create_file():
    name = input("\nPlease enter the name of the file: ")
    content = input("Enter file content: ")
    file_path = Path(name)
    if file_path.exists():
        answer = input("Overwrite existing one y/n: ")
        if answer.lower() == "n":
            print("\nDeclined")
            return 
    file_path.write_text(content, encoding="utf-8")
    print(f"\nFile created: {file_path.absolute()}")

def main():
    while True:
        show_menu()    
        choice = input("\nMake your choice from 1 to 4: ")
        
        if choice == "1":
            list_directory()
        elif choice == "2":             
            create_folder()
        elif choice == "3":
            create_file()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()