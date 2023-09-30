import React, {useState} from 'react';
import Head from 'next/head';
import {
  Box,
  Container,
  Stack,
  SvgIcon,
  Typography,
} from '@mui/material';
import { Layout as DashboardLayout } from 'src/layouts/dashboard/layout';
import ChatIcon from '@heroicons/react/24/solid/SparklesIcon';
import {CharacterSelect} from 'src/sections/chat/character-select';
import {ConversationCard} from 'src/sections/chat/conversation-card';
import { voices as characters , default_response} from 'src/sections/voices/constants';

const Page = () => {

  const [messages, setMessages] = useState([
    { sender: '派蒙', text: '你好呀！我是你的人工智能小助手，很高兴见到你，欢迎问我任何问题。', mode: 'audio' ,audioURL:  default_response['派蒙'] },
    // Add more messages as needed
  ]);
  const [selectedCharacter, setSelectedCharacter] = useState('派蒙');  // 默认为派蒙

  const handleCharacterSelected = (characterName) => {
    setSelectedCharacter(characterName);
    setMessages([ // Reset messages
      { sender: characterName, text: '你好呀！我是你的人工智能小助手，很高兴见到你，欢迎问我任何问题。', mode: 'audio' ,audioURL:  default_response[characterName] },
    ]);
  };

  return(
  <>
    <Head>
      <title>
        Lemon5 | 语音对话
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
                  <ChatIcon />
                </SvgIcon>
                <Typography variant="h4">
                  语音对话
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
                  选择角色，开始对话
                </Typography>
              </Stack>
            </Stack>
          </Stack>
          <CharacterSelect characters={characters} selectedCharacter={selectedCharacter} onCharacterSelected={handleCharacterSelected} />
          <ConversationCard messages={messages} setMessages={setMessages} 
          selectedCharacter={selectedCharacter} />
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
