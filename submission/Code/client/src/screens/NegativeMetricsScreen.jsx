import React, { useEffect, useState } from 'react';
import SentimentalBarChart from '../components/SentimentalBarChart';
import SentimentalSpinner from '../components/SentimentalSpinner';
import { Container, Row, Col } from 'react-bootstrap';
import axios from 'axios'

export default function NegativeMetricsScreen() {
    const [data, setData] = useState([])
    const [isLoading, setIsLoading] = useState(true)
  
    useEffect(() => {
      setTimeout(() => {
        axios.get(`https://enigmatic-hollows-91721.herokuapp.com/negatives`)
        // axios.get(`http://localhost:5000/negatives`)
          .then(res => {
            console.log(res.data)
            setData(res.data)
            setIsLoading(false)
          })
          .catch(err => console.log(err))
      }, 0)
    }, [])
  
    return (
      <>
        <Row>
          <Col xs={12} md={6}>
            <div className="box__wrapper">
              <Container style={{ minHeight: '80%' }}>
                {
                  (isLoading)
                    ? <SentimentalSpinner />
                    : <SentimentalBarChart data={data.american.data} options={data.american.options} toolTipContent={'Shows the count of negative reasons per category for American Airlines'} />
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
                    : <SentimentalBarChart data={data.delta.data} options={data.delta.options} toolTipContent={'Shows the count of negative reasons per category for Delta Airlines'} />
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
                    : <SentimentalBarChart data={data.southwest.data} options={data.southwest.options} toolTipContent={'Shows the count of negative reasons per category for Southwest Airlines'} />
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
                    : <SentimentalBarChart data={data.united.data} options={data.united.options} toolTipContent={'Shows the count of negative reasons per category for United Airlines'} />
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
                    : <SentimentalBarChart data={data.us_airways.data} options={data.us_airways.options} toolTipContent={'Shows the count of negative reasons per category for US Airways Airlines'} />
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
                    : <SentimentalBarChart data={data.virgin_america.data} options={data.virgin_america.options} toolTipContent={'Shows the count of negative reasons per category for Virgin America Airlines'} />
                }
              </Container>
            </div>
          </Col>
        </Row>
      </>
    )
  }