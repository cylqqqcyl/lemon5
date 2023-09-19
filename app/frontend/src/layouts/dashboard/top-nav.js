import PropTypes from 'prop-types';
import BellIcon from '@heroicons/react/24/solid/BellIcon';
import UserIcon from '@mui/icons-material/Person';
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
    router.push('/logs');
  };

  return (
    <>
      <Box
        component="header"
        sx={{
          backgroundColor: 'transparent',
          position: 'absolute', // Change from 'sticky' to 'absolute'
          right: 0, // Add this to align the header to the right
          top: 0,
          width: 92,
          zIndex: (theme) => theme.zIndex.appBar
        }}
      >
        <Stack
          alignItems="center"
          direction="row"
          justifyContent="flex-end" // Change to 'flex-end' to align items to the right
          spacing={2}
          sx={{
            minHeight: TOP_NAV_HEIGHT,
            px: 0,
            pr:1
          }}
        >
          <Stack
            alignItems="center"
            direction="row"
            spacing={2}
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
