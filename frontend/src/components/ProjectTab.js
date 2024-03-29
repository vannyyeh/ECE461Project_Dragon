import { Button, TextField } from '@mui/material';
import React, { useState } from 'react';
import Api from './Api';
import styled from 'styled-components';

const ProjectTab = ({ title, description, users, hwSets, projectID, setLoaded }) => {
	const [quantity1, setQuantity1] = useState(50);
	const [quantity2, setQuantity2] = useState(0);

	return (
		<ProjectTabContainer>
			<LeftContainer>
				<CompressText style={{ fontSize: '25px', width: '225px' }}>{title}</CompressText>
				<CompressText style={{ fontSize: '15px', width: '110px' }}>{description}</CompressText>
				<CompressText style={{ fontSize: '15px', width: '110px' }}>{users.join(', ')}</CompressText>
			</LeftContainer>
			<RightContainer>
				<QuantityHandleContainer>
					{hwSets.map((hwSet) => (
						<QuantityHandler
							key={hwSet.hwID}
							hwID={hwSet.hwID}
							projectID={projectID}
							title={hwSet.name}
							capacity={hwSet.capacity}
							availability={hwSet.availability}
							setLoaded={setLoaded}
						/>
					))}
				</QuantityHandleContainer>
			</RightContainer>
		</ProjectTabContainer>
	);
};

const QuantityHandler = ({ title, capacity, availability, hwID, projectID, setLoaded }) => {
	const [availabilityChange, setAvailabilityChange] = useState(0);

	return (
		<div style={{ display: 'flex', flexDirection: 'inline', alignItems: 'center', width: '500px' }}>
			<div style={{ display: 'flex', flexDirection: 'column', paddingLeft: '25px', fontSize: '25px' }}>
				{title}: {availability}/{capacity}
			</div>
			<TextField
				type='number'
				style={{ margin: '5px', fontSize: '25px', minWidth: '100px' }}
				value={availabilityChange}
				onChange={(e) => {
					setAvailabilityChange(parseInt(e.target.value));
				}}
			/>
			<CheckButton
				text={'check in'}
				availabilityChange={availabilityChange}
				inVal={1}
				title={title}
				hwID={hwID}
				projectID={projectID}
				setLoaded={setLoaded}
			/>
			<CheckButton
				text={'check out'}
				availabilityChange={availabilityChange}
				inVal={-1}
				title={title}
				hwID={hwID}
				projectID={projectID}
				setLoaded={setLoaded}
			/>
		</div>
	);
};

const CheckButton = ({ text, hwID, projectID, availabilityChange, inVal, setLoaded }) => {
	const buttonPress = async () => {
		let res = await Api.patch('/patch_hardware_set/', {
			hwID: hwID,
			projectID: projectID,
			availabilityChange: inVal * availabilityChange,
		});
		setLoaded(false);
		console.log(res);
	};

	return (
		<Button
			style={{
				backgroundColor: 'gray',
				color: 'white',
				padding: '5px',
				margin: '4px',
				borderRadius: '5px',
				cursor: 'pointer',
				userSelect: 'none',
			}}
			onMouseOver={(e) => (e.target.style.background = 'green')}
			onMouseLeave={(e) => (e.target.style.background = 'gray')}
			onClick={() => buttonPress()}
		>
			{text}
		</Button>
	);
};

export default ProjectTab;

const ProjectTabContainer = styled.div`
	background-color: antiquewhite;
	margin: 10px;
	padding: 5px;
	display: flex;
	align-items: center;
	border: 4px solid black;
`;

const QuantityHandleContainer = styled.div`
	display: flex;
	flex-direction: column;
	padding-left: 25px;
	font-size: 25px;
	marginright: auto;
`;

const CompressText = styled.div`
	align-items: center;
	display: flex;
	flex-shrink: 1;
	flex-wrap: wrap;
	height: 150px;
	overflow: auto;
	padding-left: 25px;
	textalign: center;
`;

const LeftContainer = styled.div`
	display: flex;
	flex-direction: inline;
	align-items: center;
	margin-right: auto;
	margin-left: 25px;
`;

const RightContainer = styled.div`
	display: flex;
	flex-direction: inline;
	align-items: center;
	margin-right: 35px;
	margin-left: auto;
`;
