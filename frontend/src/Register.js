import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { TextField, Button } from '@mui/material';
import { PageDiv, WrapperRegister, FormRegister } from './styles/GlobalStyles';

export const Register = () => {
	const [userId, setUserId] = useState('');
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const [confirmPassword, setConfirmPassword] = useState('');

	let navigate = useNavigate();
	function navigateHome() {
		navigate(`/`);
	}

	const checkStrongPassword = (password) => {
		if (password.lenth >= 12) {
			if (/^[A-Za-z0-9]*$/.test(password)) {
				console.log('strong password');
				return true;
			}
		}
		console.log('what');
		return false;
	};

	const handleSubmit = (event) => {
		event.preventDefault();
		console.log(password);
		console.log(confirmPassword);
		if (password === confirmPassword) {
			if (checkStrongPassword(password)) {
				console.log(`"Success!"`);
			} else {
				console.log("Passwords don't match!");
			}
		} else {
			console.log('what');
			console.log(password === confirmPassword);
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
					<form onSubmit={handleSubmit}>
						<FormRegister>
							<TextField label='User ID' value={userId} onChange={handleUserIdChange} />
							<TextField label='Username' value={username} onChange={handleUsernameChange} />
							<TextField label='Password' value={password} onChange={handlePasswordChange} />
							<TextField
								label='Confirm Password'
								value={confirmPassword}
								onChange={handleConfirmPasswordChange}
							/>
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
