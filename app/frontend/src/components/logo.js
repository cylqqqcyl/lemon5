import React from 'react';
import { useTheme } from '@mui/material/styles';

export const Logo = () => {
  const theme = useTheme();
  const fillColor = theme.palette.primary.main;

  return (
    <svg
    
    xmlns="http://www.w3.org/2000/svg"
    width='100%'
    height='100%'
    viewBox="0 0 326 275"
  >
    <path 
    d="M225 12v8h-16v16h-16v16H81v16H49v16H33v32H17v32H1v112h16v15h112v-15h32v-16h16v-16h16v-16h32v16h16v-16h16v-16h16v-16h16v-48h-16V84h16V68h16V52h16V20h-16V4h-80v8zm48 16v8h-16v16h-32v16h-16v112h-16v32h-16v16h-16v16h-32v16H17V148h16v-32h16V84h32V68h128V36h16V20h48v8zm-16 80v8h-16v96h-16V100h32v8z"
    fill={fillColor}
    />
    
  </svg>
  );
};