import re

def extract_markdown_images(text):
  # r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  #print(f"The matches are {matches}")

  return matches

def extract_markdown_links(text):
  # r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  return matches
