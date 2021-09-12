import argparse
import json
import os
from jinja2 import Template

template_file = "README.md.template"
target_file = "README.md"


class Hud:
    image = ""
    font = ""
    font_size = 0
    font_color = ""
    background_color = ""

    def to_dict(self):
        hub_dict = {
            "image": self.image,
            "font": self.font,
            "font_size": self.font_size,
            "font_color": self.font_color,
            "background_color": self.background_color
        }

        return hub_dict

    def to_string(self):
        return f"""
- HUD ---------------------------------------------------------------
  Image.............: {self.image}
  Font..............: {self.font}
  Font Size.........: {self.font_size}
  Font Color........: {self.font_color}
  Background Color..: {self.background_color}
---------------------------------------------------------------------"""


class Skin:
    name = ""
    author = ""
    mail = ""
    description = ""
    folder = ""
    images = {}
    hud = Hud

    def to_dict(self):
        skin_dict = {
            "name": self.name,
            "author": self.author,
            "mail": self.mail,
            "description": self.description,
            "folder": self.folder,
            "images": self.images,
            "hud": self.hud.to_dict()
        }

        return skin_dict

    def to_string(self):
        rep = f"""
print("= SKIN ==============================================================")
print(f"Name.........: {self.name}")
print(f"Author.......: {self.author}")
print(f"Mail.........: {self.mail}")
print(f"Description..: {self.description}")
print(f"Folder.......: {self.folder}")
print("Images")"""

        image_list = ""
        for image in self.images:
            image_list = image_list + f" - {image}: {self.images[image]}\n"

        image_list = image_list.removesuffix("\n")

        rep = rep + f"""
{image_list}
{self.hud.to_string()}
=====================================================================
"""
        return rep


def __image_map(prefix, images, skin_data):
    for key in images:
        doc_key = f"img_{prefix}_{key}".replace('-', '_')
        skin_data.images[doc_key] = images[key]


def __to_hud(data):
    hud_data = Hud()
    hud_data.image = data["image"]
    hud_data.font = data["font"]
    hud_data.font_size = data["font-size"]
    hud_data.font_color = data["font-color"]
    hud_data.background_color = data["background-color"]
    return hud_data


def __to_skin(data):
    skin_data = Skin()
    skin_data.name = data["name"]
    skin_data.author = data["author"]
    skin_data.mail = data["mail"]
    skin_data.description = data["description"]
    skin_data.folder = data["folder"]

    prefixes = ["walls", "backgrounds", "items", "obstacles"]

    for prefix in prefixes:
        __image_map(prefix, data["skin"][prefix], skin_data)

    hud = __to_hud(data["skin"]["hud"])
    skin_data.images["img_hud"] = hud.image
    skin_data.hud = hud

    return skin_data


def __render(template, skin_data):
    return template.render(
        skin=skin_data).strip()


def ___generate_readme(skin_data):
    with open(template_file) as file_:
        template = Template(file_.read())

    rendered_report = __render(template, skin_data)

    target_folder = skin_data["folder"]
    with open(f"{target_folder}/{target_file}", 'a') as writer:
        writer.writelines(rendered_report)

    file_.close()
    writer.close()


def main():
    parser = argparse.ArgumentParser(
        prog="skindoc",
        description="Creates documentation for skins",
    )
    parser.add_argument(
        "--skin",
        help="Skin JSON file",
        type=str,
    )
    args = parser.parse_args()
    arguments = vars(args)
    skin_parameter = arguments['skin']

    with open(os.path.join(f"{skin_parameter}.json"), "r+") as skin_definition:
        skin = json.load(skin_definition)

    template_data = __to_skin(skin)

    ___generate_readme(template_data.to_dict())


if __name__ == '__main__':
    main()
