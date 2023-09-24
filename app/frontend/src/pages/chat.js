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

  const characters = ['派蒙','可莉','甘雨','刻晴','申鹤']

const Page = () => {
  const [messages, setMessages] = useState([
    { sender: 'user', text: 'Hello' },
    { sender: '派蒙', text: 'Hi there!' },
    // Add more messages as needed
  ]);

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
          <CharacterSelect characters={characters}/>
          <ConversationCard messages={messages} setMessages={setMessages}/>
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