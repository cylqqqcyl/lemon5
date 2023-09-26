import React from 'react';
import { Box } from '@mui/material';
import Spline from '@splinetool/react-spline';

const SoundWaveBox = ({ children, ...rest }) => {
  return (
    <Box {...rest}>
      {children}
      <Spline scene="https://prod.spline.design/ZE8hYurl0cBj1KS9/scene.splinecode" />
    </Box>
  );
};

export default SoundWaveBox;
