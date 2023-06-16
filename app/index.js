const express = require('express');
const app = express();

app.use(express.json());

app.all('*', (req, res) => {
  console.log('Received request:');
  console.log('Method:', req.method);
  console.log('URL:', req.originalUrl);
  console.log('Headers:', req.headers);
  console.log('Body:', req.body);

  res.json({
    method: req.method,
    url: req.originalUrl,
    headers: req.headers,
    body: req.body
  });
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
