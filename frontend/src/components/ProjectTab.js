import React from 'react';

import { TextField, Button } from '@mui/material';

function HWSet(props) {
  const [numerator, setNumerator] = React.useState('0');
  const [denominator, setDenominator] = React.useState('100');
  const [inputValue, setInputValue] = React.useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleCheckIn = () => {
    const newValue = parseInt(numerator) - parseInt(inputValue);
    setNumerator(newValue < 0 ? '0' : newValue.toString());
    setInputValue('');
  };

  const handleCheckOut = () => {
    const newValue = parseInt(numerator) + parseInt(inputValue);
    setNumerator(newValue > parseInt(denominator) ? denominator : newValue.toString());
    setInputValue('');
  };

  return (
    <div className="hwset">
      <div className="hwset-label">
        <label className="label">HWSet {props.number}</label>
        <span className="fraction">{numerator}/{denominator}</span>
      </div>
      <TextField
        className="text-field"
        label="Enter Quantity"
        variant="outlined"
        value={inputValue}
        onChange={handleInputChange}
      />
      <Button variant="contained" color="primary" onClick={handleCheckIn}>
        Check In
      </Button>
      <Button variant="contained" color="secondary" onClick={handleCheckOut}>
        Check Out
      </Button>
    </div>
  );
}



function ProjectTab(props) {

  const handleJoinClick = () => {
    // function to handle Join button click
    console.log(`Join clicked for project ${props.title}`);
  };

  return (
    <div className="project-tab">
      <div className="title">{props.title}</div>
      <div className="description">{props.description}</div>
      <div className="hwsets">
        <HWSet number="1:" />
        <HWSet number="2:" />
      </div>
      <Button variant="contained" color="primary" onClick={handleJoinClick}>
        Join
      </Button>
    </div>
  );
}

export default ProjectTab;