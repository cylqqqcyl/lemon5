import React from 'react';
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
import { useRouter } from 'next/router';
import { useState } from 'react';

const SIDE_NAV_WIDTH = 180;
const TOP_NAV_HEIGHT = 64;

export const TopNav = (props) => {
  const { onNavOpen } = props;
  const lgUp = useMediaQuery((theme) => theme.breakpoints.up('lg'));
  const accountPopover = usePopover(); 
  const router = useRouter();
  const [hasNotification, setHasNotification] = useState(true); // 初始设定有通知

  const handleNotificationClick = () => {
    setHasNotification(false); // 点击后设定没有通知
    
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
            <IconButton onClick={handleNotificationClick}>
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
    </>
  );
};

TopNav.propTypes = {
  onNavOpen: PropTypes.func
};
