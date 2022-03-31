import os
import time

if __name__ == '__main__':
    file_path = input("Enter absolute file path\n")
    destination_file_path = input("Enter destination file path\n")
    print("Sorting...\n")
    start = time.time()
    os.system(f"sort {file_path} -o {destination_file_path}")
    end = time.time()
    print(f"Finished in {end - start} seconds.")