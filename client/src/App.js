import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Navbar } from 'react-bootstrap';
import SentimentalDoughnutChart from './components/SentimentalDoughnutChart';
import './App.css';

function App() {
  var data = {
    labels: ['Positive', 'Neutral', 'Negative'],
    datasets: [
      {
        label: '# of Votes',
        data: [12, 19, 12],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
        ],
        borderWidth: 1,
      },
    ],
  }
  return (
    <div>
      <Navbar bg="light">
        <Container>
          <Navbar.Brand href="#home">Tweet Analysis</Navbar.Brand>
        </Container>
      </Navbar>
      <Container>
        <h2 className="title"> UMB Sentimentals Analysis </h2>
        <SentimentalDoughnutChart data={data} />
      </Container>
    </div>
  );
}

export default App;
