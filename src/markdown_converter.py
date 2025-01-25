
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped = [block.strip() for block in blocks]
    return stripped

def block_to_block_type(block):
    heading_starters = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(heading_starters):
        return "heading"
    if block[:3] == block[-3:] == "```":
        return "code"
    if block.startswith(">"):
        is_valid_quote = True
        for line in block.split("\n"):
            is_valid_quote = line.startswith(">")
            if not is_valid_quote:
                break
        if is_valid_quote:
            return "quote"
    ulist_starters = ("* ", "- ")
    if block.startswith(ulist_starters):
        is_valid_ulist = True
        for line in block.split("\n"):
            is_valid_ulist = line.startswith(ulist_starters)
            if not is_valid_ulist:
                break
        if is_valid_ulist:
            return "unordered_list"
    if block.startswith("1. "):
        number = 1
        is_valid_olist = True
        split_list = block.split("\n")
        for line in split_list:
            is_valid_olist = line.startswith(str(number)+". ")
            if not is_valid_olist:
                break
            number += 1
        if is_valid_olist:
            return "ordered_list"
    return "paragraph"

