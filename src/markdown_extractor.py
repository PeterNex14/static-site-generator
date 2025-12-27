def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# ") and not line.startswith("##"):
            return line[2:].strip()
    raise Exception("Heading not found")
