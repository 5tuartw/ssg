import re

def extract_markdown_images(text):
  # r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  return matches

def extract_markdown_url(text):
  # r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  return matches
