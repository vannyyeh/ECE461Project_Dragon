import React, { useState } from 'react';
import { FormRegister } from '../styles/GlobalStyles';
import { Button, TextField } from '@mui/material';
import Api from './Api';

export const CreateHardwareSet = ({ setLoaded }) => {
	const [name, setName] = useState('');
	const [hwID, setHwID] = useState('');
	const [capacity, setCapacity] = useState(0);
	const [availability, setAvailability] = useState(0);

	const createNewHardwareSet = async (event) => {
		event.preventDefault();
		if (name && hwID && capacity && availability) {
			let res = await Api.post('/add_hardware_set/', {
				name: name,
				hwID: hwID,
				capacity: capacity,
				availability: availability,
			});
			if (res.status === 201) {
				alert('hardware set created!');
				setName('');
				setHwID('');
				setCapacity('');
				setAvailability('');

				setLoaded(false);
			} else {
				alert('hardware set already exists.');
				setName('');
				setHwID('');
				setCapacity('');
				setAvailability('');
			}
		} else {
			alert('Please fill out the form.');
		}
	};

	return (
		<div>
			<form
				onSubmit={(e) => {
					createNewHardwareSet(e);
				}}
			>
				<FormRegister>
					<p>Enter Name:</p>
					<TextField
						label='Name'
						value={name}
						onChange={(e) => {
							setName(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<p>Enter Hardware Set ID:</p>
					<TextField
						label='Hardware Set ID'
						value={hwID}
						onChange={(e) => {
							setHwID(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<p>Enter Capacity:</p>
					<TextField
						type='number'
						label='Capacity'
						value={capacity}
						onChange={(e) => {
							setCapacity(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<p>Enter Availability:</p>
					<TextField
						type='number'
						label='Availability'
						value={availability}
						onChange={(e) => {
							setAvailability(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<Button type='submit' variant='contained' color='primary'>
						Create New Hardware Set
					</Button>
				</FormRegister>
			</form>
		</div>
	);
};
