import React from 'react';
import PropTypes from 'prop-types';
import { styled, alpha } from '@mui/material/styles';
import { a } from '@react-spring/web';

const WordPillRoot = styled('span')(({ theme, ownerState }) => {
  //find the color in the theme palette, if it's not there, use the default alpha12
  const backgroundColor =  theme.palette[ownerState.color]
    ? theme.palette[ownerState.color].alpha12
    : alpha(ownerState.color, 0.12);
  const color = theme.palette[ownerState.color]
    ? theme.palette[ownerState.color].main
    : ownerState.color;

  return {
    alignItems: 'center',
    backgroundColor,
    borderRadius: 12,
    border: `2px solid ${color}`,
    color,
    cursor: 'default',
    display: 'inline-flex',
    flexGrow: 1,
    flexShrink: 0,
    fontFamily: theme.typography.fontFamily,
    fontSize: theme.typography.pxToRem(12),
    lineHeight: 2,
    fontWeight: 600,
    justifyContent: 'center',
    letterSpacing: 0.5,
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(2),
    textTransform: 'uppercase',
    whiteSpace: 'nowrap',
    marginLeft: theme.spacing(1),
  };
});

export const WordPill = (props) => {
  const { color = 'primary', children, ...other } = props;

  const ownerState = { color };

  return (
    <WordPillRoot
      ownerState={ownerState}
      {...other}
    >
      {children}
    </WordPillRoot>
  );
};

WordPill.propTypes = {
  children: PropTypes.node,
  color: PropTypes.oneOf([
    'primary',
    'secondary',
    'error',
    'info',
    'warning',
    'success'
  ])
};
