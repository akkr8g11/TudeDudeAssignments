with open ("output.txt", "w+") as lines:
    lines.write(input("Enter text to write to the file: ") + "\n")
    print("Data successfully written to output.txt.")
    lines.write(input("Enter additional text to append: "))
    print ("Data successfully appended")
    print ("Final content of output.txt:")
    lines.seek(0)
    for line in lines:
        print(f"{line.strip()}")

