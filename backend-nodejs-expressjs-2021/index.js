const express = require('express');
const cors = require('cors');
const routerApi = require('./routes');

const {logErrors, errorHandler, boomErrorHandler} = require('./middlewares/error.handler');

const app = express();
const port = 3000;

app.use(express.json())

const whitelist = ['http://localhost:8000', 'https://myapp.co'];
const options = {
  origin: (origin, callback) =>{
    if (whitelist.includes(origin)  || !origin) {
      callback(null, true);
    } else{
      callback(new Error('no permitido'));
    }
  }
}
app.use(cors(options));

app.get('/',(req, res) => {
  res.send('hello world server');
});

app.get('/nueva-ruta',(req, res) => {
  res.send('hello I am a new route');
});

routerApi(app);


app.use(logErrors);
app.use(boomErrorHandler);
app.use(errorHandler);


app.listen(port, () => {
  console.log('My port ' + port);
});
