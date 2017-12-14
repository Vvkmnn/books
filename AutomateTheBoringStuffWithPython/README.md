
# Automate The Boring Stuff with Python
###  By Al Sweigart

## Introduction

This is a series of Jupyter Notebooks following Al Sweigarts ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) [book](http://www.amazon.ca/Automate-Boring-Stuff-Python-Programming/dp/1593275994) and [video course](www.udemy/automate).

I wrote these notebooks to follow along with his [Udemy](https://www.udemy.com/automate/learn/v4/t/lecture/3547544) course, and I found that publishing my work as I worked through it helped keep me motivated.To get up and running with this book, you can follow along live within this Github repository, which natively supports Jupyter, or [clone the repository yourself](https://guides.github.com/activities/hello-world/).

This repo includes custom/mirrored versions of all the lesson content & scripts, as well as [all provided supporting  files](https://www.nostarch.com/automatestuff) (and then some) stored in the `/files` folder.

### Local Setup

I work on OSX, and this is the method I used to setup  my environment. This is available as a script in `setup.sh`, which can be run with `sh setup.sh` from your repo directory.

In your Terminal, input the following uncommented code:

    # For OSX users: install and setup brew and cask for code and applications
    # For UNIX users: use whatever package manager you typically use to get these packages.

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew tap caskroom/cask

    # Setup Python 3

    brew cask install python3

    # Setup a Text Editor (Atom)

    brew cask install atom

    # Setup an IDE to handle iPython Notebooks (Jupyter)

    pip3 install jupyter

    # Setup Python 3 kernel in Jupyter for easy use/switching

    ipython3 kernel install

    # Install some of the packages we might need later on; use pip3 to install any module that isn't available

    pip3 install pprint

## Notes

If you find any errors in this notebook, feel free to submit [an issue](https://guides.github.com/features/issues/) to flag it or a [pull request](https://guides.github.com/introduction/flow/) on Github to suggest a modification.

Lessons 1 - 16 were created with [Atom](https://atom.io/), and exist in `.py` script format. After lesson 17, I started creating [Jupyter](http://jupyter.org/) notebooks that use the `.ipynb` format because I found it super fun to use.

Theoretically, I'd like to transform all the Python scripts into Jupyter notebooks, but given that it's partially indicative of my transition within this project itself, I might just leave it for posterity. The code I have transformed so far is in `/transitions`.

This was created entirely for my own learning, and I learnt a whole lot getting this off the ground. This work has not been reviewed by Al Sweigart, and is no way a reflection on him and his work; I highly recommend his actual book for the novice or the experienced Python user, I guarantee you'll learn something new. 
