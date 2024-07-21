import React from 'react';
import { AppBar, Toolbar, Typography, Grid, Paper } from '@mui/material';
import ChatBox from '../components/Chatbox';
import VideoFeed from '../components/VideoFeed';

const HomePage: React.FC = () => {
  return (
    <div className="home-page">
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">
            Sign Language Translation Tool
          </Typography>
        </Toolbar>
      </AppBar>
      <Grid container spacing={3} style={{ padding: 24 }}>
        <Grid item xs={12} sm={6}>
          <Paper style={{ padding: 16 }}>
            <Typography variant="h5" gutterBottom>
              Video Feed
            </Typography>
            <VideoFeed isLocal={true} />
            <VideoFeed isLocal={false} />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper style={{ padding: 16 }}>
            <Typography variant="h5" gutterBottom>
              Chat Window
            </Typography>
            <ChatBox />
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
};

export default HomePage;
