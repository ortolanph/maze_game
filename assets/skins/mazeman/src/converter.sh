#!/usr/bin/env bash

OUTPUT_FOLDER=../images

ROOM_IMAGES=( mazeman-normal mazeman-start mazeman-end )
WALL_IMAGES=( mazeman-corner mazeman-exit-wall mazeman-exit-step mazeman-wall )
OBSTACLE_IMAGES=( mazeman-rock-s mazeman-rock-m mazeman-rock-l mazeman-rock-xl mazeman-column mazeman-cross-middle mazeman-cross-arm )
HUD_IMAGES=( mazeman-hud )

echo "- Items -----------------------------------------"
inkscape -z -w 50 -h 50 mazeman-coin.svg -e $OUTPUT_FOLDER/mazeman-coin.png

echo "- Room Images -----------------------------------"
for ROOM_IMAGE in "${ROOM_IMAGES[@]}"
do
	inkscape $ROOM_IMAGE".svg" -e $OUTPUT_FOLDER/$ROOM_IMAGE".png"
done

echo "- Walls -----------------------------------------"
for WALL_IMAGE in "${WALL_IMAGES[@]}"
do
	inkscape $WALL_IMAGE".svg" -e $OUTPUT_FOLDER/$WALL_IMAGE".png"
done

echo "- Obstacles -------------------------------------"
for OBSTACLE_IMAGE in "${OBSTACLE_IMAGES[@]}"
do
	inkscape $OBSTACLE_IMAGE".svg" -e $OUTPUT_FOLDER/$OBSTACLE_IMAGE".png"
done

echo "- Heads Up Display -------------------------------"
for HUD_IMAGE in "${HUD_IMAGES[@]}"
do
	inkscape $HUD_IMAGE".svg" -e $OUTPUT_FOLDER/$HUD_IMAGE".png"
done
