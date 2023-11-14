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
import { AudioUpload } from 'src/sections/voices/audio-upload';
import { GeneratedGrid } from 'src/sections/voices/generated-grid';
import ConverseIcon from '@heroicons/react/24/solid/ArrowsRightLeftIcon';

  
const Page = () => {
  const [searchText, setSearchText] = useState('');
  const [voiceCardSelected, setVoiceCardSelected] = useState(null);
  const [audioInput, setAudioInput] = useState(null);
  const [isLoading, setIsLoading] = useState(false); // New state for loading
  const [generatedCards, setGeneratedCards] = useState([]); // New state for generated cards

  const handleButtonClick = () => {
    let id = 0;
    setIsLoading(true);
    // logic here,
    // After the operation is complete, set isLoading back to false
    // setIsLoading(false);
    const newCard = {
      id: id++,
      voice: voiceCardSelected,
      text: audioInput
    };
    setTimeout(() => setIsLoading(false), 2000); //delay 2s debug
    setGeneratedCards([newCard, ...generatedCards]); // Add new card at the beginning
  };

  return(
  <>
    <Head>
      <title>
        Lemon5 | 语音转换
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
                  <ConverseIcon />
                </SvgIcon>
                <Typography variant="h4">
                  语音转换
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
                  上传音频，将音频转为另一种音色
                </Typography>
              </Stack>
            </Stack>
          </Stack>
          <VoicesSearch setSearchText={setSearchText} />
          <VoicesSelect setVoiceCardSelected={setVoiceCardSelected} searchText={searchText} />
          <AudioUpload voiceCardSelected={voiceCardSelected} setAudioInput={setAudioInput} />
          <Box sx={{ mt: 2, display: 'flex', justifyContent: 'center' }}>
            {isLoading ? (
              <CircularProgress color="success"  />
            ) : (
              <Button variant="contained" color="success" onClick={handleButtonClick} 
              disabled={!voiceCardSelected || !audioInput}
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
