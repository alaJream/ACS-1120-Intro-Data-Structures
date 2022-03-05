import re


def clean_file(file):
    with open(file, "r") as source_file:
        lines = source_file.read()

        cleaned_lines = re.sub("\[.*?\]", "", lines)
        cleaned_lines = cleaned_lines.replace("‘", "\'")
        cleaned_lines = cleaned_lines.replace("’", "\'")
        cleaned_lines = cleaned_lines.replace("“", "\"")
        cleaned_lines = cleaned_lines.replace("”", "\"")

    with open(file, "w") as source_file:
        source_file.write(cleaned_lines)

    return cleaned_lines


if __name__ == "__main__":
    clean_file("data/corpus.txt")