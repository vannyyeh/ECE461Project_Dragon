import React from 'react';
import { useNavigate } from 'react-router-dom';
import { PageDiv, Wrapper } from './styles/GlobalStyles';

export const Register = () => {
	let navigate = useNavigate();

	function navigateHome() {
		navigate(`/`);
	}

	return (
		<PageDiv>
			<Wrapper>
				<div>
					<a style={{ cursor: 'pointer' }} onClick={() => navigateHome()}>
						Welcome to user registration
					</a>
				</div>
				<script src='./script.js'></script>
			</Wrapper>
		</PageDiv>
	);
};
