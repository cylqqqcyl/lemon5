import React, {useState, useEffect, useRef} from 'react';
import { Card, Typography, Box, Button, Menu, MenuItem } from '@mui/material';
import RecordIcon from '@mui/icons-material/Mic';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';
import { CustomSnackbar } from '../message/custom-snackbar';


export const RecordCard = ({ handleRecordClickOverride }) => {
    const [snackbarConfig, setSnackbarConfig] = useState({ message: '', type: '' });
    const [anchorEl, setAnchorEl] = useState(null); 
    const [selectedMic, setSelectedMic] = useState(null);
    const [selectedMicId, setSelectedMicId] = useState(null);
    const [recordAudioURL, setRecordAudioURL] = useState(null);
    const [mics, setMics] = useState([]);  
    const [micIDs, setMicIDs] = useState([]);
    const [recorder, setRecorder] = useState(null);
    const [stream, setStream] = useState(null);
    const [recording, setRecording] = useState(false);


    const boxRef = useRef(null); // Create a ref to attach to the Box
    const chunksRef = useRef([]);

    const startRecording = async () => {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true , deviceId: selectedMicId});
      setStream(stream);

      const recorder = new MediaRecorder(stream);
      setRecorder(recorder);

      recorder.ondataavailable = (e) => {
        chunksRef.current.push(e.data);
      };

      recorder.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: 'audio/webm;codecs=opus' });
        const url = URL.createObjectURL(blob);
        setRecordAudioURL(url);
        chunksRef.current = [];  // Clear the chunks
        setRecording(false);
      };
  
      recorder.start();
      setRecorder(recorder);
      setRecording(true);
    };

    const stopRecording = () => {
      if (recorder) {
        recorder.stop();
        stream.getTracks().forEach((track) => track.stop());
        setStream(null);
      }
    };


    
    const handleMenuClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = (item) => {
    setAnchorEl(null);
    if (item){
        setSelectedMic(item);
        setSelectedMicId(micIDs[mics.indexOf(item)]);
    }
  };

  const handleRecordClick = () => {
    if (!recording) {
      startRecording();
    } else {
      stopRecording();
    }
  };
  
  useEffect(() => {
    handleRecordClickOverride(recording, recordAudioURL);
  }, [recording]);

  useEffect(() => {
    handleRecordRequest();
  }, []); // Empty dependency array means this useEffect runs once when the component mounts


  const handleRecordRequest = () => {
    setSnackbarConfig({ message: '', type: '' });
    navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {

      // Optionally, enumerate devices again to update device information
      return navigator.mediaDevices.enumerateDevices();
    })
    .then(devices => {
      // Get a list of only audio devices
      const audioDevices = devices.filter(device => device.kind === 'audioinput');
      // Get the device names
      const audioDeviceNames = audioDevices.map(device => device.label);
      // Get the device IDs
      const audioDeviceIDs = audioDevices.map(device => device.deviceId);
      // Set the state variable
      setMics(audioDeviceNames);
      setMicIDs(audioDeviceIDs);
    })
    .catch(error => {
      console.error("Permission denied or no audio device found", error);
      setSnackbarConfig({ message: 'Permission denied or no audio device found', type: 'error' });
    });
    };

  return (
    <Box>
    <Card sx={{ position: 'relative', p: 2}}>
      <CustomSnackbar message={snackbarConfig.message} type={snackbarConfig.type} />
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
  );
};
