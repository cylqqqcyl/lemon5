import React from 'react';
import { useCallback } from 'react';
import { useRouter } from 'next/navigation';
import PropTypes from 'prop-types';
import { Box, Popover, Divider, Typography, List, ListItem, ListItemText } from '@mui/material';

export const NotificationPopover = (props) => {
  const { anchorEl, onClose, open, notifications } = props;

  return (
    <Popover
      anchorEl={anchorEl}
      anchorOrigin={{
        horizontal: 'left',
        vertical: 'bottom'
      }}
      onClose={onClose}
      open={open}
      PaperProps={{ sx: { width: 250 } }} // Adjust the width as needed
    >
      <Box
        sx={{
          py: 1.5,
          px: 2
        }}
      >
        <Typography variant="overline">
          消息
        </Typography>
      </Box>
      <Divider />
      <List
        sx={{
          p: 0,
          maxHeight: 300, // Set a maximum height
          overflow: 'auto' // Add scrolling for long lists
        }}
      >
        {notifications.map((notification, index) => (
          <ListItem key={index} sx={{ py: 1 }}>
            <ListItemText
              primary={notification.message}
              secondary={notification.time}
              secondaryTypographyProps={{
                variant: 'body2',
                color: 'text.secondary'
              }}
            />
          </ListItem>
        ))}
      </List>
    </Popover>
  );
};

NotificationPopover.propTypes = {
  anchorEl: PropTypes.any,
  notifications: PropTypes.arrayOf(PropTypes.shape({
    message: PropTypes.string.isRequired,
    time: PropTypes.string.isRequired
  })).isRequired,
  onClose: PropTypes.func,
  open: PropTypes.bool.isRequired
};
