# Rock, Paper, Scissors Shoot!

A fun game of Rock, Paper, Scissors.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/abhisheksn/rock-paper-scissors-game) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```
cd ~/Desktop/rock-paper-scissors-game
```

## Create Environment
Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":
```
conda create -n my-game-env python=3.8 #(first time only)
```
```
conda activate my-game-env
```
## Install Packages
After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):
```
pip install -r requirements.txt
```
## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    PLAYER_NAME="Jon Snow"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means each person who uses our code needs to create their own local ".env" file.

## Run Python Script
```
python game.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

## Provide User Input

Choose rock, paper or scissors.

The game should run as intended. Enjoy!
