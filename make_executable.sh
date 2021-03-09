#!/usr/bin/env bash

function installRequirements() {
  echo "Installing requirements, needed to be sudo"
  sudo pip3 install -r requirements.txt
}

function generateExecutable() {
  echo "Generate executable"
  pyinstaller --onefile --noconsole maze_game.py
}

function copyAssets() {
  echo "Copying Assets"
  cp -R assets dist/assets
}

function packingDistributable() {
  echo "Packing distributable"
  this_dir=$PWD
  cd dist
  zip -r maze_game . maze_game.zip
  cd $this_dir
}

echo "Creating a executable for maze_game"

installRequirements
generateExecutable
copyAssets
packingDistributable