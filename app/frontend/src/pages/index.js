import React from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import {
  Box,
  Container,
  Stack,
  Typography,
  Button,
  Link,
  Divider,
  useTheme,
} from '@mui/material';
import { Layout as DashboardLayout } from 'src/layouts/dashboard/layout';
import { Logo } from 'src/components/logo';
import TextBubbleIcon from '@heroicons/react/24/solid/ChatBubbleBottomCenterTextIcon';
import ConverseIcon from '@heroicons/react/24/solid/ArrowsRightLeftIcon';
import ChatIcon from '@heroicons/react/24/solid/SparklesIcon';
import io from 'socket.io-client';

//----------------heart beat----------------

// Connect to the socket.io server
// const socket = io('http://localhost:8080'); // Connect to the socket.io server

// let lastHeartbeat = Date.now(); // Initialize the lastHeartbeat variable with the current time

// socket.on('heartbeat', (data) => {
//   console.log('Received heartbeat:', data);
//   lastHeartbeat = Date.now(); // Update the lastHeartbeat variable with the current time
// });

// setInterval(() => {
//   const now = Date.now();
//   const timeSinceLastHeartbeat = now - lastHeartbeat; // Calculate the time since the last heartbeat
//   if (timeSinceLastHeartbeat > 20000) { // If it has been more than 20 seconds since the last heartbeat
//     socket.connect(); // Attempt to reconnect
//   }
// }, 10000); // Check every 10 seconds

//----------------heart beat----------------
  
const Page = () => {
const theme = useTheme(); // Access the theme object
  const router = useRouter();

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
          {/* Logo */}
          <Box
            sx={{
              position: 'absolute',
              zIndex: -1,
              top: 70,
              opacity: 0.3,
            }}
          >
            <Logo />
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
            <Box display="flex" 
            flexDirection="column" alignItems="center" justifyContent="center"
            sx={{ width: '100%'}}>
            <Button variant="contained" 
            color="info" onClick={() => navigateTo('/tts')} 
            startIcon={<TextBubbleIcon style={{ width: '24px', height: '24px' }} />}>
                文本转语音
              </Button>
            </Box>
            <Box display="flex" 
            flexDirection="column" alignItems="center" justifyContent="center"
            sx={{ width: '100%'}}>
            <Button variant="contained" 
            color="info" onClick={() => navigateTo('/vc')}
            startIcon={<ConverseIcon style={{ width: '24px', height: '24px' }} />}>
                语音转换
              </Button>
            </Box>
            <Box display="flex" 
            flexDirection="column" alignItems="center" justifyContent="center"
            sx={{ width: '100%'}}>
            <Button variant="contained" 
            color="info" onClick={() => navigateTo('/chat')}
            startIcon={<ChatIcon style={{ width: '24px', height: '24px' }} />}>
                语音对话
              </Button>
            </Box>
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