import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { InputBox } from './inputs/InputBox';
import { CheckInButton, Header1, Header2, PageDiv, Wrapper } from './styles/GlobalStyles';

export const LandingPage = () => {
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');

	let navigate = useNavigate();

	function registerNavigation() {
		navigate(`/register`);
	}

	return (
		<PageDiv>
			<Header1>
				<text>Dragon</text>
				<link href='./stylesheet.css' rel='stylesheet' />
			</Header1>
			<Header2>
				<Wrapper>
					<h1>Welcome to Dragon Check-in System!</h1>
					<h2>Enter your username and password</h2>

					<p>
						Username: <InputBox value={username} setValue={setUsername} />
					</p>
					<p>
						Password: <InputBox value={password} setValue={setPassword} />
					</p>

					<p id='username-error-message' style={{ display: 'none', color: 'red' }}>
						Please enter a username
					</p>
					<p id='password-error-message' style={{ display: 'none', color: 'red' }}>
						Please enter a password
					</p>
					<CheckInButton>Check in</CheckInButton>
					<br />
					<a style={{ cursor: 'pointer' }} onClick={() => registerNavigation()}>
						I am a new user
					</a>
				</Wrapper>
				<script src='./script.js'></script>
			</Header2>
		</PageDiv>
	);
};
