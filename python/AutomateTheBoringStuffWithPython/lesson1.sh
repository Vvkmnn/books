#!/usr/bin/env bash

# install and setup brew and cask for applications

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap caskroom/cask

# Setup Python 3 for lessons

brew cask install python3

# Setup an IDE (Atom or Jupyter)

brew cask install atom

# Setup Jupyter for notebooks
brew cask install Jupyter
