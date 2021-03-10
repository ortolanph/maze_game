pip3 install -r requirements.txt
pyinstaller --onefile --noconsole maze_game.py
cd dist
xcopy ..\assets
Compress-Archive -Path . -DestinationPath maze_game.zip
cd ..
copy dist/maze_game.zip .