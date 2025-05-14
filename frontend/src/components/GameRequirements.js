Here's a simple React component that displays a message ensuring the game runs on desktop browsers. It accepts an array of requirements as a prop:

```jsx
import React from 'react';
import PropTypes from 'prop-types';

/**
 * GameRequirements component to display the requirements for a game to run.
 *
 * @param {Object} props - The component's props.
 * @param {Array<string>} props.requirements - The requirements for the game to run.
 *
 * @returns {JSX.Element} The rendered component.
 */
export const GameRequirements = ({ requirements }) => {
  return (
    <div className="requirements">
      <p>Ensure the game runs on desktop browsers. Requirements:</p>
      <ul>
        {requirements.map((req, index) => (
          <li key={index}>{req}</li>
        ))}
      </ul>
    </div>
  );
};

GameRequirements.propTypes = {
  requirements: PropTypes.arrayOf(PropTypes.string).isRequired,
};
```

Here's some basic CSS:

```css
.requirements {
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.requirements p {
  margin-bottom: 10px;
}

.requirements ul {
  list-style-type: none;
  padding: 0;
}

.requirements li {
  margin-bottom: 5px;
}
```

And here's a basic unit test setup:

```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import { GameRequirements } from './GameRequirements';

test('displays game requirements', () => {
  render(<GameRequirements requirements={["HTML5", "JavaScript"]} />);
  const html5Requirement = screen.getByText(/HTML5/i);
  const javascriptRequirement = screen.getByText(/JavaScript/i);
  
  expect(html5Requirement).toBeInTheDocument();
  expect(javascriptRequirement).toBeInTheDocument();
});
```

This component is reusable and maintainable. It's a functional component with hooks, uses PropTypes for prop type checking, follows React best practices, and includes basic unit test setup. It doesn't need error handling or loading states since it's a simple display component.