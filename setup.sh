#!/bin/bash

easyclip_version="v0.0.1"

echo "Installing EasyClip"

# Download EasyClip binary
sudo wget -P /usr/local/bin https://github.com/dhsathiya/EasyClip/releases/download/$easyclip_version/easyclip -q --show-progress
sudo chmod +x /usr/local/bin/easyclip

# Download EasyClip png
mkdir -p ~/.local/share/icons/easyclip
wget -P ~/.local/share/icons/easyclip https://raw.githubusercontent.com/dhsathiya/EasyClip/master/images/easyclip.png -q --show-progress

# Create Applicatios entry
echo "[Desktop Entry]
Type=Application
Name=EasyClip
Icon=$(eval echo "~$USER")/.local/share/icons/easyclip/easyclip.png
Exec=/usr/local/bin/easyclip
Categories=Utility
Terminal=False" > ~/.local/share/applications/dhsathiya-easyclip.desktop

chmod +x ~/.local/share/applications/dhsathiya-easyclip.desktop
xdg-desktop-menu install ~/.local/share/applications/dhsathiya-easyclip.desktop

echo "Easyclip is currently tested on Ubuntu 20.04 only."
echo "If you find any issues please report at: https://github.com/dhsathiya/EasyClip/issues/new"
