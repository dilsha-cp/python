def copyfile(s_file,d_file):
    try:
      with open(s_file,'r')as file_sourse:
        with open(d_file,'w')as file_destination:
            for line in file_sourse:
                file_destination.write(line)
      print(f"content of {s_file} is copied to {d_file}")
    except FileNotFoundError as e:
      print(f"file not found error: {e}")

        
s_file="file1.txt"
d_file="file2.txt"
copyfile(s_file,d_file)