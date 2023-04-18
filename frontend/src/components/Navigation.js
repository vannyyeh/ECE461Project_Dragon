import React from 'react';
import styled from '@emotion/styled';
import { useNavigate } from 'react-router-dom';
import { useAuthentification } from './AuthentificationContext';
import { NavigationHeader, NavigationPage } from '../styles/GlobalStyles';

export const Navigation = ({}) => {
	const { admin, authorized } = useAuthentification();

	return (
		<NavigationHeader>
			<NavText text={'Home'} url={'/'} />
			{authorized ? <NavText text={'Projects'} url={'/projects/'} /> : null}
			{admin ? <NavText text={'Admin'} url={'/admin/'} /> : null}
			<NavText text={'Register'} url={'/register/'} />
		</NavigationHeader>
	);
};

const NavText = ({ text, url }) => {
	let navigate = useNavigate();
	return (
		<NavigationPage
			style={{ justifyContent: 'left' }}
			onMouseEnter={(e) => {
				e.target.style.color = 'red';
			}}
			onMouseLeave={(e) => {
				e.target.style.color = 'black';
			}}
			onClick={() => {
				navigate(url);
			}}
		>
			{text}
		</NavigationPage>
	);
};
