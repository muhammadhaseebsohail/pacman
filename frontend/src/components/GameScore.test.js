You got it right. The unit test you have set up checks if the GameScore component is rendered correctly with the correct props. Here's how you can expand on that test to check for prop changes:

```jsx
// GameScore.test.js

import React from 'react';
import { render, cleanup } from '@testing-library/react';
import GameScore from './GameScore';

// Clean up after each test
afterEach(cleanup);

test('renders GameScore and checks for prop changes', () => {
    const { getByText, rerender } = render(<GameScore score={100} lives={3} />);
    let scoreElement = getByText(/Score: 100/i);
    let livesElement = getByText(/Lives: 3/i);
    expect(scoreElement).toBeInTheDocument();
    expect(livesElement).toBeInTheDocument();

    // Re-render the same component with different props
    rerender(<GameScore score={200} lives={2} />);
    scoreElement = getByText(/Score: 200/i);
    livesElement = getByText(/Lives: 2/i);
    expect(scoreElement).toBeInTheDocument();
    expect(livesElement).toBeInTheDocument();
});
```

This test checks if the GameScore component correctly updates when the props (score and lives) change. It first renders the component with a score of 100 and 3 lives, then re-renders it with a score of 200 and 2 lives. The test checks if the component correctly displays the updated props.
