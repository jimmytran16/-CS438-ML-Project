import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, LinearScale, Title } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend, LinearScale, Title);

export default function SentimentalDoughnutChart({ data, options }) {
    return (
        <div style={{ padding: 20 }}>
            <Doughnut data={data} options={options} />
        </div>
    )
}

