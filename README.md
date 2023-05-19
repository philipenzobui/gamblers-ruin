# Gambler's Ruin and Simulations

Consider a coin-flipping game with two players with $p$ and $q = 1 - p$ chance of winning each round, respectively. After each round, the loser transfers one 
penny to the winner. The game ends when one player has all the pennies. Let the first and second player start with fortunes n<sub>1</sub> and n<sub>2</sub> pennies 
respectively, what is the probability of the first player winning?

This repository contains a theoretical [derivation](https://github.com/philipenzobui/gamblers-ruin/blob/main/GamblersRuin.pdf) for 
the answer to this popular problem and a [Python script](https://github.com/philipenzobui/gamblers-ruin/blob/main/GamblerRuinSimulations.py) to run simulations and
generate a visualization.

Here's a representation of 1,000,000 simulations for the probability of winning starting with n<sub>1</sub> = n<sub>2</sub> = 10 using the odds of European (single-zero)
and American (double-zero) style roulettes. The theoretical answers are P(European) = 0.36803 and P(American) = 0.25853.

<p align="center">
  <img src="https://github.com/philipenzobui/gamblers-ruin/assets/104658293/fa91d85d-5b6d-4b71-852f-79683373471e">
<p>
  
  
I mainly wrote this project as practice for LaTex syntax and some matplotlib specifics. 
  
Some interesting follow-up questions: what is the expectation of rounds for each game? What is the expectation of rounds in each game, knowing the first player won?
