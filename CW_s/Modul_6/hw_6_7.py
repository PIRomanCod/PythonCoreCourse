import re


def sanitize_file(source, output):

    with open(source, "r") as fh:
        source_content = fh.read()
        output_content = re.sub(r"\d", "", source_content)

    with open(output, "w") as fh:
        fh.write(output_content)


sanitize_file(r"recipe.txt", r"sanitized.txt")
