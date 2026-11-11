import sys

from bs4 import BeautifulSoup, SoupReplacer


def set_paragraph_class(tag):
    if tag.name == "p":
        tag["class"] = "test"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 task7.py <filename>")
        return 1

    file_name = sys.argv[1]
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return 1

    parser = "xml" if file_name.lower().endswith(".xml") else "html.parser"
    soup = BeautifulSoup(
        content,
        parser,
        replacer=SoupReplacer(xformer=set_paragraph_class),
    )

    with open("outputClass.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
    return 0


if __name__ == "__main__":
    sys.exit(main())
