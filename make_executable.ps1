function RemoveOldBuilds {
	Write-Output "Cleaning files"
    if (Test-Path -Path "build") {
        Write-Output " - Cleaning build"
        Remove-Item "build" -Recurse
    }

    if (Test-Path -Path "dist") {
        Write-Output " - Cleaning dist"
        Remove-Item "dist" -Recurse
    }

    if (Test-Path "maze_game.zip") {
        Write-Output " - Cleaning distributable package"
        Remove-Item "maze_game.zip" -Recurse
    }

    if (Test-Path "maze_game.spec") {
        Write-Output " - Cleaning specs"
        Remove-Item "maze_game.spec" -Recurse
    }

    Write-Output " - Everything is clean now!"
}

function Install-Requirements {
    Write-Output "Installing dependencies"
    pip install -r requirements.txt
}

function Make-Executable {
    Write-Output "Generate executable"
	python -m PyInstaller --onefile --noconsole maze_game.py
}

function Prepare-Distributable {
    cd dist
    Copy-Item -Path ../assets/ -Destination . -Recurse
    Copy-Item -Path ../README.txt -Destination .
    Copy-Item -Path ../README.md -Destination .
    Copy-Item -Path ../docs -Destination . -Recurse
    Compress-Archive -Path * -DestinationPath maze_game.zip
    Copy-Item -Path ./maze_game.zip -Destination ..
    cd ..
}

RemoveOldBuilds
cls
Install-Requirements
cls
Make-Executable
cls
Prepare-Distributable
cls
Write-Output "Done!"