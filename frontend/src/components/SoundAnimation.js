Here's a simple example of a React component that plays a sound file and displays an animation when clicked.

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './SoundAnimation.css';

// Simple sound and animation component
const SoundAnimation = ({ soundFile, animation }) => {
  const [isAnimating, setIsAnimating] = useState(false);

  const handleClick = () => {
    setIsAnimating(true);

    const audio = new Audio(soundFile);
    audio.play()
      .catch(error => {
        console.error('Error playing sound file:', error);
      });
  };

  const handleAnimationEnd = () => {
    setIsAnimating(false);
  };

  const animationClasses = `animation ${isAnimating ? 'animating' : ''}`;

  return (
    <div
      className={animationClasses}
      onClick={handleClick}
      onAnimationEnd={handleAnimationEnd}
      style={{ backgroundImage: `url(${animation})` }}
    />
  );
};

SoundAnimation.propTypes = {
  soundFile: PropTypes.string.isRequired,
  animation: PropTypes.string.isRequired,
};

export default SoundAnimation;
```

In this component, we use `useState` to keep track of whether the animation is currently running. When the user clicks on the component, we start the animation and play the sound. When the animation ends, we reset the state so it can be triggered again.

The CSS might look something like this:

```css
.animation {
  width: 100px;
  height: 100px;
  background-size: cover;
  cursor: pointer;
}

.animation.animating {
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

The PropTypes are already defined in the component, but here they are for reference:

```jsx
SoundAnimation.propTypes = {
  soundFile: PropTypes.string.isRequired,
  animation: PropTypes.string.isRequired,
};
```

To test this component, you might write something like this using Jest and React Testing Library:

```jsx
import { render, fireEvent } from '@testing-library/react';
import SoundAnimation from './SoundAnimation';

test('plays sound and animates on click', () => {
  const { getByTestId } = render(<SoundAnimation soundFile="test.mp3" animation="test.png" />);
  const component = getByTestId('sound-animation');

  fireEvent.click(component);

  expect(component).toHaveClass('animating');
});
```

Remember to add `data-testid="sound-animation"` to the component's root div in the actual component file for this test to work.