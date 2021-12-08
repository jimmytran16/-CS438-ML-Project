import React, { useState } from 'react';
import { Container, Navbar, Row, Col, Button } from 'react-bootstrap';
import SentimentalMetricsScreen from './screens/SentimentalMetricsScreen';
import NegativeMetricsScreen from './screens/NegativeMetricsScreen';
import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {

  const [mainIsActive, setMainIsActive] = useState(true)
  const [negativeIsActive, setNegativeIsActive] = useState(false)

  const handleMainClick = () => {
    setMainIsActive(true);
    setNegativeIsActive(false);
  }

  const handleNegativeClick = () => {
    setNegativeIsActive(true);
    setMainIsActive(false);
  }

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
          <div style={{ display: 'flex', justifyContent: 'space-evenly', paddingTop: 20, paddingBottom: 20 }}>
            <Link to="/">
              <Button onClick={handleMainClick} active={mainIsActive ? true : false}>Main</Button>
            </Link>
            <Link to="/negatives">
              <Button onClick={handleNegativeClick} active={negativeIsActive ? true : false}>Negative Reason Counts</Button>
            </Link>
          </div>
          <Routes>
            <Route path='/' element={<SentimentalMetricsScreen />} />
            <Route path='/negatives' element={<NegativeMetricsScreen />} />
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
