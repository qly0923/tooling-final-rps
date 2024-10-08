# Rock-Paper-Scissors Game App

This is a simple **Rock-Paper-Scissors** game built with Python and Streamlit. The app allows users to play the classic game against the computer, which randomly selects rock, paper, or scissors. The app also tracks and displays the results.

## Features

- User can choose between **rock**, **paper**, or **scissors**.
- The computer makes a random selection.
- The app shows the result of each round, indicating if the player won, lost, or tied.
- Simple and intuitive user interface built using **Streamlit**.

## How to Play

1. **Choose** rock, paper, or scissors by selecting the respective option on the screen.
2. **Submit** your choice and the app will reveal the computer's choice.
3. The result (Win/Lose/Tie) is displayed immediately.

## Installation

```bash
git clone https://github.com/qly0923/tooling-final-rps.git

docker build -t streamlit .

docker run -p 8501:8501 streamlit
```
