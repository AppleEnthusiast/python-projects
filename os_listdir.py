import os

def main():
    print("Current directory:", os.getcwd())

    for item in os.listdir():
        if os.path.isfile(item):
            print(f"File:       {item}")
        elif os.path.isdir(item):
            print(f"Directory:  {item}")
        else:
            print(f"Other:      {item}")

if __name__ == "__main__":
    main()

