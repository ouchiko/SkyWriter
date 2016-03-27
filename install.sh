# -
# Basic Skywriter Setup Script
# Taken as base from rasppi org
# --
curl -sSL get.pimoroni.com/skywriter | bash
sudo apt-get install libx11-dev libxtst-dev
sudo pip install autopy
git clone https://github.com/pimoroni/skywriter-hat.git
cd Pimoroni/skywriter
sudo python test.py
