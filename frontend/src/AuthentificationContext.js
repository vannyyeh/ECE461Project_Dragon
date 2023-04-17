import React, { createContext, useContext, useEffect, useState } from 'react';

const AuthentificationContext = createContext();

export const AuthentificationProvider = ({ children }) => {
	const [authorized, setAuthorized] = useState(false);
	const [authUserID, setAuthUserID] = useState('');

	function loadAuth() {
		const authorized = Boolean(localStorage.getItem('authorized'));
		const authUserID = localStorage.getItem('authUserID');
		setAuthorized(authorized);
		setAuthUserID(authUserID);
	}

	useEffect(() => {
		window.addEventListener('storage', loadAuth);
		loadAuth();
	}, []);

	const loginUser = (userID) => {
		setAuthorized(true);
		setAuthUserID(userID);
		localStorage.setItem('authorized', true);
		localStorage.setItem('authUserID', userID);
	};

	// const logoutUser = () => {
	// 	setAuthorized(false);
	// 	setAuthUserID('');
	// 	localStorage.setItem('authorized', false);
	// 	localStorage.setItem('authUserID', '');
	// };

	return (
		<AuthentificationContext.Provider value={{ authorized, authUserID, loginUser, loadAuth }}>
			{children}
		</AuthentificationContext.Provider>
	);
};

export function useAuthentification() {
	const context = useContext(AuthentificationContext);
	return context;
}
