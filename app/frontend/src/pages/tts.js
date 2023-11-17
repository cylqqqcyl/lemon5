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
import { CustomSnackbar } from 'src/sections/message/custom-snackbar';
import TextBubbleIcon from '@heroicons/react/24/solid/ChatBubbleBottomCenterTextIcon';
  
const Page = () => {
  const [voiceCardSelected, setVoiceCardSelected] = useState(null);
  const [searchText, setSearchText] = useState('');
  const [textInput, setTextInput] = useState('');
  const [isLoading, setIsLoading] = useState(false); // New state for loading
  const [generatedCards, setGeneratedCards] = useState([]); // New state for generated cards
  const [snackbarConfig, setSnackbarConfig] = useState({ message: '', type: '' });

  // parameters for backend
  const [sdpValue, setSdpValue] = useState(0.2); // SDP/DP
  const [noiseValue, setNoiseValue] = useState(0.5); // 情感
  const [noisewValue, setNoisewValue] = useState(0.9); // 音素长度
  const [lengthValue, setLengthValue] = useState(1.0); // 语速
  const [formatValue, setFormatValue] = useState('wav'); // 格式

  const handleButtonClick = async () => {
    console.log(voiceCardSelected, textInput);
    setSnackbarConfig({ message: '', type: '' });
    setIsLoading(true);
  
    try {

      const response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/tts?speaker=${voiceCardSelected.name}&text=${textInput}&format=${formatValue}&length=${lengthValue}&noise=${noiseValue}&noisew=${noisewValue}&sdp=${sdpValue}`
      , {
        method: 'GET'
      });

      const responseData = await response.json();  
      if (responseData) {
        if (response.ok) {
          const audioResponse = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/audio/${responseData.filename}`,
          {
            method: 'GET',
          });
          console.log('audioResponse', audioResponse)
          const audioBlob = await audioResponse.blob();
          const audioURL= URL.createObjectURL(audioBlob);
          console.log('audio_path', audioURL)
          
          const newCard = {
            id: responseData.filename,
            voice: voiceCardSelected.name,
            length: lengthValue,
            noise: noiseValue,
            noisew: noisewValue,
            sdp: sdpValue,
            text: textInput,
            audioURL: audioURL // 将音频 URL 保存到卡片中
          };
    
          setGeneratedCards([newCard, ...generatedCards]);
        }
      } else {
        console.error('Error fetching audio:', response.statusText);
        setSnackbarConfig({
          message: 'Error fetching audio',
          type: 'error'
        });
      }
    } catch (error) {
      console.error('There was an error:', error);
      setSnackbarConfig({
        message: error.message,
        type: 'error'
      });
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
          <VoicesSearch setSearchText={setSearchText} />
          <VoicesSelect setVoiceCardSelected={setVoiceCardSelected}
            searchText={searchText} pageQuery={'tts'} />

          <VoicesText voiceCardSelected={voiceCardSelected} setTextInput={setTextInput} 
          sdpValue={sdpValue} setSdpValue={setSdpValue}
          emotionValue={noiseValue} setEmotionValue={setNoiseValue}
          lengthValue={noisewValue} setLengthValue={setNoisewValue}
          speedValue={lengthValue} setSpeedValue={setLengthValue}
          setFormatValue={setFormatValue}
          />

          <Box sx={{ mt: 2, display: 'flex', justifyContent: 'center' }}>
            {isLoading ? (
              <CircularProgress color="success"  />
            ) : (
              <Button 
                variant="contained" 
                color="success" 
                onClick={() => {
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
    {snackbarConfig.message && <CustomSnackbar message={snackbarConfig.message} type={snackbarConfig.type} />}
  </>
  )

};

Page.getLayout = (page) => (
  <DashboardLayout>
    {page}
  </DashboardLayout>
);

export default Page;
