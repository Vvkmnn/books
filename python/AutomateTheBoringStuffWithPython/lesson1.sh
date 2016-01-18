#!/usr/bin/env bash

# install and setup brew and cask for applications

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap caskroom/cask

# Setup Python 3 for lessons

brew cask install python3

# Setup an Text Editor (Atom)

brew cask install atom

# Setup an IDE (Jupyter)

pip3 install jupyter

# Setup Python 3 kernel in Jupyter for easy use/switching
ipython3 kernel install
