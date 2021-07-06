
import os
from datetime import date
import subprocess
import sys


def convert_script_to_markdown(python_file, markdown_dir="/Users/fengzhixiao/Documents/Git_Webstie/zhr1996.github.io/_posts"):
    problem_name = os.path.basename(
        python_file).replace(".py", "").replace("_", " ")

    prev_line = ""
    mark_down_array = []

    # Blog meta data
    mark_down_array.append("---\n")
    mark_down_array.append("layout: post\n")
    mark_down_array.append("title: " + problem_name + "\n")
    mark_down_array.append("subtitle: " + "Leetcode Daily Challenge\n")
    mark_down_array.append("date: " + date.today().strftime("%Y-%m-%d") + "\n")
    mark_down_array.append("author: Haoran\n")
    mark_down_array.append("header-img: img/post-bg-2015.jpg\n")
    mark_down_array.append("catalog: true\n")
    mark_down_array.append("tags: \n")
    mark_down_array.append("  - Leetcode\n")
    mark_down_array.append("  - Algorithm\n")
    mark_down_array.append("  - Daily Challenge\n")
    mark_down_array.append("---\n")
    mark_down_array.append("\n\n")

    with open(python_file, 'r') as py_file:

        cur_line = py_file.readline()
        comment_start = False
        code_start = False
        while cur_line:
            if cur_line == "-------------------\n":
                prev_line = mark_down_array.pop()
                prev_line = "## " + prev_line

                mark_down_array.append(prev_line)
            elif cur_line == "'''\n":
                if not comment_start:
                    comment_start = True
                else:
                    code_start = True
                    mark_down_array.append("\n")
                    mark_down_array.append("```python\n")
            else:
                # if code_start:
                #     mark_down_array.append("        " + cur_line)
                # else:
                mark_down_array.append(cur_line)
            cur_line = py_file.readline()
        mark_down_array.append("```")

    mark_down_file_name = date.today().strftime("%Y-%m-%d") + "-" + \
        os.path.basename(python_file).replace(".py", ".md")

    with open(os.path.join(markdown_dir, mark_down_file_name), 'w') as mk:
        for line in mark_down_array:
            mk.write(line)

    return "success"


def publish_blog():
    bash_file = "/Users/fengzhixiao/Documents/Git_Webstie/zhr1996.github.io/git_cmd.sh"

    subprocess.run(bash_file)


if __name__ == "__main__":
    python_file = sys.argv[1]

    print(convert_script_to_markdown(python_file,
                                     "/Users/fengzhixiao/Documents/Git_Webstie/zhr1996.github.io/_posts"))
    publish_blog()
