import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { TextField, Button } from '@mui/material';
import { PageDiv, WrapperRegister, FormRegister } from './styles/GlobalStyles';
import Api from './Api.js';
import axios from 'axios';

export const Register = () => {
	const [response, setResponse] = useState('');
	const [errorMessage, setErrorMessage] = useState('');
	const [userId, setUserId] = useState('');
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const [confirmPassword, setConfirmPassword] = useState('');

	let navigate = useNavigate();
	function navigateHome() {
		navigate(`/`);
	}

	const checkStrongPassword = (password) => {
		if (password.length >= 12) {
			if (/^[A-Za-z0-9]*$/.test(password)) {
				return true;
			}
		}
		return false;
	};

	const handleSubmit = async (event) => {
		event.preventDefault();

		if (!userId) {
			setErrorMessage('Please enter a user ID');
		} else if (!username) {
			setErrorMessage('Please enter a username');
		} else if (!password) {
			setErrorMessage('Please enter a password');
		} else if (!confirmPassword) {
			setErrorMessage('Please confirm your password');
		} else if (!(confirmPassword === password)) {
			setErrorMessage('Passwords do not match');
		} else {
			let res = await Api.post('/add_user/', {
				userID: userId,
				username: username,
				password: password,
			});
			console.log(res.status);
			if (res.status === 201) {
				navigate(`/projects`);
			} else if (res.status === 204) {
				alert('account already exists');
			} else {
				alert('an error occurred when registering you.');
			}
		}
	};

	const handleUserIdChange = (event) => {
		setUserId(event.target.value);
	};

	const handleUsernameChange = (event) => {
		setUsername(event.target.value);
	};

	const handlePasswordChange = (event) => {
		setPassword(event.target.value);
	};

	const handleConfirmPasswordChange = (event) => {
		setConfirmPassword(event.target.value);
	};

	return (
		<PageDiv>
			<WrapperRegister>
				<div>
					<h1>Welcome to Registration</h1>
					<div style={{ color: 'red' }}> {errorMessage} </div>
					<form onSubmit={handleSubmit}>
						<FormRegister>
							<p>Enter User ID:</p>
							<TextField label='User ID' value={userId} onChange={handleUserIdChange} />
						</FormRegister>
						<FormRegister>
							<p>Enter Username:</p>
							<TextField label='Username' value={username} onChange={handleUsernameChange} />
						</FormRegister>
						<FormRegister>
							<p>Enter password:</p>
							<TextField label='Password' value={password} onChange={handlePasswordChange} />
						</FormRegister>
						<FormRegister>
							<p>Confirm your password:</p>
							<TextField
								label='Confirm Password'
								value={confirmPassword}
								onChange={handleConfirmPasswordChange}
							/>
						</FormRegister>
						<FormRegister>
							<Button type='submit' variant='contained' color='primary'>
								Register New Account
							</Button>
						</FormRegister>
					</form>
					<a style={{ cursor: 'pointer' }} onClick={() => navigateHome()}>
						Back to Home Page
					</a>
				</div>
				<script src='./script.js'></script>
			</WrapperRegister>
		</PageDiv>
	);
};
