function Install-Requirements {
    Write-Output "Installing dependencies"
    pip3 install -r requirements.txt
}

function Make-Executable {
    Write-Output "Generata executable"
    pyinstaller --onefile --noconsole maze_game.py
}

function Prepare-Distributable {
    cd dist
    Copy-Item -Path ../assets/ -Destination . -Recurse
    Compress-Archive -Path * -DestinationPath maze_game.zip
    Copy-Item -Path ./maze_game.zip -Destination ..
    cd ..
}

Install-Requirements
Make-Executable
Prepare-Distributable