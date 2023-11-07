const express = require('express');
const axios = require('axios');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
let fetch;

const AK = "tvGX7Y****MDSl8i"
const SK = "HO6dIO****PF4OVM"

const app = express();
const port = 3001;

app.use(cors({
  // origin: 'https://6a4e5b50.r10.cpolar.top', // 更改为你的内网穿透域名
  origin: 'http://localhost:3001'
}));  // production

// app.use(cors()); // development
// use gradio
app.get('/genshinAPI', async (req, res) => {
  try {
    const { speaker, text, format, length, noise, noisew, sdp } = req.query;
    const trimmedSpeaker = speaker.trim();
    const trimmedLength = length.trim();
    const gradioAPI = await client("https://modelscope.cn/api/v1/studio/erythrocyte/Bert-VITS2_Genshin_TTS/gradio/");
    const result = await gradioAPI.predict(0, [
        "Howdy!", // string  in 'AccessToken' Textbox component		
				`${trimmedSpeaker}`, // string  in '要合成的内容' Textbox component		
        text, // string  in '要合成的内容' Textbox component		
				sdp, // number (numeric value between 0 and 1) in 'SDP/DP 混合比' Slider component		
				noise, // number (numeric value between 0.1 and 2) in '感情' Slider component		
				noisew, // number (numeric value between 0.1 and 2) in '音素长度' Slider component		
				-99, // number (numeric value between -99 and 99) in '语速(%)' Slider component
    ]);

  console.log(result.data);

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

// app.get('/genshinAPI', async (req, res) => {
//   try {
//     const { speaker, text, format, length, noise, noisew, sdp } = req.query;
//     const trimmedSpeaker = speaker.trim();
//     const trimmedLength = length.trim();
//     const apiUrl = `https://genshinvoice.top/api?speaker=${encodeURIComponent(trimmedSpeaker)}&text=${encodeURIComponent(text)}&format=${encodeURIComponent(format)}&length=${encodeURIComponent(trimmedLength)}&noise=${encodeURIComponent(noise)}&noisew=${encodeURIComponent(noisew)}&sdp_ratio=${encodeURIComponent(sdp)}`;
//     const apiResponse = await fetch(apiUrl);

//     if (apiResponse.status === 200 && apiResponse.headers.get('content-type') === 'audio/wav') {
//       // Set the response headers
//       res.setHeader('Content-Type', 'audio/wav');

//       // Pipe the audio data to the response
//       apiResponse.body.pipe(res);
//     } else {
//       console.error('Unexpected response:', apiResponse);
//       res.status(500).json({ error: 'Unexpected API response' });
//     }
//   } catch (error) {
//     console.error('Error fetching data:', error);
//     res.status(500).json({ error: 'An error occurred while fetching data' });
//   }
// });

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

app.get('/chat', async (req, res) => {
  var options = {
      'method': 'post',
      'url': 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=' + await getAccessToken(),
      'headers': {
              'Content-Type': 'application/json'
      }
  };

  try {
    const response = await axios(options);
    console.log(response.data);
  } catch (error) {
    throw new Error(error);
  }
});

/**
* 使用 AK，SK 生成鉴权签名（Access Token）
* @return string 鉴权签名信息（Access Token）
*/
function getAccessToken() {

  let options = {
      'method': 'post',
      'url': 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + AK + '&client_secret=' + SK,
  }
  return new Promise((resolve, reject) => {
      axios(options)
        .then(response => {
            resolve(response.data.access_token);
        })
        .catch(error => {
            reject(error);
        });
  })
}

import('node-fetch').then(nodeFetch => {
  fetch = nodeFetch.default || nodeFetch;
});