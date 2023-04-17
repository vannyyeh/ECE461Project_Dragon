import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { LandingPage } from './LandingPage';
import { Register } from './Register';
import Projects from './components/Projects';
import { AuthentificationProvider } from './AuthentificationContext';

export default function Render() {
	return (
		<AuthentificationProvider>
			<BrowserRouter>
				<Routes>
					<Route exact path='/' element={<LandingPage />} />
					<Route exact path='/projects' element={<Projects />} />
					<Route exact path='/register' element={<Register />} />
					<Route exact path='*' element={<NotFound />} />
				</Routes>
			</BrowserRouter>
		</AuthentificationProvider>
	);
}

export const NotFound = () => {
	return <div>This is a 404 page</div>;
};
