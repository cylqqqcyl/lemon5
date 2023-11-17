import React, { useState, useEffect, useRef } from 'react';
import { Card, Typography, Collapse, IconButton, Box, Button, Menu, MenuItem} from '@mui/material';
import { AudioCard } from './audio-card';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import BackIcon from '@mui/icons-material/ArrowBack';
import UploadIcon from '@mui/icons-material/CloudUpload';
import RecordIcon from '@mui/icons-material/Mic';
import FileIcon from '@mui/icons-material/AudioFile';
import { RecordCard } from './record-card';


export const AudioUpload = ({voiceCardSelected, setAudioInput}) => {
  const [expanded, setExpanded] = useState(false);
  const [inputAudio, setInputAudio] = useState(null);
  const [changeAudioSelected, setChangeAudioSelected] = useState(false);
  const [audioSource, setAudioSource] = useState(null); 
  const [choseUpload, setChoseUpload] = useState(false);
  const [choseRecord, setChoseRecord] = useState(false);
  const [recordURL, setRecordURL] = useState(null);
  const [recordDuration, setRecordDuration] = useState(0);
  const [audioURL, setAudioURL] = useState(null);
  const [serverFile, setServerFile] = useState(''); // File uploaded to server

  const fileInputRef = useRef(null); // Create a ref to the file input element

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

 const handleUploadSelect = () => {
    setChoseUpload(true);
    setChoseRecord(false);
  };

  const handleRecordSelect = () => {
      setChoseUpload(false);
      setChoseRecord(true);

  };
  
  const handleRecordClick = (recording, recordURL, duration) => {
    if (!recording && recordURL) {
      setInputAudio('录制音频');
      setAudioSource('录制音频');
      setAudioInput('录制音频');
      setRecordURL(recordURL);
      setRecordDuration(duration);
      
      setChoseRecord(false);
      setChangeAudioSelected(false);
    }

  };

  const handleBackClick = () => {
    setChoseUpload(false);
    setChoseRecord(false);
    setChangeAudioSelected(false);
  };

  const handleChangeClick = () => {
    setChoseUpload(false);
    setChoseRecord(false);
    setChangeAudioSelected(true);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    const files = e.dataTransfer.files;
    if (files && files[0]) {
      handleFileDrop(files[0]);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleFileDrop = (file) => {
    setInputAudio(file);
    setAudioSource(file.name);
    setAudioInput(file.name);
    setChoseUpload(false);
    setChangeAudioSelected(false);
    sendFileToServer(file); // Function to send file to server
  };

  const handleUploadFile = () => {
    fileInputRef.current.click(); // Programmatically trigger the file input click event
  };


  const handleFileChange = (e) => {
    const file = e.target.files[0]; // Get the file from the input event
    if (file) {
      try {
        // Revoke the old Blob URL to avoid memory leaks
        if (audioURL) {
          URL.revokeObjectURL(audioURL);
      }

      const url = URL.createObjectURL(file);
      setAudioURL(url);
      setInputAudio(file); // Update your state or do something with the file
      setAudioSource(file.name);
      setAudioInput(file.name);
      setChoseUpload(false);
      setChangeAudioSelected(false);
      sendFileToServer(file); // Function to send file to server
      } catch (error) {
        console.error("Error in uploading file", error);
      }
    }
  };



  useEffect(() => {
    console.log("Server file", serverFile);
  }, [serverFile]);

  useEffect(() => {
    if (voiceCardSelected) {
      setExpanded(true);
    }
  }, [voiceCardSelected]);

  const sendFileToServer = async (file) => {
    const formData = new FormData();
    formData.append("file", file);
    // Send file to Flask backend
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/recording`, { 
        method: 'POST',
        body: formData,
      });
      if (response.ok) {
        console.log("File uploaded successfully");
      }
    } catch (error) {
      console.error("Error in uploading file", error);
    }
  };

  return (
    <Card sx={{ p: 2, position: 'relative' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography variant="h5" sx={{ color: 'text.primary', p: 1 }}>
          你的音频
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={handleExpandClick}>
          <Typography variant="body1" sx={{ marginRight: 0, color: 'text.secondary', p: 0 }}>
            {expanded ? null : inputAudio ? '更改音频' : '添加音频'}
          </Typography>
          <IconButton onClick={handleExpandClick} sx={{ position: 'relative' }}>
            {expanded ? <ExpandLessIcon /> : <ExpandMoreIcon />}
          </IconButton>
        </Box>
      </Box>
      <Collapse in={expanded}>
        {inputAudio && !choseUpload && !choseRecord && !changeAudioSelected &&
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', width: '100%' }}>
          <AudioCard text={audioSource} audioURL={audioSource==='录制音频' ? recordURL : audioURL} audioDuration={audioSource==='录制音频' ? recordDuration : null} />
          <Typography variant="body1" onClick={handleChangeClick}
          sx={{ color: 'info', mt:2, fontWeight: 'bold', cursor: 'pointer' }}>
                  更换音频
          </Typography>
        </Box>
        }


        {(choseUpload || choseRecord || changeAudioSelected) &&
        <Box sx={{ display: 'flex', flexDirection: 'row', alignItems: 'left'}}>
        <Box onClick={handleBackClick} sx={{ display: 'flex', flexDirection: 'row', 
        mb: 1, ml: 2, alignItems: 'center', cursor: 'pointer' }}>
          <BackIcon />
          <Typography variant="body1" sx={{ color: 'text.secondary' }}>
            返回
          </Typography>
        </Box>
      </Box>
      }

        {!choseUpload && !choseRecord && (!inputAudio || changeAudioSelected) &&
        <Card sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 2 }}>
          <Box onClick={handleUploadSelect}
          sx={{ display: 'flex', flexDirection: 'column', 
          alignItems: 'center', mt:2, cursor: 'pointer' }} >
            <UploadIcon sx={{ color: 'info.main'}} />
          <Typography variant="body1" sx={{ color: 'text.secondary'}}>
            上传音频文件
          </Typography>
          </Box>
          <Typography variant="body1" sx={{ color: 'neutral.400', mt: 2 }}>
            或者
          </Typography>
          <Box onClick={handleRecordSelect}
              sx={{ display: 'flex', flexDirection: 'column', 
              alignItems: 'center', mt: 2, cursor: 'pointer' }} >
            <RecordIcon sx={{ color: 'error.main'}} />
          <Typography variant="body1" sx={{ color: 'text.secondary', mb:2 }}>
            录制你的声音
          </Typography>
          </Box>
        </Card>
        }

          {/* Hidden file explorer input */}
        <input 
          type="file" 
          ref={fileInputRef} 
          style={{ display: 'none' }} 
          accept="audio/*" // Accept only audio files
          onChange={handleFileChange} 
        />


        {choseUpload &&
        <Card onDrop={handleDrop} onDragOver={handleDragOver} onClick={handleUploadFile}  sx={{  cursor: 'pointer',display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 2, borderStyle: 'dashed', borderColor: 'neutral.500'}}>
          <FileIcon sx={{ color: 'info.main', fontSize: 50, mt: 2}} />
          <Typography variant="body1" sx={{ color: 'text.secondary', mt: 2 }}>

              上传音频文件, 或者将其拖到这里
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary', mb: 2 }}>
            使用高质量的音频文件，少于1 min，仅人声
          </Typography>
        </Card>}
          

        {choseRecord &&
          <RecordCard handleRecordClickOverride={handleRecordClick}/>
        }
      </Collapse>
    </Card>
  );
};
