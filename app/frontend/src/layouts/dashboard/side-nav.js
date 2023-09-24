import React from 'react';
import NextLink from 'next/link';
import { usePathname } from 'next/navigation';
import PropTypes from 'prop-types';
import { alpha } from '@mui/system';  // Import alpha for gradient
import {
  Box,
  Divider,
  Drawer,
  Stack,
  Typography,
  useMediaQuery,
  useTheme
} from '@mui/material';
import { Logo } from 'src/components/logo';
import { Scrollbar } from 'src/components/scrollbar';
import { items } from './config';
import { SideNavItem } from './side-nav-item';

export const SideNav = (props) => {
  const { open, onClose } = props;
  const pathname = usePathname();
  const lgUp = useMediaQuery((theme) => theme.breakpoints.up('lg'));
  const theme = useTheme();

  const content = (
    <Scrollbar
      sx={{
        height: '100%',
        '& .simplebar-content': {
          height: '100%'
        },
        '& .simplebar-scrollbar:before': {
          background: 'neutral.400'
        }
      }}
    >
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          height: '100%',
        }}
      >
        <Box sx={{ p: 3 }}>
          <Box
            component={NextLink}
            href="/"
            sx={{
              display: 'inline-flex',
              
              height: 32,
              width: 32
            }}
          >
            <Logo />
          </Box>
          <Typography
            variant="h6"
            sx={{
              marginLeft: 0,  // Add some left margin
              background: `linear-gradient(to right, 
                ${alpha(theme.palette.primary.main, 1)}, ${alpha(theme.palette.primary.lightest, 0.4)})`,
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent'
            }}
          >
            lemon5
          </Typography>

          <Typography
            variant="h6"
            sx={{
              marginLeft: 0,  // Add some left margin
              marginTop: 1,
              background: `linear-gradient(to right, 
                ${alpha(theme.palette.neutral[50], 1)}, ${alpha(theme.palette.neutral[50], 0.4)})`,
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent'
            }}
          >
            AI语音平台
          </Typography>
        </Box>
        <Divider sx={{ borderColor: 'neutral.700' }} />
        <Box
          component="nav"
          sx={{
            flexGrow: 1,
            px: 0,
            py: 0,
            display: 'flex',  // Enable flexbox layout
            flexDirection: 'column',  // Set direction to column
            justifyContent: 'space-evenly',  // Space items evenly
            alignItems: 'center'  // Center items horizontally
          }}
        >
          <Stack
            component="ul"
            spacing={0.5}
            alignItems="center"
            direction="column"
            justifyContent="space-evenly"
            sx={{
              listStyle: 'none',
              p: 0,
              m: 0,
              display: 'flex',
              flexGrow: 1
            }}
          >
            {items.map((item) => {
              const active = item.path ? (pathname === item.path) : false;

              return (
                <SideNavItem
                  active={active}
                  disabled={item.disabled}
                  external={item.external}
                  icon={item.icon}
                  key={item.title}
                  path={item.path}
                  title={item.title}
                  sx={{flexGrow: 1,
                    flexBasis: 0,}}
                />
              );
            })}
          </Stack>
        </Box>
        <Divider sx={{ borderColor: 'neutral.700' }} />
      </Box>
    </Scrollbar>
  );

  if (lgUp) {
    return (
      <Drawer
        anchor="left"
        open
        PaperProps={{
          sx: {
            backgroundColor: 'neutral.800',
            color: 'neutral.50',
            width: 180,
            borderRight: 0
          },
          elevation: 0, 
          square: true  
        }}
        variant="permanent"
      >
        {content}
      </Drawer>
    );
  }

  return (
    <Drawer
      anchor="left"
      onClose={onClose}
      open={open}
      PaperProps={{
        sx: {
          backgroundColor: 'neutral.800',
          color: 'neutral.50',
          width: 180,
          borderRight: 0
        },
  
      }}
      sx={{ zIndex: (theme) => theme.zIndex.appBar + 100 }}
      variant="temporary"
    >
      {content}
    </Drawer>
  );
};

SideNav.propTypes = {
  onClose: PropTypes.func,
  open: PropTypes.bool
};
