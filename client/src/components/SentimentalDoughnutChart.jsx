import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { Tooltip, OverlayTrigger } from 'react-bootstrap';
import { FaInfoCircle } from 'react-icons/fa';
import { Chart as ChartJS, ArcElement, Tooltip as TT, Legend, LinearScale, Title } from 'chart.js';

ChartJS.register(ArcElement, TT, Legend, LinearScale, Title);

export default function SentimentalDoughnutChart({ data, options, toolTipContent }) {
    const renderTooltip = (props) => (
        <Tooltip id="button-tooltip" {...props}>
            {toolTipContent ?? ''}
        </Tooltip>
    );

    return (
        <>
            <div>
                <OverlayTrigger
                    placement="top"
                    delay={{ show: 100, hide: 100 }}
                    overlay={renderTooltip}
                >
                    <div style={{ textAlign: 'center' }}>
                        <FaInfoCircle />
                    </div>
                </OverlayTrigger>
            </div>
            <div style={{ padding: 20 }}>
                <Doughnut data={data} options={options} />
            </div>
        </>
    )
}

