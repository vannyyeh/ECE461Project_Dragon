import React from 'react';
import styled from 'styled-components';

export const TestBackend = () => {
	function sendTestRequest() {}

	return (
		<PageDiv>
			<Wrapper>
				<div>
					<a style={{ userSelect: 'none', cursor: 'pointer' }} onClick={() => sendTestRequest()}>
						Backend Test
					</a>
				</div>
				<script src='./script.js'></script>
			</Wrapper>
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

const Wrapper = styled.div`
	background: #ffe4b5;
	margin: 24px auto;
	padding: 24px;
	border-radius: 20px;
	width: 60%;
`;
