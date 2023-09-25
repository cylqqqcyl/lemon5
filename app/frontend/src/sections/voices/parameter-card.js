import React, { useState } from 'react';
import { Card, Typography, Slider } from '@mui/material';

export const ParameterCard = ({ description, min, max, step, defaultValue, onChange }) => {
  const [sliderValue, setSliderValue] = useState(defaultValue);

  const handleSliderChange = (event, newValue) => {
    setSliderValue(newValue);
    if (onChange) {
      onChange(newValue);
    }
  };

  return (
    <Card sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', p: 2,mt:2 }}>
      <Typography variant="body1" sx={{ flex: 1, fontWeight:'bold' }}>
        {description}
      </Typography>
      <Slider
        value={sliderValue}
        min={min}
        max={max}
        step={step}
        onChange={handleSliderChange}
        sx={{ flex: 2 }}
      />
      <Typography variant="body1" sx={{ flex: 1, textAlign: 'right',mr:2, fontWeight:'bold' }}>
        {sliderValue}
      </Typography>
    </Card>
  );
};
