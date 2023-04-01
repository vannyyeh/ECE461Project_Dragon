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
		if (password.length >= 12) {
			if (/^[A-Za-z0-9]*$/.test(password)) {
				console.log('It is a strong password');
				return true;
			}
		}
		console.log('not strong');
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
		    fetch(`/register/${username}/${userId}/${password}/${confirmPassword}`)
            .then((response) => response.json())
            .then((data) => {
             if (data.response === 'New user created') {
               setUser(data.userId)
                  localStorage.setItem('user', data.userId)
                }
                alert(data.response)
            })
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
						<FormRegister >
						    <p>
                            Enter User ID:
                            </p>
							<TextField label='User ID' value={userId} onChange={handleUserIdChange} />
						</FormRegister>
						<FormRegister>
							<p>
                            Enter Username:
                            </p>
							<TextField label='Username' value={username} onChange={handleUsernameChange} />
						</FormRegister>
						<FormRegister>
							<p>
                            Enter password:
                            </p>
							<TextField label='Password' value={password} onChange={handlePasswordChange} />
						</FormRegister>
						<FormRegister>
							<p>
                            Confirm your password:
                            </p>
							<TextField
								label='Confirm Password'
								value={confirmPassword}
								onChange={handleConfirmPasswordChange}
							/>
						</FormRegister>
						<FormRegister>
							<Button type='submit' variant='contained' color='primary' >
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
