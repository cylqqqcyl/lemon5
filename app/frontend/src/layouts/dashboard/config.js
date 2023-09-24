import React from 'react';
import { SvgIcon } from '@mui/material';
import TextBubbleIcon from '@heroicons/react/24/solid/ChatBubbleBottomCenterTextIcon';
import ConverseIcon from '@heroicons/react/24/solid/ArrowsRightLeftIcon';
import DenoiseIcon from '@heroicons/react/24/solid/SparklesIcon';

export const items = [
  {
    title: '文本转语音',
    path: '/',
    icon: (
      <SvgIcon fontSize="small">
        <TextBubbleIcon />
      </SvgIcon>
    )
  },  
  {
    title: '语音转换',
    path: '/voiceCon',
    icon: (
      <SvgIcon fontSize="small">
        <ConverseIcon />
      </SvgIcon>
    )
  },
  {
    title: '语音降噪',
    path: '/denoise',
    icon: (
      <SvgIcon fontSize="small">
        <DenoiseIcon />
      </SvgIcon>
    )
  }

];
