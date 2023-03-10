import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { LandingPage } from './LandingPage';
import { Register } from './register';
import { TestBackend } from './TestBackend';
import { UserPortal } from './UserPortal';

export default function Render() {
	return (
		<BrowserRouter>
			<Routes>
				<Route exact path='/' element={<LandingPage />} />
				<Route exact path='/register' element={<Register />} />
				<Route exact path='/userPortal' element={<UserPortal />} />
				<Route exact path='/testBackend' element={<TestBackend />} />
				<Route exact path='*' element={<NotFound />} />
			</Routes>
		</BrowserRouter>
	);
}

export const NotFound = () => {
	return <div>This is a 404 page</div>;
};
