try:
    with open("sample.txt", "r") as lines:
        print (f"Reading the file content:")
        for lineNum, line in enumerate(lines, start=1):
            print (f"Line{lineNum}: {line.strip()}")
except FileNotFoundError as e:
    print (f"Error: The file 'sample.txt' was not found")
except:
    print (f"Error Opening and reading file")
