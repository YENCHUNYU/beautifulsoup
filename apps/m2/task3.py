import sys
from bs4 import BeautifulSoup, SoupStrainer


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 task3.py <filename>")
        return 1

    file_name = sys.argv[1]
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return 1

    parser = "xml" if file_name.lower().endswith(".xml") else "html.parser"
    all_tags = SoupStrainer(True)
    soup = BeautifulSoup(content, parser, parse_only=all_tags)

    for tag in soup.find_all(True):
        print(tag.name)

    return 0


if __name__ == "__main__":
    sys.exit(main())