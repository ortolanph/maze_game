import argparse
import json
import os


def __gen_title(title, description):
    title = f"""# {title}

{description}
"""

    return title


def __gen_basic_info(name, author, mail, folder):
    basic_info = f"""
## Basic info
    
**Skin Name**: {name}
    
**Author**: {author}
    
**e-mail: {mail}
    
**Base folder**: `{folder}`
"""

    return basic_info


def main():
    parser = argparse.ArgumentParser(
        prog="skindoc",
        description="Creates documentation for skins",
    )
    parser.add_argument(
        "--skin",
        help="Skin SVG file",
        type=str,
    )
    args = parser.parse_args()
    arguments = vars(args)
    skin_parameter = arguments['skin']

    with open(os.path.join(f"{skin_parameter}.json"), "r+") as skin_definition:
        skin = json.load(skin_definition)

    file_name = f"{skin['folder']}/README.md"

    with open(file_name, 'a') as writer:
        writer.write(__gen_title(skin["name"], skin["description"]))
        writer.write((__gen_basic_info(skin["name"], skin["author"], skin["mail"], skin["folder"])))


if __name__ == '__main__':
    main()