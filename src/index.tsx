import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import GravSim from './GravSim';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <GravSim />
  </React.StrictMode>
);