import React from 'react';
import PropTypes from 'prop-types';
import { styled } from '@mui/material/styles';

const WordPillRoot = styled('span')(({ theme, ownerState }) => {
  const backgroundColor = theme.palette[ownerState.color].alpha12;
  const color = theme.palette.mode === 'dark'
    ? theme.palette[ownerState.color].main
    : theme.palette[ownerState.color].dark;

  return {
    alignItems: 'center',
    backgroundColor,
    borderRadius: 12,
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
