import React from 'react';
import PropTypes from 'prop-types';
import NextLink from 'next/link';
import { Box, Typography, Unstable_Grid2 as Grid } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { alpha } from '@mui/system';  // Import alpha for gradient
import { Logo } from 'src/components/logo';
import SoundWaveBox from 'src/sections/login/soundwave-background';
// TODO: Change subtitle text

export const Layout = (props) => {
  const { children } = props;
  const theme = useTheme();

  return (
    <Box
      component="main"
      sx={{
        display: 'flex',
        flex: '1 1 auto'
      }}
    >
      <Grid
        container
        sx={{ flex: '1 1 auto' }}
      >
        <Grid
          xs={12}
          lg={6}
          sx={{
            backgroundColor: 'background.paper',
            display: 'flex',
            flexDirection: 'column',
            position: 'relative'
          }}
        >
          <Box
            component="header"
            sx={{
              left: 0,
              p: 3,
              position: 'static',
              top: 0,
              width: '100%',
              display: 'flex',  // Added flex display
              alignItems: 'center'  // Center items vertically
            }}
          >
            <Box
              component={NextLink}
              href="/"
              sx={{
                display: 'inline-flex',
                height: 40,
                width: 60
              }}
            >
              <Logo />
            </Box>
            <Typography
              variant="h6"
              sx={{
                marginLeft: 0,  // Add some left margin
                background: `linear-gradient(to right, 
                  ${alpha(theme.palette.primary.main, 1)}, ${alpha(theme.palette.primary.lightest, 1)})`,
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent'
              }}
            >
              lemon5
            </Typography>
          </Box>
          {children}
        </Grid>
        <Grid
          xs={12}
          lg={6}
          sx={{
            alignItems: 'center',
            color: 'black',
            display: 'flex',
            justifyContent: 'center',
            '& img': {
              maxWidth: '100%'
            }
          }}
        >
          <SoundWaveBox sx={{ p: 3 }}>
            <Typography
              align="center"
              color="inherit"
              sx={{
                fontSize: '24px',
                lineHeight: '32px',
                mb: 1
              }}
              variant="h1"
            >
              欢迎登录{' '}
              <Box
                component="a"
                sx={{ color: '#A0D189' }}
                target="_blank"
              >
                lemon5
              </Box>
            </Typography>
            <Typography
              align="center"
              sx={{ mb: 3 }}
              variant="subtitle1"
            >
              lemon5 AI语音平台
            </Typography>
          </SoundWaveBox>
        </Grid>
      </Grid>
    </Box>
  );
};

Layout.prototypes = {
  children: PropTypes.node
};