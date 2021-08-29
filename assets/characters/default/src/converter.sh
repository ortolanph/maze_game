#!/usr/bin/env bash

OUTPUT_FOLDER=..

FRONT_IMAGES=( front_01 front_02 front_03 )
BACK_IMAGES=( back_01 back_02 back_03 )
LEFT_IMAGES=( left_01 left_02 left_03 )
RIGHT_IMAGES=( right_01 right_02 right_03 )

echo "- Front -----------------------------------------"
for FRONT_IMAGE in "${FRONT_IMAGES[@]}"
do
	inkscape $FRONT_IMAGE".svg" -e $OUTPUT_FOLDER/$FRONT_IMAGE".png"
done

echo "- Back ------------------------------------------"
#for BACK_IMAGE in "${BACK_IMAGES[@]}"
#do
#	inkscape $BACK_IMAGE".svg" -e $OUTPUT_FOLDER/$BACK_IMAGE".png"
#done

echo "- Left ------------------------------------------"
#for LEFT_IMAGE in "${LEFT_IMAGES[@]}"
#do
#	inkscape $LEFT_IMAGE".svg" -e $OUTPUT_FOLDER/$LEFT_IMAGE".png"
#done

echo "- Right -----------------------------------------"
#for RIGHT_IMAGE in "${RIGHT_IMAGES[@]}"
#do
#	inkscape $RIGHT_IMAGE".svg" -e $OUTPUT_FOLDER/$RIGHT_IMAGE".png"
#done