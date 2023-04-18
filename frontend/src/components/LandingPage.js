import React, { useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { InputBox } from '../inputs/InputBox';
import { CheckInButton, Header1, Header2, PageDiv, Wrapper, InputBoxContainer } from '../styles/GlobalStyles';
import { Stack, TextField, Button } from '@mui/material';
import Api from './Api';
import { useAuthentification } from './AuthentificationContext';
import { Navigation } from './Navigation';

export const LandingPage = () => {
	let navigate = useNavigate();

	const [userID, setUserID] = useState('');
	const [password, setPassword] = useState('');
	const [errorMessage, setErrorMessage] = useState('');
	//const url = process.env.REACT_APP_BASE_URL

	const { loginUser, authorized, logoutUser } = useAuthentification();

	const handleLogin = async () => {
		if (!userID) {
			setErrorMessage('Please enter a username');
			return;
		}

		if (!password) {
			setErrorMessage('Please enter a password');
			return;
		}
		try {
			let res = await Api.patch('/login_user/', {
				userID: userID,
				password: password,
			});

			if (res.status === 200) {
				loginUser(userID, res.data.admin);
				navigate('/projects');
			} else if (res.status === 204) {
				alert('Incorrect userID or password');
			}
		} catch (error) {
			alert('userID does not exist');
		}
	};

	function registerNavigation() {
		navigate(`/register`);
	}

	return (
		<PageDiv>
			<Navigation />
			<Header1>
				<text>Dragon</text>
				<link href='./stylesheet.css' rel='stylesheet' />
			</Header1>
			<Header2>
				<Wrapper>
					{!authorized ? (
						<>
							<h1>Welcome to the Dragon Check-in System!</h1>
							<Stack>
								<InputBoxContainer>
									<p>User ID:</p>
									<TextField
										value={userID}
										type='string'
										id='outlined-basic'
										label='Enter Your User ID'
										variant='outlined'
										onChange={(e) => {
											setUserID(e.target.value);
											setErrorMessage('');
										}}
									/>
								</InputBoxContainer>
								<InputBoxContainer>
									<p>Password:</p>
									<TextField
										value={password}
										type='password'
										id='outlined-basic'
										label='Enter Your Password'
										variant='outlined'
										onChange={(e) => {
											setPassword(e.target.value);
											setErrorMessage('');
										}}
									/>
								</InputBoxContainer>
								<br />
								<InputBoxContainer>
									<Button
										variant='contained'
										size='large'
										onClick={handleLogin}
										sx={{ width: '200px' }}
									>
										LogIn
									</Button>
								</InputBoxContainer>
							</Stack>
							<br />
							<br />
							<a style={{ cursor: 'pointer' }} onClick={() => registerNavigation()}>
								I am a new user
							</a>
						</>
					) : (
						<>
							<h1>Welcome to the Dragon Check-in System!</h1>
							<h2>You are already logged in, would you like to sign out?</h2>
							<Button variant='contained' size='large' onClick={logoutUser} sx={{ width: '200px' }}>
								SignOut
							</Button>
						</>
					)}
				</Wrapper>
				<script src='./script.js'></script>
			</Header2>
		</PageDiv>
	);
};
