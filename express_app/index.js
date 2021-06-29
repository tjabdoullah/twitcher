const tmi = require('tmi.js');
const {spawn} = require('child_process');

const client = new tmi.Client({
  connection: {
    secure: true,
    reconnect: true
  },
  identity: {
    username: 'abdoullahtj',
    password: '9sf47q6po1qbx8p8smc71hy8yg93m6'
  },
  channels: [ 'AbdoullahTJ' ]
});

client.connect();

client.on('message', (channel, tags, message, self) => {
  const txt = `${message}`
  console.log(`${tags['display-name']}: ${message}`);
  console.log(`${message}`);
  const python = spawn('python3', ['../python_scripts/move.py', txt]);
});
