import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import BellIcon from '@heroicons/react/24/solid/BellIcon';
import UserIcon from '@mui/icons-material/Person';
import Bars3Icon from '@heroicons/react/24/solid/Bars3Icon';
import {
  Avatar,
  Badge,
  Box,
  IconButton,
  Stack,
  SvgIcon,
  Tooltip,
  useMediaQuery,
} from '@mui/material';
import { alpha } from '@mui/material/styles';
import { usePopover } from 'src/hooks/use-popover';
import { AccountPopover } from './account-popover';
import { NotificationPopover } from './notification-popover';
import { useRouter } from 'next/router';
import { useState } from 'react';
import io from 'socket.io-client';

const socket = io(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api`, {
  reconnection: true,       // whether to automatically attempt to reconnect
  reconnectionAttempts: 5,  // number of reconnection attempts before giving up
  reconnectionDelay: 1000,  // how long to initially wait before attempting a new reconnection
  reconnectionDelayMax: 5000, // maximum amount of time to wait between reconnection attempts
  randomizationFactor: 0.5  // randomization factor for the reconnection delay
});



const SIDE_NAV_WIDTH = 180;
const TOP_NAV_HEIGHT = 64;

export const TopNav = (props) => {
  const { onNavOpen } = props;
  const lgUp = useMediaQuery((theme) => theme.breakpoints.up('lg'));
  const accountPopover = usePopover(); 
  const notificationPopover = usePopover();
  const [hasNotification, setHasNotification] = useState(false);
  const [notifications, setNotifications] = useState([]);

  socket.on('connect', () => {
    console.log('Connected to the server');
  });
  
  socket.on('disconnect', () => {
    console.log('Disconnected from the server');
  });
  
  socket.on('reconnect_attempt', (attemptNumber) => {
    console.log(`Reconnect attempt ${attemptNumber}`);
  });

  useEffect(() => {
    // Listen for 'new_notification' event from the server
    socket.on('notification', (notification) => {
      setNotifications([notification, ...notifications]);
      setHasNotification(true);
    });

    return () => {
      socket.off('new_notification');
    };
  }, []);


  const handleNotificationClick = async () => {
    setHasNotification(false);
    notificationPopover.handleOpen();
  };


  return (
    <>
      <Box
        component="header"
        sx={{
          backdropFilter: 'blur(6px)',
          backgroundColor: (theme) => alpha(theme.palette.background.default, 0.1),
          position: 'sticky',
          left: {
            lg: `${SIDE_NAV_WIDTH}px`
          },
          top: 0,
          width: 
          {
            lg: `calc(100% - ${SIDE_NAV_WIDTH}px)`
          },
          zIndex: (theme) => theme.zIndex.appBar
        }}
      >
        <Stack
          alignItems="center"
          direction="row"
          justifyContent="space-between" // Change to 'flex-end' to align items to the right
          spacing={2}
          sx={{
            minHeight: TOP_NAV_HEIGHT,
            width: '100%',
            px: 0,
            pr:1
          }}
        >
          <Stack
            alignItems="center"
            direction="row"
            spacing={2}
            sx={{
              ml: 1,
            }}
          >
          {!lgUp && (
              <IconButton onClick={onNavOpen}>
                <SvgIcon fontSize="small">
                  <Bars3Icon />
                </SvgIcon>
              </IconButton>
            )}
          </Stack>
          <Stack
            alignItems="center"
            direction="row"
            spacing={2}
            sx={{
              mr: 1,
            }}
          >
            <Tooltip title="消息">
            <IconButton onClick={handleNotificationClick}
              ref={notificationPopover.anchorRef}
            >
              <Badge
                badgeContent={hasNotification ? 1 : 0} // 如果有通知则显示小点，否则不显示
                color="success"
                variant="dot"
              >
                <SvgIcon fontSize="small">
                  <BellIcon />
                </SvgIcon>
              </Badge>
            </IconButton>
          </Tooltip>
            <Avatar
              onClick={accountPopover.handleOpen}
              ref={accountPopover.anchorRef}
              sx={{
                cursor: 'pointer',
                height: 30,
                width: 30,
                bgcolor: 'primary.main'
              }}
            >
              <UserIcon />
            </Avatar>
          </Stack>
        </Stack>
      </Box>
      <AccountPopover
        anchorEl={accountPopover.anchorRef.current}
        open={accountPopover.open}
        onClose={accountPopover.handleClose}
      />
      <NotificationPopover
        anchorEl={notificationPopover.anchorRef.current}
        open={notificationPopover.open}
        onClose={notificationPopover.handleClose}
        notifications={notifications}
      />
    </>
  );
};

TopNav.propTypes = {
  onNavOpen: PropTypes.func
};
