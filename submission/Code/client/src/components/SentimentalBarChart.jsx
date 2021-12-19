import React from 'react';
import { FaInfoCircle } from 'react-icons/fa';
import { Tooltip, OverlayTrigger } from 'react-bootstrap';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Legend,
  Tooltip as ToolT
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  ToolT,
  Legend
);

export default function SentimentalBarChart({ data, options, toolTipContent }) {
  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      {toolTipContent ?? '' }
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
        <div style={{ textAlign:'center' }}>
          <FaInfoCircle />
        </div>
        </OverlayTrigger>
      </div>
      <div style={{ padding: 20, minHeight: 500 }}>
        <Bar options={options} data={data} />
      </div>
    </>
  )
}

