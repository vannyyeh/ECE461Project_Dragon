import React from 'react';

export const UserPortal = () => {
	return (
		<html>
			<head>
				<title>Dragon</title>
				<link href='./stylesheet.css' rel='stylesheet' />
			</head>
			<body>
				<div>
					<h1>
						Hello <span id='username'></span>!
					</h1>
				</div>
				<script src='./script.js'></script>
			</body>
		</html>
	);
};
