import React, { createContext, useContext, useEffect, useState } from 'react';

const AuthentificationContext = createContext();

export const AuthentificationProvider = ({ children }) => {
	const [authorized, setAuthorized] = useState(false);
	const [admin, setAdmin] = useState(false);
	const [authUserID, setAuthUserID] = useState('');

	function loadAuth() {
		const authorizedLocal = Boolean(localStorage.getItem('authorized'));
		const adminLocal = Boolean(localStorage.getItem('authorized'));
		const authUserIDLocal = localStorage.getItem('authUserID');
		setAuthorized(authorizedLocal);
		setAdmin(adminLocal);
		setAuthUserID(authUserIDLocal);
	}

	useEffect(() => {
		window.addEventListener('storage', loadAuth);
		loadAuth();
	}, []);

	const loginUser = (userID, admin) => {
		setAuthorized(true);
		setAdmin(admin);
		setAuthUserID(userID);
		localStorage.setItem('authorized', true);
		localStorage.setItem('admin', admin);
		localStorage.setItem('authUserID', userID);
	};

	const logoutUser = () => {
		setAuthorized(false);
		setAdmin(false);
		setAuthUserID('');
		localStorage.setItem('authorized', false);
		localStorage.setItem('admin', false);
		localStorage.setItem('authUserID', '');
	};

	return (
		<AuthentificationContext.Provider value={{ authorized, authUserID, loginUser, logoutUser, loadAuth, admin }}>
			{children}
		</AuthentificationContext.Provider>
	);
};

export function useAuthentification() {
	const context = useContext(AuthentificationContext);
	return context;
}
