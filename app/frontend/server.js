const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
let fetch;

import('node-fetch').then(nodeFetch => {
    fetch = nodeFetch.default || nodeFetch;
});

const app = express();
const port = 3001;

app.use(cors({
  origin: 'https://6a4e5b50.r10.cpolar.top', // 更改为你的内网穿透域名
}));  // production

// app.use(cors()); // development

app.get('/genshinAPI', async (req, res) => {
  try {
    const { speaker, text, format, length, noise, noisew, sdp } = req.query;
    const trimmedSpeaker = speaker.trim();
    const trimmedLength = length.trim();
    const apiUrl = `https://genshinvoice.top/api?speaker=${encodeURIComponent(trimmedSpeaker)}&text=${encodeURIComponent(text)}&format=${encodeURIComponent(format)}&length=${encodeURIComponent(trimmedLength)}&noise=${encodeURIComponent(noise)}&noisew=${encodeURIComponent(noisew)}&sdp_ratio=${encodeURIComponent(sdp)}`;
    const apiResponse = await fetch(apiUrl);

    if (apiResponse.status === 200 && apiResponse.headers.get('content-type') === 'audio/wav') {
      // Set the response headers
      res.setHeader('Content-Type', 'audio/wav');

      // Pipe the audio data to the response
      apiResponse.body.pipe(res);
    } else {
      console.error('Unexpected response:', apiResponse);
      res.status(500).json({ error: 'Unexpected API response' });
    }
  } catch (error) {
    console.error('Error fetching data:', error);
    res.status(500).json({ error: 'An error occurred while fetching data' });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
