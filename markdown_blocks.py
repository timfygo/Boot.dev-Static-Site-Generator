def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block: str) -> BlockType:
    if "#" in block[0:6]:
        return BlockType(HEADING)
    if "`" in block[0:3] and "`" in block[-3:-1]:
        return BlockType(CODE)
    if all(item.startswith(">") for line in block.split("\n"))
        return BlockType(QUOTE)
    if all(item.startswith("- ") for line in block.split("\n"))
        return BlockType(UNORDERED_LIST)
    lines = block.split("\n")
    i = 1
    for line in lines:
        if not line.startswith(f"{i}. ")
            break
        i += 1
    if i == len(lines):
        return BlockType(ORDERED_LIST)
    return BlockType(PARAGRAPH)

def extract_title(markdown):
    lines = markdown.spli("\n")
    for line in lines:
        if line.startswith("# "):
            return line.split(" ", 1)[1].strip()
    raise Exception("No h1 found")
