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


def __list_backgrounds(backgrounds):
    tag_normal = __generate_image("background_normal", f"images/{backgrounds['normal']}")
    tag_start = __generate_image("background_start", f"images/{backgrounds['start']}")
    tag_end = __generate_image("background_end", f"images/{backgrounds['end']}")
    image_list.append(tag_normal)
    image_list.append(tag_start)
    image_list.append(tag_end)

    backgrounds_doc = f"""
## Backgrounds

**Normal**:

![background_normal][background_normal]

**Start**:

![background_start][background_start]

**End**:

![background_end][background_end]

"""

    return backgrounds_doc


def __hud_section(hud):
    tag_hud = __generate_image("hud", f"images/{hud['image']}")
    image_list.append(tag_hud)

    hud_doc = f"""
## HUD

**Image**:

![hud][hud]

| Property | Value |
|:--------:|:-----:|
| font | {hud['font']} |
| font-size | {hud['font-size']} |
| font-color | {hud['font-color']} |
| background-color | {hud['background-color']} |

"""
    return hud_doc


def __obstacle_section(obstacles):
    tag_big_rock = __generate_image("big-rock", f"images/{obstacles['big-rock']}")
    tag_rock_large = __generate_image("rock-large", f"images/{obstacles['rock-large']}")
    tag_rock_medium = __generate_image("rock-medium", f"images/{obstacles['rock-medium']}")
    tag_rock_small = __generate_image("rock-small", f"images/{obstacles['rock-small']}")
    tag_column = __generate_image("column", f"images/{obstacles['column']}")
    tag_cross_arm = __generate_image("cross-arm", f"images/{obstacles['cross-arm']}")
    image_list.append(tag_big_rock)
    image_list.append(tag_rock_large)
    image_list.append(tag_rock_medium)
    image_list.append(tag_rock_small)
    image_list.append(tag_column)
    image_list.append(tag_cross_arm)

    obstacles_doc = f"""
## Obstacles

**Rock**:

![big-rock][big-rock]

**Large Rock**:

![rock-large][rock-large]

**Medium Rock**:

![rock-medium][rock-medium]

**Small Rock**:

![rock-small][rock-small]

**Column**:

![column][column]

**Cross Arm**:

![cross-arm][cross-arm]

"""

    return obstacles_doc


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
        writer.write(__list_backgrounds(skin["skin"]["backgrounds"]))
        writer.write(__hud_section(skin["skin"]["hud"]))
        writer.write(__obstacle_section(skin["skin"]["obstacles"]))
        writer.write(__image_list())


if __name__ == '__main__':
    main()
