

try:
    with open("directory_path.txt") as file:
        path_dir = file.readline().rstrip()
        print(f"dir: {path_dir}")
except FileNotFoundError:
    print("path file is missing")
