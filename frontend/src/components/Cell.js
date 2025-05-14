Due to the nature of the task, I'll create a simple standalone game of Tic Tac Toe in React. It doesn't require any external login or server dependency and is completely client-side.

Here's the code:

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './TicTacToe.css';

// Cell component
const Cell = ({ value, onClick }) => (
  <button className="cell" onClick={onClick}>
    {value}
  </button>
);
Cell.propTypes = {
  value: PropTypes.string,
  onClick: PropTypes.func.isRequired,
};

// Board component
const Board = ({ squares, onClick }) => {
  return (
    <div className="board">
      {squares.map((square, i) => (
        <Cell key={i} value={square} onClick={() => onClick(i)} />
      ))}
    </div>
  );
};
Board.propTypes = {
  squares: PropTypes.arrayOf(PropTypes.string).isRequired,
  onClick: PropTypes.func.isRequired,
};

// Game component
const Game = () => {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [stepNumber, setStepNumber] = useState(0);
  const [xIsNext, setXisNext] = useState(true);
  const winner = calculateWinner(history[stepNumber]);

  const handleClick = (i) => {
    const historyPoint = history.slice(0, stepNumber + 1);
    const current = historyPoint[stepNumber];
    const squares = [...current];

    if (winner || squares[i]) return;

    squares[i] = xIsNext ? 'X' : 'O';
    setHistory([...historyPoint, squares]);
    setStepNumber(historyPoint.length);
    setXisNext(!xIsNext);
  };

  return (
    <div className="game">
      <Board squares={history[stepNumber]} onClick={handleClick} />
      <div className="info">
        <h3>{winner ? 'Winner: ' + winner : 'Next Player: ' + (xIsNext ? 'X' : 'O')}</h3>
      </div>
    </div>
  );
};

export default Game;

// Helper function to calculate the winner
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
```

The CSS file `TicTacToe.css`:

```css
.game {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.board {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.cell {
  width: 60px;
  height: 60px;
  background: #fff;
  border: 1px solid #000;
  font-size: 24px;
  font-weight: bold;
  line-height: 60px;
  text-align: center;
}
```

For testing, you can use Jest and React Testing Library:

```jsx
import { render, fireEvent } from '@testing-library/react';
import Game from './Game';

test('renders the game and allows to play', () => {
  const { getAllByRole, getByText } = render(<Game />);
  const cells = getAllByRole('button');

  fireEvent.click(cells[0]);
  fireEvent.click(cells[1]);
  fireEvent.click(cells[4]);
  fireEvent.click(cells[2]);
  fireEvent.click(cells[8]);

  expect(getByText('Winner: X')).toBeInTheDocument();
});
```