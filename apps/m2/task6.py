import sys
from bs4 import BeautifulSoup, SoupReplacer

# Check command-line arguments
if len(sys.argv) < 2:
    print("Usage: python3 task6.py <filename>")
    sys.exit(1) # terminate the program and indicate that an error occurred.

file_name = sys.argv[1]

# Read the file
try:
    with open(file_name, "r", encoding="utf-8") as file: 
        content = file.read()

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    sys.exit(1)

# Parse HTML or XML into a tree
if file_name.lower().endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"

soup = BeautifulSoup(content, parser, replacer=SoupReplacer("b", "blockquote"))

# Write the modified HTML tree to a file.
with open("outputB.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())