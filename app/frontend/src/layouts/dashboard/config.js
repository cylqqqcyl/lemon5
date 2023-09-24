import React from 'react';
import { SvgIcon } from '@mui/material';
import TextBubbleIcon from '@heroicons/react/24/solid/ChatBubbleBottomCenterTextIcon';
import ConverseIcon from '@heroicons/react/24/solid/ArrowsRightLeftIcon';
import ChatIcon from '@heroicons/react/24/solid/SparklesIcon';

export const items = [
  {
    title: '文本转语音',
    path: '/tts',
    icon: (
      <SvgIcon fontSize="small">
        <TextBubbleIcon />
      </SvgIcon>
    )
  },  
  {
    title: '语音转换',
    path: '/vc',
    icon: (
      <SvgIcon fontSize="small">
        <ConverseIcon />
      </SvgIcon>
    )
  },
  {
    title: '语音对话',
    path: '/chat',
    icon: (
      <SvgIcon fontSize="small">
        <ChatIcon />
      </SvgIcon>
    )
  }

];
