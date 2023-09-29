import React, { useEffect, useRef } from 'react';
import { Box } from '@mui/material';
import Spline from '@splinetool/react-spline';

const SoundWaveBox = ({ children, ...rest }) => {
  const splineRef = useRef(null);

  return (
    <Box {...rest}>
      {children}
      <Spline scene="https://prod.spline.design/0aVrJbm7zSxlSlAR/scene.splinecode" />
    </Box>
  );
};

export default SoundWaveBox;
