import React, { useEffect, useRef } from 'react';
import { Box } from '@mui/material';
import Spline from '@splinetool/react-spline';

const SoundWaveBox = ({ children, ...rest }) => {
  const splineRef = useRef(null);

  return (
    <Box {...rest}>
      {children}
      <Spline scene="https://prod.spline.design/kxb7ox6EwX2yMKEZ/scene.splinecode" />
      {/* Overlay to disable mouse interaction */}
      <Box
        position="absolute"
        top={0}
        left={0}
        right={0}
        bottom={0}
        zIndex={1}
        style={{ cursor: 'default' }}
      ></Box>
    </Box>
  );
};

export default SoundWaveBox;
