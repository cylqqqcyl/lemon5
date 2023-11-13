import React from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import {
  Box,
  Container,
  Stack,
  Typography,
  Button,
  useMediaQuery,
  useTheme,
} from '@mui/material';
import { Layout as DashboardLayout } from 'src/layouts/dashboard/layout';
import { Logo } from 'src/components/logo';
import TextBubbleIcon from '@heroicons/react/24/solid/ChatBubbleBottomCenterTextIcon';
import ConverseIcon from '@heroicons/react/24/solid/ArrowsRightLeftIcon';
import ChatIcon from '@heroicons/react/24/solid/SparklesIcon';
import io from 'socket.io-client';

//----------------button style----------------
const glassStyle = {
  backgroundColor: 'rgba(237, 216, 61, 0.7)', // semi-transparent white
  backdropFilter: 'blur(10px)', // blur effect on the background
  border: '5px solid primary', // subtle white border
  boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)', // soft shadow for depth
  color: 'neutral.600', // text color for contrast
  '&:hover': {
    backgroundColor: 'rgba(237, 216, 61, 0.2)', // slightly more opaque on hover
    boxShadow: '0 6px 8px rgba(0, 0, 0, 0.15)', // deeper shadow on hover
  },
};
//---------------button style----------------
  
const Page = () => {
  const theme = useTheme(); // Access the theme object
  const lgUp = useMediaQuery((theme) => theme.breakpoints.up('lg'));
  const router = useRouter();
  const logos = lgUp ? [...Array(15).fill(0)] : [...Array(20).fill(0)]; // Number of logos to display


  const navigateTo = (path) => {
    router.push(path);  // Navigate to the given path
  };

  return (
    <>
      <Head>
        <title>Lemon5 | AI语音平台</title>
      </Head>
      <Container>
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            height: '100vh',
          }}
        >
          {/* Logo grid */}
          <Box sx={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            zIndex: -1,
          }}>
            <Box sx={{
            display: 'grid',
            gridTemplateColumns: 'repeat(5, 1fr)', // Adjust the grid layout as needed
            gap: 2, // Space between logos
            opacity: 0.3, // Make logos more subtle
          }}>
            {logos.map((_, index) => (
              <Logo key={index} sx={{ width: 10, height: 10 }} /> // Adjust logo size
              ))}
          </Box>
        </Box>

          <Typography variant="h1" 
          gutterBottom
            sx={{
              background: `linear-gradient(270deg, 
                ${theme.palette.neutral[500]}, ${theme.palette.neutral[50]}, ${theme.palette.neutral[800]})`,
              backgroundSize: '600% 600%',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              animation: 'colorWave 8s ease infinite',
             '@keyframes colorWave': {
                '0%':{
                  'background-position': '0% 50%',
                },
                '50%':{
                  'background-position': '100% 50%',
                },
                '100%':{
                  'background-position': '0% 50%',
                }
              },
              userSelect: 'none',
            }}
          >
            欢迎来到 Lemon5 AI语音平台
          </Typography>
          <Stack direction="row" 
          spacing={2} sx={{ mt:5 ,width: '50%', justifyContent: 'center' }}>
            <Button
              variant="contained"
              color="primary"
              onClick={() => navigateTo('/tts')}
              startIcon={<TextBubbleIcon style={{ width: '24px', height: '24px' }} />}
              sx={{ minWidth: 150, ...glassStyle }}
            >
              文本转语音
            </Button>
            <Button
              variant="contained"
              color="secondary"
              onClick={() => navigateTo('/vc')}
              startIcon={<ConverseIcon style={{ width: '24px', height: '24px' }} />}
              sx={{ minWidth: 150, ...glassStyle }}
            >
              语音转换
            </Button>
            <Button
              variant="contained"
              color="info"
              onClick={() => navigateTo('/chat')}
              startIcon={<ChatIcon style={{ width: '24px', height: '24px' }} />}
              sx={{ minWidth: 150, ...glassStyle }}
            >
              语音对话
            </Button>
          </Stack>
        </Box>
      </Container>
    </>
  );
};

Page.getLayout = (page) => (
  <DashboardLayout>
    {page}
  </DashboardLayout>
);

export default Page;