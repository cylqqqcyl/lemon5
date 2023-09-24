import React, {useState} from 'react';
import Head from 'next/head';
import {
  Box,
  Container,
  Stack,
  SvgIcon,
  Typography,
  Button,
  CircularProgress,
  Divider
} from '@mui/material';
import { Layout as DashboardLayout } from 'src/layouts/dashboard/layout';
import { VoicesSearch } from 'src/sections/voices/voices-search';
import { VoicesSelect } from 'src/sections/voices/voices-select';
import { VoicesText } from 'src/sections/voices/voices-text';
import { GeneratedGrid } from 'src/sections/voices/generated-grid';
import io from 'socket.io-client';
import TextBubbleIcon from '@heroicons/react/24/solid/ChatBubbleBottomCenterTextIcon';


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
  const [voiceCardSelected, setVoiceCardSelected] = useState(null);
  const [textInput, setTextInput] = useState('');
  const [isLoading, setIsLoading] = useState(false); // New state for loading
  const [generatedCards, setGeneratedCards] = useState([]); // New state for generated cards

  // const handleButtonClick = () => {
  //   let id = 0;
  //   setIsLoading(true);
  //   // logic here,
  //   // After the operation is complete, set isLoading back to false
  //   // setIsLoading(false);
  //   const newCard = {
  //     id: id++,
  //     voice: voiceCardSelected,
  //     text: textInput
  //   };
  //   setTimeout(() => setIsLoading(false), 2000); //delay 2s debug
  //   setGeneratedCards([newCard, ...generatedCards]); // Add new card at the beginning
  // };
  const handleButtonClick = async () => {
    console.log(voiceCardSelected, textInput);
    setIsLoading(true);
  
    try {
      const response = await fetch('https://10ed6d77.r7.cpolar.top/tts?text=' + textInput + '&lang=ja', {
        method: 'GET'
      });
  
      if (response.ok) {
        const audioBlob = await response.blob();
        const audioUrl = URL.createObjectURL(audioBlob);
        console.log('audio_path', audioUrl)
        
        const newCard = {
          id: Date.now(), // 使用时间戳作为 id 可能更好
          voice: voiceCardSelected,
          text: textInput,
          audioUrl: audioUrl // 将音频 URL 保存到卡片中
        };
  
        setGeneratedCards([newCard, ...generatedCards]);
      } else {
        // 处理错误响应，例如显示一个错误消息
        console.error('Error fetching audio:', response.statusText);
      }
    } catch (error) {
      console.error('There was an error:', error);
    }
  
    setIsLoading(false);
  };
  

  return(
  <>
    <Head>
      <title>
        Lemon5 | 文本转语音
      </title>
    </Head>
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        py: 8
      }}
    >
      <Container maxWidth="xl">
        <Stack spacing={3}>
          <Stack
            direction="row"
            justifyContent="space-between"
            spacing={4}
          >
            <Stack spacing={1}>
              <Stack
                alignItems="center"
                direction="row"
                spacing={1}
              >
                <SvgIcon fontSize="large">
                  <TextBubbleIcon />
                </SvgIcon>
                <Typography variant="h4">
                  文本转语音
                </Typography>
              </Stack>
              <Stack
                alignItems="center"
                direction="row"
                spacing={1}
              >
                <Typography variant="body1"
                  sx={{
                    color: 'text.secondary'
                  }}
                >
                  选择音色，输入文本，生成高质量语音
                </Typography>
              </Stack>
            </Stack>
          </Stack>
          <VoicesSearch />
          <VoicesSelect setVoiceCardSelected={setVoiceCardSelected} />
          <VoicesText voiceCardSelected={voiceCardSelected} setTextInput={setTextInput} />
          <Box sx={{ mt: 2, display: 'flex', justifyContent: 'center' }}>
            {isLoading ? (
              <CircularProgress color="success"  />
            ) : (
              <Button 
                variant="contained" 
                color="success" 
                onClick={() => {
                  console.log("Button definitely clicked!");
                  handleButtonClick();
                }} 
                disabled={!voiceCardSelected || !textInput}
                sx={{ width: '50%', borderRadius: '50px'}}>
                生成语音
              </Button>
            )}
          </Box>
          {generatedCards.length > 0 && (
            <>
            <Divider variant="middle" sx={{ my: 2, borderColor: 'neutral.300' }} />
            <Typography variant="h5">
              生成的语音
            </Typography>
            <GeneratedGrid generatedCards={generatedCards} />
           </>
          )}
        </Stack>
      </Container>
    </Box>
  </>
  )

};

Page.getLayout = (page) => (
  <DashboardLayout>
    {page}
  </DashboardLayout>
);

export default Page;
