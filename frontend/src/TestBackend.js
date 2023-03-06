import React from 'react';
import { PageDiv, Wrapper } from './styles/GlobalStyles';

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
			</Wrapper>
		</PageDiv>
	);
};
