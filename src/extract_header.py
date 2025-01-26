import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

def extract_title(markdown_file):
    
    f = open(markdown_file, "r")
    markdown = f.read()
    f.close()
    markdown_lines = markdown.split("\n")
    header_line = ""
    line_no = 0
    while header_line == "" and line_no < len(markdown_lines):
        if markdown_lines[line_no].startswith("# "):
            header_line = markdown_lines[line_no][2:]
        line_no += 1
    
    if header_line == "":
        raise Exception(f"No h1 header found in {markdown_file}")
    
    return header_line
