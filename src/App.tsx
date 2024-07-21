import React from 'react';
import { CssBaseline, Container } from '@mui/material';
import HomePage from './pages/HomePage';
import './styles/styles.css';

const App: React.FC = () => {
  return (
    <div className="App">
      <CssBaseline />
      <Container>
        <HomePage />
      </Container>
    </div>
  );
};

export default App;
