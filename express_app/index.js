const tmi = require('tmi.js');
const {spawn} = require('child_process');

const client = new tmi.Client({
  connection: {
    secure: true,
    reconnect: true
  },
  identity: {
    username: 'abdoullahtj',
    password: 'll2qg4231qavcerqjqtacq0nq6d2qa'
  },
  channels: [ 'AbdoullahTJ' ]
});

client.connect();

client.on('message', (channel, tags, message, self) => {
  const txt = `${tags['display-name']}: ${message}`
  console.log(`${tags['display-name']}: ${message}`);
  const python = spawn('python3', ['move_left.py', txt]);
});