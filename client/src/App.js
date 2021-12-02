import React, { useEffect, useState } from 'react';
import { Container, Navbar, Row, Col } from 'react-bootstrap';
import SentimentalDoughnutChart from './components/SentimentalDoughnutChart';
import SentimentalBarChart from './components/SentimentalBarChart';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [data, setData] = useState([])
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    setTimeout(() => {
      axios.get(`https://enigmatic-hollows-91721.herokuapp.com/`)
        .then(res => {
          console.log(res.data)
          setData(res.data)
          setIsLoading(false)
        })
        .catch(err => console.log(err)) 
    }, 1000)
  }, [])


  return (
    <div>
      <Navbar bg="light">
        <Container>
          <Navbar.Brand href="#home">Airlines Sentimental Tweet Analysis</Navbar.Brand>
        </Container>
      </Navbar>
      <Row>
        <Col xs={12} md={6}>
          <Container>
            {
              (isLoading)
                ? <p>Loading.... </p>
                : <SentimentalDoughnutChart data={data.sentimental.data} options={data.sentimental.options} />
            }
          </Container>
        </Col>
        <Col xs={12} md={6}>
        <Container>
            {
              (isLoading)
                ? <p>Loading.... </p>
                : <SentimentalBarChart data={data.sentimental.data} options={data.sentimental.options} />
            }
          </Container>
        </Col>
      </Row>
      <Row>
        <Col>
        <Container>
            {
              (isLoading)
                ? <p>Loading.... </p>
                : <SentimentalBarChart data={data.airlines.data} options={data.airlines.options} />
            }
          </Container></Col>
      </Row>
    </div>
  );
}

export default App;
