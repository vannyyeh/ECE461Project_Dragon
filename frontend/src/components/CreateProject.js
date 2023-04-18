import React, { useState } from 'react';
import { FormRegister } from '../styles/GlobalStyles';
import { Button, TextField } from '@mui/material';
import Api from './Api';
export const CreateProject = ({ setLoaded }) => {
	const [name, setName] = useState('');
	const [projectID, setProjectID] = useState('');
	const [desc, setDesc] = useState('');
	const [users, setUsers] = useState('');
	const [hardwareSets, setHardwareSets] = useState('');

	const createNewProject = async (event) => {
		event.preventDefault();
		if (name && projectID && desc) {
			let res = await Api.post('/add_project/', {
				name: name,
				projectID: projectID,
				desc: desc,
				users: users.replaceAll(' ', '').split(','),
				grabHW: hardwareSets.replaceAll(' ', '').split(','),
			});
			if (res.status === 201) {
				alert('project created!');
				setName('');
				setProjectID('');
				setDesc('');
				setUsers('');
				setHardwareSets('');

				setLoaded(false);
			} else {
				alert('project already exists.');
				setName('');
				setProjectID('');
				setDesc('');
				setUsers('');
				setHardwareSets('');
			}
		} else {
			alert('Please fill out the form.');
		}
	};

	return (
		<div>
			<form
				onSubmit={(e) => {
					createNewProject(e);
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
					<p>Enter Project ID:</p>
					<TextField
						label='Project ID'
						value={projectID}
						onChange={(e) => {
							setProjectID(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<p>Enter Description:</p>
					<TextField
						label='Description'
						value={desc}
						onChange={(e) => {
							setDesc(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<p>Enter Users in a Comma Separated List:</p>
					<TextField
						label='Users'
						value={users}
						onChange={(e) => {
							setUsers(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<p>Enter Hardware Sets, in a Comma Separated List:</p>
					<TextField
						label='Hardware Sets'
						value={hardwareSets}
						onChange={(e) => {
							setHardwareSets(e.target.value);
						}}
					/>
				</FormRegister>
				<FormRegister>
					<Button type='submit' variant='contained' color='primary'>
						Create New Project
					</Button>
				</FormRegister>
			</form>
		</div>
	);
};
