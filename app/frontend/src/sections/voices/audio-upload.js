import React, { useState, useEffect, useRef } from 'react';
import { Card, Typography, Collapse, IconButton, Box, Button, Menu, MenuItem} from '@mui/material';
import { AudioCard } from './audio-card';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import BackIcon from '@mui/icons-material/ArrowBack';
import UploadIcon from '@mui/icons-material/CloudUpload';
import RecordIcon from '@mui/icons-material/Mic';
import FileIcon from '@mui/icons-material/AudioFile';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';


export const AudioUpload = ({voiceCardSelected, setAudioInput}) => {
  const [expanded, setExpanded] = useState(false);
  const [inputAudio, setInputAudio] = useState(null);
  const [changeAudioSelected, setChangeAudioSelected] = useState(false);
  const [audioSource, setAudioSource] = useState(null); 
  const [choseUpload, setChoseUpload] = useState(false);
  const [choseRecord, setChoseRecord] = useState(false);
  const [anchorEl, setAnchorEl] = useState(null);
  const [mics, setMics] = useState([]);  
  const [selectedMic, setSelectedMic] = useState(null);  
  const [recording, setRecording] = useState(false);  

  const fileInputRef = useRef(null); // Create a ref to the file input element
  const boxRef = useRef(null); // Create a ref to attach to the Box

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

 const handleUploadSelect = () => {
    setChoseUpload(true);
    setChoseRecord(false);
  };

  const handleRecordSelect = () => {
    // Request microphone access
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        // Microphone access granted
        setChoseUpload(false);
        setChoseRecord(true);

        // Optionally, enumerate devices again to update device information
        return navigator.mediaDevices.enumerateDevices();
      })
      .then(devices => {
        // Get a list of only audio devices
        const audioDevices = devices.filter(device => device.kind === 'audioinput');
        // Get the device names
        const audioDeviceNames = audioDevices.map(device => device.label);
        // Set the state variable
        setMics(audioDeviceNames);
      })
      .catch(error => {
        console.error("Permission denied or no audio device found", error);
      });
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

  const handleUploadFile = () => {
    fileInputRef.current.click(); // Programmatically trigger the file input click event
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0]; // Get the selected file
    if (file) {
      setInputAudio(file); // Update your state or do something with the file
      setAudioSource(file.name);
      setAudioInput(file.name);
      setChoseUpload(false);
      setChangeAudioSelected(false);
    }
  };

  const handleMenuClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = (item) => {
    setAnchorEl(null);
    if (item){
        setSelectedMic(item);
    }
  };

  const handleRecordClick = () => {
    setRecording(!recording)
    if (recording) {
      setAudioSource('录制音频');
      setAudioInput('录制音频');
      setChoseRecord(false);
      setChangeAudioSelected(false);
    }
  };

  useEffect(() => {
    if (voiceCardSelected) {
      setExpanded(true);
    }
  }, [voiceCardSelected]);

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
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <AudioCard source={audioSource} />
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
        <Card sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 2, borderStyle: 'dashed', borderColor: 'neutral.500'}}>
          <FileIcon sx={{ color: 'info.main', fontSize: 50, mt: 2}} />
          <Typography variant="body1" sx={{ color: 'text.secondary', mt: 2 }}>
            <span onClick={handleUploadFile} style={{ cursor: 'pointer', textDecoration: 'underline' }}>
              上传音频文件</span> 或者将其拖到这里
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary', mb: 2 }}>
            使用高质量的音频文件，少于1 min，仅人声
          </Typography>
        </Card>}
          

        {choseRecord &&
        <Box>
        <Card sx={{ position: 'relative', p: 2}}>
          <Typography variant="body2" sx={{ color: 'text.secondary', p: 1, alignItems: 'left' }}>
              选择麦克风
          </Typography>
          <Box ref={boxRef}  // Attach the ref to the Box
          sx={{ p: 0, width: '100%', alignItems: 'center', display: 'flex', justifyContent: 'space-between' }}>
              <Button
                id="demo-customized-button"
                aria-controls={open ? 'demo-customized-menu' : undefined}
                aria-haspopup="true"
                aria-expanded={open ? 'true' : undefined}
                variant="contained"
                onClick={handleMenuClick}
                endIcon={<UnfoldMoreIcon />}
                sx={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center',  
            backgroundColor: 'neutral.100'}}
            >
                {selectedMic ? selectedMic : '无麦克风'}
            </Button>
              <Menu
                anchorEl={anchorEl}
                open={Boolean(anchorEl)}
                onClose={() => handleMenuClose(null)}
                PaperProps={{ style: { width: boxRef.current ? boxRef.current.offsetWidth : undefined }, }}  
              >
                {mics.map((mic, index) => (
                  <MenuItem key={index} onClick={() => handleMenuClose(mic)}
                  sx={{ backgroundColor: mic === selectedMic ? 'primary.lightest' : 'inherit', 
                  color:'inherit',
                  '&:hover': { backgroundColor: 'primary.light'}}}
                  >
                    {mic}
                  </MenuItem>
                ))}
              </Menu>
          </Box>
        </Card>
        <Card sx={{ position: 'relative', p: 2,mt:2}}>
          <Box sx={{ display: 'relative', flexDirection: 'column',justifyContent: 'space-between', alignItems: 'center' }}>
            <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'left'}}>
              <Typography variant="body1" sx={{ color: 'text.primary', ml: 1 }}>
                单击“录音”开始录制。 单击“停止录音”结束录制。
              </Typography>
              <Typography variant="body2" sx={{ color: 'text.secondary', ml: 1 }}>
                为了获得最佳效果，请在安静的环境中录制并尽量减少噪音。
              </Typography>
            </Box>
            <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
              <Button variant="outlined" color="error" onClick={handleRecordClick}
              disabled={!selectedMic}
               sx={{ width: '100', borderRadius: '50px',
                animation: recording ? 'breathing 1s infinite' : 'none',
                '@keyframes breathing': {
                  '0%': { backgroundColor: 'error.lightest' },
                  '50%': { backgroundColor: 'error.light' },
                  '100%': { backgroundColor: 'error.lightest' }, // Breathing effect
                }, }}>  
               <RecordIcon sx={{ color: selectedMic ? 'error.main' : 'disabled', mr:1}} />
                  {recording ? '停止录音' : '录音'}
              </Button>
            </Box>
          </Box>
        </Card>
        </Box>
        }
      </Collapse>
    </Card>
  );
};
