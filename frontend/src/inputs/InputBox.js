import React from 'react';
export const InputBox = ({ value, setValue }) => {
	return (
		<input
			type='text'
			value={value}
			onChange={(e) => {
				setValue(e.target.value);
			}}
		/>
	);
};
