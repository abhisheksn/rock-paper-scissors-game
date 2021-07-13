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
Use Anaconda to create and activate a new virtual environment, perhaps called "my-first-env":
```
conda create -n my-game-env python=3.8 #(first time only)
```
```
conda activate my-game-env
```
## Install Packages
```
pip install -r requirements.txt
```
## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    PLAYER_NAME="Jon Snow"

## Run Python Script
```
python game.py
```
## Provide User Input

Choose rock, paper or scissors.

The game should run as intended. Enjoy!
