# Simple script to read and print log file contents
with open("../logs/sample_auth.log", "r") as file:
    for line in file:
        print(line.strip())
