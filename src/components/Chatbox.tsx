import React, { useState } from 'react';
import { Paper, TextField, Button, List, ListItem, ListItemText } from '@mui/material';

const ChatBox: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState<string>('');

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, input]);
      setInput('');
    }
  };

  return (
    <Paper style={{ padding: 16 }}>
      <List style={{ maxHeight: '300px', overflow: 'auto' }}>
        {messages.map((msg, index) => (
          <ListItem key={index}>
            <ListItemText primary={msg} />
          </ListItem>
        ))}
      </List>
      <div style={{ display: 'flex', marginTop: 16 }}>
        <TextField
          fullWidth
          variant="outlined"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Type a message"
        />
        <Button color="primary" variant="contained" onClick={handleSend} style={{ marginLeft: 8 }}>
          Send
        </Button>
      </div>
    </Paper>
  );
};

export default ChatBox;
