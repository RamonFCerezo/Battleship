<p align="center">
  <img src="https://github.com/RamonFCerezo/Battleship/blob/main/img/Battleship.png" alt="Battleship game screenshot" style="display: block; margin: auto;">
</p>

<p>Development of the game 'Battleship' using the Python programming language and its Numpy library. This is also an approach to Object-Oriented Programming. The game will be developed within the Python console, as it does not have its own interface.</p>

<h1>Project Structure</h1>
<p>This project consists of 4 Python executable files:</p>

<h2>main.py:</h2> 
<p>Executable of the game, contains the presentation messages, coordinate inputs, and the main logic of the game.</p>

<h2>functions.py:</h2>
  <ul>
    <li><strong>random_boats_generator</strong> &#8594; Creates new boats of a specified size and validates them in their board</li>
    <li><strong>list_of_contiguous</strong> &#8594; Takes the previously generated boat and returns a list with the contiguous locations of it, including the boat locations</li>
    <li><strong>boat_placing</strong> &#8594; Places the new boat in the board depending on the player, replacing the empty space for an "O" in the index of the np.array</li>
    <li><strong>shoot</strong> &#8594; Function that allows both players to shoot one spot of the opponent's board. If the shot hits a boat, the player who did it keeps the turn. Otherwise, it will change. Will print the both shots and boats board in each turn</li>
  </ul>
  <h2><strong>classes.py &#8594; </strong></h2>
  <h2><strong>variables.py &#8594; </strong></h2>
