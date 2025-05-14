Component Code:

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import styles from './GameScore.module.css';

/**
 * GameScore component displays the score and remaining lives of the user.
 * 
 * @param {object} props - Component props
 * @param {number} props.score - Current game score
 * @param {number} props.lives - Current number of remaining lives
 */
function GameScore({ score, lives }) {
    return (
        <div className={styles.container}>
            <div className={styles.score}>
                Score: {score}
            </div>
            <div className={styles.lives}>
                Lives: {lives}
            </div>
        </div>
    );
}

GameScore.propTypes = {
    score: PropTypes.number.isRequired,
    lives: PropTypes.number.isRequired,
};

export default GameScore;
```

CSS/Styling:

```css
/* GameScore.module.css */

.container {
    display: flex;
    justify-content: space-between;
    padding: 20px;
    background-color: #f3f3f3;
}

.score, .lives {
    font-size: 1.2em;
    font-weight: bold;
}
```

PropTypes or TypeScript interfaces:

```jsx
GameScore.propTypes = {
    score: PropTypes.number.isRequired,
    lives: PropTypes.number.isRequired,
};
```

Basic unit test setup:

```jsx
// GameScore.test.js

import React from 'react';
import { render } from '@testing-library/react';
import GameScore from './GameScore';

test('renders GameScore', () => {
    const { getByText } = render(<GameScore score={100} lives={3} />);
    const scoreElement = getByText(/Score: 100/i);
    const livesElement = getByText(/Lives: 3/i);
    expect(scoreElement).toBeInTheDocument();
    expect(livesElement).toBeInTheDocument();
});
```