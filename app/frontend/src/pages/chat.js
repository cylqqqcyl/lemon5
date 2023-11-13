import React, {useState, useEffect} from 'react';
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


const Page = () => {
  const [characters, setCharacters] = useState([]);
  const [messages, setMessages] = useState([]);
  const [selectedCharacter, setSelectedCharacter] = useState(null);

  const handleCharacterSelected = (characterName) => {
    setSelectedCharacter(characterName);
    setMessages([ // Reset messages
    ]);
  };
  useEffect(() => {
    const url = new URL(`${process.env.NEXT_PUBLIC_BACKEND_URL}/voices`);

    fetch(url)
      .then(response => response.json())
      .then(data => {
        setCharacters(data);
      })
      .catch(error => {
        console.error('Error fetching character data:', error);
      });
  }, []);

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
