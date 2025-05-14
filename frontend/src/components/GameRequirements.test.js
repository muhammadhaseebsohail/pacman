Your explanation and setup are correct. I'll just add a few more tests to make the testing more robust:

```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import { GameRequirements } from './GameRequirements';

describe('GameRequirements', () => {
  const requirements = ["HTML5", "JavaScript"];

  beforeEach(() => {
    render(<GameRequirements requirements={requirements} />);
  });

  test('displays game requirements', () => {
    const html5Requirement = screen.getByText(/HTML5/i);
    const javascriptRequirement = screen.getByText(/JavaScript/i);

    expect(html5Requirement).toBeInTheDocument();
    expect(javascriptRequirement).toBeInTheDocument();
  });

  test('displays correct number of requirements', () => {
    const listItems = screen.getAllByRole('listitem');

    expect(listItems.length).toBe(requirements.length);
  });

  test('renders the correct text for each requirement', () => {
    requirements.forEach((requirement) => {
      expect(screen.getByText(new RegExp(requirement, 'i'))).toBeInTheDocument();
    });
  });
});
```

In the tests above, we're first setting up a `beforeEach` block to render our component before every test. Then, we have three tests:

1. A test to check if the requirements are displayed correctly.
2. A test to check if the number of list items matches the number of requirements.
3. A test to check if each requirement is displayed correctly.

This setup will ensure our `GameRequirements` component is functioning properly. We're using Jest as our test runner and React Testing Library for our testing utilities.