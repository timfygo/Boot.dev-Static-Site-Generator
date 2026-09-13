from markdown_blocks import extract_title, markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_path_contents = file.read()
    with open(template_path) as file:
        template_path_contents = file.read()
    html = markdown_to_html_node(from_path_contents)
    html = html.to_html()
    title = extract_title(from_path_contents)
    template_path_contents = template_path_contents.replace("{{ Title }}", title)
    template_path_contents = template_path_contents.replace("{{ Content }}", html)
    template_path_contents = template_path_contents.replace('href="/', f'href="{basepath}')
    template_path_contents = template_path_contents.replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
       file.write(template_path_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        destination_subdir = os.path.join(dest_dir_path, entry)
        if entry.endswith(".md"):
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry[:-3] + ".html"), basepath)
        else:
            os.makedirs(destination_subdir, exist_ok=True)
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, destination_subdir, basepath)
