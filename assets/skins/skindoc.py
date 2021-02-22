import argparse
import json
import os

image_list = []


def __generate_image(key, file):
    return f"[{key}]: {file}"


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
    
**e-mail**: {mail}
    
**Base folder**: `{folder}`
"""

    return basic_info


def __item_list(items):
    image = __generate_image("coin", f"images/{items['coin']}")
    image_list.append(image)

    items = f"""
## Items

**Coin**:

![Coin][coin]

"""

    return items


def __image_list():
    all_images = ""

    for image in image_list:
        all_images += f"{image}\n"

    return all_images


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
        writer.write(__gen_basic_info(skin["name"], skin["author"], skin["mail"], skin["folder"]))
        writer.write(__item_list(skin["skin"]["items"]))
        writer.write(__image_list())


if __name__ == '__main__':
    main()
