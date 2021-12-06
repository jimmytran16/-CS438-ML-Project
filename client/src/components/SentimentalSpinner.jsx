import React from 'react'
import { Spinner } from 'react-bootstrap'

export default function SentimentalSpinner() {
    return (
        <div style={{ textAlign:'center', padding:15 }}>
            <Spinner animation="border" style={{ color: '#8BA8B7' }}/>
        </div>
    )
}