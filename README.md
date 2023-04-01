<p align="center">
  <img src="https://github.com/RamonFCerezo/Battleship/blob/main/img/Battleship.png" alt="Battleship game screenshot" style="display: block; margin: auto;">
</p>

<h1>Battleship</h1>

<p>Development of the game 'Battleship' using the Python programming language and its Numpy library. This is also an approach to Object-Oriented Programming. The game will be developed within the Python console, as it does not have its own interface.</p>

<h2>Project Structure</h2>
<p>This project consists of 4 Python executable files:</p>
<ol>
  <li><strong>main.py &#8594; </strong> Executable of the game, contains the presentation messages, coordinate inputs, and the main logic of the game.</li>
  <li><strong>functions.py:</strong>
    <ul>
      <li>random_boats_generator &#8594; Creates new boats of a specified size and validates them in their board</li>
      <li>list_of_contiguous &#8594; Takes the previously generated boat and returns a list with the contiguous locations of it, including the boat locations</li>
      <li>boat_placing &#8594; Places the new boat in the board depending on the player, replacing the empty space for an "O" in the index of the Np.array</li>
      <li>shoot &#8594; Function that allows both players to shoot one spot of the opponent's board. If the shot hits a boat, the player who did it keeps the turn. Otherwise, it will change. Will print the both shots and boats board in each turn</li>
    </ul>
  <li><strong>classes.py &#8594; </strong></li>
  <li><strong>variables.py &#8594; </strong></li>
</ol>
