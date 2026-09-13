import os
import shutil
import sys

from gen_page import generate_pages_recursive
from copystatic import copy_files_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"


def main() -> None:
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()

