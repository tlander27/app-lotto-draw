import streamlit as st
from random import Random


def get_numbers(game):
    """ Generates random numbers for Powerball and MegaMillions
    :param game: Draw game determined by selectbox
    :return: list of 5 numbers, power/mega ball
    """
    draws = []
    if game == "Powerball":
        numbers = list(range(1, 66))
        local_ball = Random().randrange(1, 27)
    else:
        numbers = list(range(1, 65))
        local_ball = Random().randrange(1, 27)

    for i in range(5):
        draw = Random().choice(numbers)
        numbers.remove(draw)
        draws.append(draw)
    return draws, local_ball


st.title("Lottery Number Generator")

options = ["Powerball", "Mega Millions"]
game = st.selectbox("Select a draw game".title(), options)
button = st.button("Get Numbers")

if button:
    results, ball = get_numbers(game)
    results.sort()
    st.subheader(f"{results[0]} {results[1]} {results[2]} {results[3]} {results[4]} - {ball}")
