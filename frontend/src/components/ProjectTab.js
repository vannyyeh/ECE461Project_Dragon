import { Button, TextField } from '@mui/material';
import React, { useEffect, useState } from 'react';
import Api from '../Api';
import styled from 'styled-components';
import { useAuthentification } from '../AuthentificationContext';
import { useNavigate } from 'react-router-dom';

const ProjectTab = ({ title, description }) => {
	const [quantity1, setQuantity1] = useState(50);
	const [quantity2, setQuantity2] = useState(0);
	return (
		<ProjectTabContainer>
			<LeftContainer>
				<CompressText style={{ fontSize: '25px', width: '225px' }}>{title}</CompressText>
				<CompressText style={{ fontSize: '15px', width: '110px' }}>{description}</CompressText>
			</LeftContainer>
			<RightContainer>
				<div style={{ display: 'flex', flexDirection: 'column', paddingLeft: '25px', fontSize: '25px' }}>
					<p>HWSet1: {quantity1}/100</p>
					<p>HWSet2: {quantity2}/100</p>
				</div>
				<QuantityHandleContainer>
					<QuantityHandler quantity={quantity1} setQuantity={setQuantity1} title={title} />
					<QuantityHandler quantity={quantity2} setQuantity={setQuantity2} title={title} />
				</QuantityHandleContainer>
				<JoinLeaveButton title={title} />
			</RightContainer>
		</ProjectTabContainer>
	);
};

const QuantityHandler = ({ quantity, setQuantity, title }) => {
	const [tempVal, setTempVal] = useState(0);

	return (
		<div style={{ display: 'flex', flexDirection: 'inline', alignItems: 'center', width: '250px' }}>
			<TextField
				type='number'
				style={{ margin: '5px', fontSize: '25px', width: '140px' }}
				value={tempVal}
				onChange={(e) => {
					setTempVal(parseInt(e.target.value));
				}}
			/>
			<CheckButton
				text={'check in'}
				tempVal={tempVal}
				quantity={quantity}
				setQuantity={setQuantity}
				inVal={1}
				title={title}
			/>
			<CheckButton
				text={'check out'}
				tempVal={tempVal}
				quantity={quantity}
				setQuantity={setQuantity}
				inVal={-1}
				title={title}
			/>
		</div>
	);
};

const CheckButton = ({ text, tempVal, quantity, setQuantity, inVal, title }) => {
	const buttonPress = async () => {
		setQuantity(parseInt(quantity) + parseInt(inVal) * tempVal);
		if (tempVal !== 0) {
			if (parseInt(inVal) === 1) {
				// need to route through hwID, and projectID
				let res = await Api.patch('/patch_hardware_set/', {
					hwID: hwID,
					projectID: projectID,
					availabilityChange: availabilityChange,
				});
			} else {
				let res = await Api.get(`/patch_hardware_set/${title}/${tempVal}/`);
				alert(res.data.msg);
			}
		}
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

const JoinLeaveButton = ({ title }) => {
	const [joined, setJoined] = useState(false);

	const buttonPress = async () => {
		setJoined(!joined);
		if (!joined) {
			let res = await Api.get(`/join/${title}/`);
			alert(res.data.msg);
		} else {
			let res = await Api.get(`/leave/${title}/`);
			alert(res.data.msg);
		}
	};

	function buttonLeave(e) {
		if (!joined) {
			e.target.style.background = 'gray';
		}
	}

	return (
		<Button
			style={{
				backgroundColor: 'gray',
				borderRadius: '5px',
				color: 'white',
				cursor: 'pointer',
				marginLeft: '40px',
				marginRight: '40px',
				marginRight: 'auto',
				padding: '5px',
				scale: '1.75',
				userSelect: 'none',
			}}
			onMouseOver={(e) => (e.target.style.background = 'green')}
			onMouseLeave={(e) => buttonLeave(e)}
			onClick={() => buttonPress()}
		>
			{joined ? 'Leave' : 'Join'}
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
