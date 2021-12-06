import React, { useEffect, useState } from 'react';
import { Container, Navbar, Row, Col, Spinner } from 'react-bootstrap';
import SentimentalDoughnutChart from './components/SentimentalDoughnutChart';
import SentimentalBarChart from './components/SentimentalBarChart';
import SentimentalSpinner from './components/SentimentalSpinner';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [data, setData] = useState([])
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    setTimeout(() => {
      axios.get(`https://enigmatic-hollows-91721.herokuapp.com/`)
      // axios.get(`http://localhost:5000/`)
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
          <Navbar.Brand>Airlines Sentimental Tweets Analysis</Navbar.Brand>
        </Container>
      </Navbar>
      <div className="graph__wrapper">
        <Row>
          <Col xs={12} md={6}>
            <div className="box__wrapper">
              <Container style={{ minHeight: '100%' }}>
                {
                  (isLoading)
                    ? <SentimentalSpinner />
                    : <SentimentalDoughnutChart data={data.sentimental.data} options={data.sentimental.optionsDoughnut} />
                }
              </Container>
            </div>
          </Col>
          <Col xs={12} md={6}>
            <div className="box__wrapper">
              <Container style={{ minHeight: '100%' }}>
                {
                  (isLoading)
                    ? <SentimentalSpinner />
                    : <SentimentalBarChart data={data.sentimental.data} options={data.sentimental.optionsBar} toolTipContent={'This is a bar graph that lays out the counts of the sentimentals'} />
                }
              </Container>
            </div>
          </Col>
        </Row>
        <Row>
          <Col xs={12} md={6}>
            <div className="box__wrapper">
              <Container style={{ minHeight: '100%' }}>
                {
                  (isLoading)
                    ? <SentimentalSpinner />
                    : <SentimentalBarChart data={data.airlines.data} options={data.airlines.options} toolTipContent={'This is a bar graph that shows the counts of tweets of all the airlines that were mentioned'} />
                }
              </Container>
            </div>
          </Col>
          <Col xs={12} md={6}>
            <div className="box__wrapper">
              <Container style={{ minHeight: '100%' }}>
                {
                  (isLoading)
                    ? <SentimentalSpinner />
                    : <SentimentalBarChart data={data.negative_test.data} options={data.negative_test.options} toolTipContent={'This is a bar graph shows the different categories of negative reasons and the counts of it'} />
                }
              </Container>
            </div>
          </Col>
        </Row>
        <Row>
        <Col>
            <div className="box__wrapper">
              <Container style={{ minHeight: '100%' }}>
                {
                  (isLoading)
                    ? <SentimentalSpinner />
                    : <SentimentalBarChart data={data.null_values_from_columns.data} options={data.null_values_from_columns.options} toolTipContent={'This is a bar graph shows the counts of the null values that existed within each of the data sets'} />
                }
              </Container>
            </div>
          </Col>
        </Row>
      </div>
    </div>
  );
}

export default App;
