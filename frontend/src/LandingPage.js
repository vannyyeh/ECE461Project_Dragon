import React from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';

export const LandingPage = () => {
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
						Username: <input type='text' id='username-input' />
					</p>
					<p>
						Password: <input type='text' id='password-input' />
					</p>
					<p id='username-error-message' style={{ display: 'none', color: 'red' }}>
						Please enter a username
					</p>
					<p id='password-error-message' style={{ display: 'none', color: 'red' }}>
						Please enter a password
					</p>
					<CheckInButton onclick='storeName(); checkInput();'>Check in</CheckInButton>
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

const PageDiv = styled.div`
	font-size: 24px;
	text-align: center;
`;

const Header1 = styled.div`
	font-family: 'Copperplate', 'Courier New', sans-serif;
	font-size: 30px;
	color: #663399;
	text-align: center;
`;

const Header2 = styled.div`
	font-family: 'Monaco', 'Courier New', monospace;
	font-size: 22px;
	text-align: center;
`;

const Wrapper = styled.div`
	background: #ffe4b5;
	margin: 24px auto;
	padding: 24px;
	border-radius: 20px;
	width: 60%;
`;

const CheckInButton = styled.div`
	display: inline-block;
	padding: 12px 24px;
	background: linear-gradient(to bottom right, #e66465, #9198e5);
	color: white;
	border-radius: 15px;
	box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
	transition: all 0.3s ease;
`;
