import argparse
import json
import os

image_list = []


def __generate_image(key, file):
    return f"[img_{key}]: {file}"


def __title_section(title_doc, description):
    title_doc = f"""# {title_doc}

{description}
"""

    return title_doc


def __basic_info_section(name, author, mail, folder):
    basic_info_doc = f"""
## Basic info
    
**Skin Name**: {name}

**Author**: {author}

**e-mail**: {mail}

**Base folder**: `{folder}`

"""

    return basic_info_doc


def __item_section(items_doc):
    tag_coin = __generate_image("coin", f"images/{items_doc['coin']}")
    image_list.append(tag_coin)

    items_doc = f"""
## Items

**Coin**:

![Coin][img_coin]

"""

    return items_doc


def __backgrounds_section(backgrounds):
    tag_normal = __generate_image("background_normal", f"images/{backgrounds['normal']}")
    tag_start = __generate_image("background_start", f"images/{backgrounds['start']}")
    tag_end = __generate_image("background_end", f"images/{backgrounds['end']}")
    image_list.append(tag_normal)
    image_list.append(tag_start)
    image_list.append(tag_end)

    backgrounds_doc = f"""
## Backgrounds

**Normal**:

![Normal Background][img_background_normal]

**Start**:

![Start Background][img_background_start]

**End**:

![Ending Background][img_background_end]

"""

    return backgrounds_doc


def __hud_section(hud):
    tag_hud = __generate_image("hud", f"images/{hud['image']}")
    image_list.append(tag_hud)

    hud_doc = f"""
## HUD

**Image**:

![HUD][img_hud]

| Property | Value |
|:--------:|:-----:|
| font | {hud['font']} |
| font-size | {hud['font-size']} |
| font-color | {hud['font-color']} |
| background-color | {hud['background-color']} |

"""
    return hud_doc


def __obstacle_section(obstacles):
    tag_big_rock = __generate_image("big_rock", f"images/{obstacles['big-rock']}")
    tag_rock_large = __generate_image("rock_large", f"images/{obstacles['rock-large']}")
    tag_rock_medium = __generate_image("rock_medium", f"images/{obstacles['rock-medium']}")
    tag_rock_small = __generate_image("rock_small", f"images/{obstacles['rock-small']}")
    tag_column = __generate_image("column", f"images/{obstacles['column']}")
    tag_cross_arm = __generate_image("cross_arm", f"images/{obstacles['cross-arm']}")
    image_list.append(tag_big_rock)
    image_list.append(tag_rock_large)
    image_list.append(tag_rock_medium)
    image_list.append(tag_rock_small)
    image_list.append(tag_column)
    image_list.append(tag_cross_arm)

    obstacles_doc = f"""
## Obstacles

**Rock**:

![Big Rock][img_big_rock]

**Large Rock**:

![Large Rock][img_rock_large]

**Medium Rock**:

![Medium Rock][img_rock_medium]

**Small Rock**:

![Small Rock][img_rock_small]

**Column**:

![Column][img_column]

**Cross Arm**:

![Cross Arm][img_cross_arm]

"""

    return obstacles_doc


def __wall_section(obstacles):
    tag_corner = __generate_image("corner", f"images/{obstacles['corner']}")
    tag_exit_wall = __generate_image("exit_wall", f"images/{obstacles['exit-wall']}")
    tag_wall = __generate_image("wall", f"images/{obstacles['wall']}")
    image_list.append(tag_corner)
    image_list.append(tag_exit_wall)
    image_list.append(tag_wall)

    walls_doc = f"""
## Walls

**Corner**:

![Corners][img_corner]

**Exit Wall**:

![Exit Wall][img_exit_wall]

**Wall**:

![Wall][img_wall]

"""

    return walls_doc


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
        writer.write(__title_section(skin["name"], skin["description"]))
        writer.write(__basic_info_section(skin["name"], skin["author"], skin["mail"], skin["folder"]))
        writer.write(__item_section(skin["skin"]["items"]))
        writer.write(__backgrounds_section(skin["skin"]["backgrounds"]))
        writer.write(__hud_section(skin["skin"]["hud"]))
        writer.write(__obstacle_section(skin["skin"]["obstacles"]))
        writer.write(__wall_section(skin["skin"]["walls"]))
        writer.write(__image_list())


if __name__ == '__main__':
    main()
