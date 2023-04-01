<p align="center">
  <img src="https://github.com/RamonFCerezo/Battleship/blob/main/img/Battleship.png" alt="Battleship game screenshot" style="display: block; margin: auto;">
</p>

<h1>Battleship</h1>

<p>Development of the game 'Battleship' using the Python programming language and its Numpy library. This is also an approach to Object-Oriented Programming. The game will be developed within the Python console, as it does not have its own interface.</p>

<h2>Project Structure</h2>
<p>This project consists of 4 Python executable files:</p>
<ol>
  <li><strong>main.py</strong> &#8594; Executable of the game, contains the presentation messages, coordinate inputs, and the main logic of the game.</li>
  <li>functions.py &#8594;
    <ul>
      <li>random_boats_generator &#8594; Function that creates new boats of a specified size and validates them in their board</li>
      <li>list_of_contiguous &#8594; Function that takes the previously generated boat and returns a list with all the contiguous locations of it. The list includes the boat locations too</li>
      <li>boat_placing</li> &#8594; Function that places the new boat in the board depending on the player, replacing the empty space for an "O" in the index of the np.array</li>
    </ul>
  <li>classes.py &#8594; </li>
  <li>variables.py &#8594; </li>
</ol>
