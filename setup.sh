# Author: Reilly Parent (R3IXY)
# Copyright (c) Reilly Parent 2021
#
# https://r3ixy.com/

mkdir ~/.pypreprocessor
echo "Made ~/.pypreprocessor directory"
cp preprocessor.py ~/.pypreprocessor
echo "Copied preprocessor.py into ~/.pypreprocessor directory"
echo "alias piethon=\"python3 ~/.pypreprocessor/preprocessor.py\"" >> ~/.bashrc
echo "Added \"piethon\" alias to ~/.bashrc"
source ~/.bashrc
echo "Reloaded ~/.bashrc"
echo "Enjoy python preprocessing!"
