# EasyClip ![Generic badge](https://img.shields.io/badge/Status-Beta-Yellow.svg) ![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

<img src="https://github.com/dhsathiya/EasyClip/raw/master/images/easyclip.png" align="right"
     alt="EasyClip logo" width="120" height="120">

[![License](https://img.shields.io/badge/License-MIT-success.svg)](https://opensource.org/licenses/MIT)
![Made With Python](https://img.shields.io/badge/Made%20With-Python-blue)
![Tested On Ubuntu 20.04](https://img.shields.io/badge/Tested%20On-Ubuntu%2020.04-orange)

Simple and Open-Source clipboard manager. Easy to use, Light Weight and with keyboard shortcuts.

<kbd>w</kbd> : Previous clip

<kbd>s</kbd> : Next clip

<kbd>c</kbd> : Copy current clip

<kbd>q</kbd> : Minimize window

![EasyClip demo GIF](https://github.com/dhsathiya/EasyClip/raw/master/images/easyclip.gif)

## Installation

```bash
wget -q -O - https://raw.githubusercontent.com/dhsathiya/EasyClip/master/setup.sh | bash
```

## Run EasyClip
```bash
easyclip
```

## ToDo
- Fix dirty code
- Add checksum verification
- GUI Improvements
- Image support
- Programmatic Improvements


## Uninstallation
```bash
sudo rm -r ~/.local/share/icons/easyclip
sudo rm ~/.local/share/applications/dhsathiya-easyclip.desktop
sudo rm /usr/local/bin/easyclip
```
