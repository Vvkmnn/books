### Introduction

This is a series of Jupyter Notebooks following Al Sweigarts ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) [book](http://www.amazon.ca/Automate-Boring-Stuff-Python-Programming/dp/1593275994) and [video course](www.udemy/automate).

To get up and running with this book, you can follow along live within this Github repository, which natively supports Jupyter, or [clone the repository yourself](https://guides.github.com/activities/hello-world/).

To get up and running with this book, you can follow along live within this Github repository, which natively supports Jupyter, or [clone the repository yourself](https://guides.github.com/activities/hello-world/).

### Local Setup

I work on OSX Setup, and this is the method I used. This is available as a script in `setup.sh`.

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

    pip3 install pprint ipdb

### Notes

If you find any errors in this notebook, feel free to submit [an issue](https://guides.github.com/features/issues/) to flag it or a [pull request](https://guides.github.com/introduction/flow/) on Github to modify it yourself.

Lessons 1 - 16 were created and run via [Atom](https://atom.io/), and exist in `.py` formats. After lesson 17, I started creating [Jupyter](http://jupyter.org/) notebookst that use the `.ipynb` format.

I want to theoritcally update all the Python script code to Jupyter notebooks, but it is also partially indicative of my transition within this project itself, so I might just leave it for posterity. Most of its pretty simple code which should run fine as is.

This was created entirely for my own learning, and I learnt a whole lot getting this off the ground. This work has not been reviewed by Al Sweigart, and is no way a reflection on him and his work. I highly recommend his book for the novice or the experienced Python user; I guarantee you'll learn something new.
