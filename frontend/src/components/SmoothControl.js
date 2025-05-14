Sure, here is a simple example of a responsive and smooth controls component. This component will animate a square div from left to right smoothly when the right arrow key on the keyboard is pressed. 

The main component's code:

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './SmoothControl.css';

const SmoothControl = ({ speed }) => {
  const [left, setLeft] = useState(0);

  const handleKeyDown = (event) => {
    if (event.key === 'ArrowRight') {
      setLeft((prevLeft) => prevLeft + speed);
    }
  };

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  return <div className="box" style={{ transform: `translateX(${left}px)` }} />;
};

SmoothControl.propTypes = {
  speed: PropTypes.number,
};

SmoothControl.defaultProps = {
  speed: 10,
};

export default SmoothControl;
```

The CSS code:

```css
.box {
  width: 50px;
  height: 50px;
  background-color: red;
  position: absolute;
  top: 50%;
  left: 0;
  transition: transform 0.3s ease;
}
```

This component has propTypes defined for "speed" which is a number. By default, the speed is set to 10. 

Here is a simple test setup:

```jsx
import { render, fireEvent } from '@testing-library/react';
import SmoothControl from './SmoothControl';

test('checks if right arrow key moves the box', () => {
  const { getByRole } = render(<SmoothControl />);
  const box = getByRole('box');

  fireEvent.keyDown(window, { key: 'ArrowRight' });

  expect(box).toHaveStyle('transform: translateX(10px)');
});
```

This test checks if the box moves by 10px when the right arrow key is pressed. Please note that you will need to install 'jest-styled-components' to be able to test CSS in JS.