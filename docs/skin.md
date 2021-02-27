# Skin

Skin is a set of images, a font configuration and some colors to make a customization on the game.

## Loading skins

On the command line, use the `--skin SKIN` parameter to load a skin. The skins are located on the `assets/skin` folder. It's not needed to put the `.json` extension on the command line.

## Basic Skin

The game comes with a basic skin. Refer to [this document](../assets/skins/basic/README.md) to see the used pictures.

## Creating your own skins

If you want to create your own skin, follow this guide.

The first thing is to create the skin structure that comprehends in the skin descriptor file in json format and the folder structure, that should be named as the same name of the descriptor file. The list below shows the structure:

```
my_skin.json
my_skin/fonts
my_skin/images
my_skin/src
my_skin/README.md
```

Where:

 - `my_skin.json` is the skin descriptor
 - `my_skin/fonts` is the fonts directory
 - `my_skin/images` is the images directory
 - `my_skin/src` is the optional sources directory
 - `my_skin/README.md` is the skin README created by the `skindoc.py` util  

The skin descriptor has the following structure:

```json
{
  "name": "My Skin",
  "author": "Author Name Surname",
  "mail": "author.name.surname@mail.com",
  "description": "Some descriptor here",
  "folder": "my_skin",
  "skin": {
    "walls": {
      "corner": "image-to-corner.png",
      "wall": "image-to-wall.png",
      "exit-wall": "image-to-exit-wall.png"
    },
    "backgrounds": {
      "normal": "image-to-normal.png",
      "start": "image-to-start.png",
      "end": "image-to-end.png"
    },
    "items": {
      "coin": "image-to-coin.png"
    },
    "hud": {
      "image": "image-to-hud.png",
      "font": "my-skin-font.ttf",
      "font-size": "20",
      "font-color": [
        255,
        255,
        0
      ],
      "background-color": [
        0,
        0,
        0
      ]
    },
    "obstacles": {
      "big-rock": "image-to-rock-xl.png",
      "rock-large": "image-to-rocks-x.png",
      "rock-medium": "image-to-rock-m.png",
      "rock-small": "image-to-rock-s.png",
      "column": "image-to-column.png",
      "cross-arm": "image-to-cross-arm.png"
    }
  }
}
```

### Metadata section

The metadata section stores the description, the author, how to contact and the skin folder. 

```json
  "name": "My Skin",
  "author": "Author Name Surname",
  "mail": "author.name.surname@mail.com",
  "description": "Some descriptor here",
  "folder": "my_skin"
```

This will be show on the console when loading the skin.

### Skin section

The skin section describes the elements that will be rendered in the screen.

#### Walls

The walls sections have three pictures. The following excerpt shows the walls section:

```json
    "walls": {
      "corner": "image-to-corner.png",
      "wall": "image-to-wall.png",
      "exit-wall": "image-to-exit-wall.png"
    }
```

The walls are composed mainly by three pictures: 

| Image | Width (px) | Height (px) |
| ----- |:----------:|:-----------:|
| Corners | 50 | 50 |
| Walls | 800 | 50 |
| Exits | 250 | 50 |

All these elements are flipped and rotated to be drawn in the screen in their right position.

#### Backgrounds

The backgrounds sections contains three images. Here follow the code:

```json
    "backgrounds": {
      "normal": "image-to-normal.png",
      "start": "image-to-start.png",
      "end": "image-to-end.png"
    }
```

The walls are composed mainly by three pictures:

| Image | Width (px) | Height (px) |
| ----- |:----------:|:-----------:|
| Normal | 800 | 800 |
| Start | 800 | 800 |
| End | 800 | 800 |

#### Items

The items represent stuff that can be used or can be collected during a gameplay: 

For now there is just the Coin item that you can collect.

```json
    "items": {
      "coin": "image-to-coin.png"
    }
```

All items have 50 px width and 50 px height.

#### HUD

The HUD section allows font and color customization. Here follows an example:

```json
    "hud": {
      "image": "image-to-hud.png",
      "font": "my-skin-font.ttf",
      "font-size": "20",
      "font-color": [
        255,
        255,
        0
      ],
      "background-color": [
        0,
        0,
        0
      ]
    }
```

The elements:

| Image | Width (px) | Height (px) |
| ----- |:----------:|:-----------:|
| HUD | 800 | 100 |

Some considerations:
 - The font should come together with the license if any
 - It's recommended `20px` to the font size

The texts will be written at:

| Text | x | y | Format |
| --- |:---:|:---:|:---:|
| X | 60 | 15 | `000` |
| Y | 60 | 55 | `000` |
| GOLD | 620 | 20 | `00000000` |

 - The colors are in the R, G and B order
 - The background color is used to erase the text where the coordinates and the total money are located

| Element | x | y | width | height |
| --- |:---:|:---:|:---:|:---:|
| X Coordinate | 60 | 15 | 60 | 25 |
| Y Coordinate | 60 | 55 | 60 | 25 |
| Gold | 610 | 20 | 170 | 25 |

The space between the coordinates and the gold collected is reserved for future uses.

#### Obstacles

There are six images regarding the obstacles:

```json
    "obstacles": {
      "big-rock": "image-to-rock-xl.png",
      "rock-large": "image-to-rocks-x.png",
      "rock-medium": "image-to-rock-m.png",
      "rock-small": "image-to-rock-s.png",
      "column": "image-to-column.png",
      "cross-arm": "image-to-cross-arm.png"
    }
```

In the following table, their dimensions:

| Obstacle | width | height |
| -------- |:-----:|:------:|
| Big Rock    | 400 | 400 |
| Large Rock  | 150 | 250 |
| Medium Rock | 150 | 150 |
| Small Rock  |  50 |  50 |
| Column      | 200 | 200 |
| Cross Arm   | 200 | 150 |

Considerations:

 - The cross arm represents the north arm. It will combine with the column picture and will be drawn around it.
 - The large rock will be flipped and rotated

## Documenting a skin

If you want to create a skin, don't forget to document it. Look at the [Skin README](../assets/skins/README.md) for more details. 

[Back](../README.md)
