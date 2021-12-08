import React from 'react';
import { Container, Navbar, Row, Col } from 'react-bootstrap';
import SentimentalMetricsScreen from './screens/SentimentalMetricsScreen';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    // REFERENCE : https://reactrouterdotcom.fly.dev/docs/en/v6/getting-started/overview
    <BrowserRouter>
      <div>
        <Navbar bg="light">
          <Container>
            <Navbar.Brand>Airlines Sentimental Tweets Analysis</Navbar.Brand>
          </Container>
        </Navbar>
        <div className="graph__wrapper">
          <Routes>
            <Route path='/' element={<SentimentalMetricsScreen />} />
            <Route path='/tweets' element={<SentimentalTweets />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}


const SentimentalTweets = () => {
  return (
    <p>This is the Tweets</p>
  )
}

export default App;
