import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { TextField, Button } from '@mui/material';
import { PageDiv, WrapperRegister, FormRegister } from './styles/GlobalStyles';


export const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

	let navigate = useNavigate();

	function navigateHome() {
		navigate(`/`);
	}

	const handleSubmit = (event) => {
        event.preventDefault();
        if (password !== confirmPassword) {
          alert("Passwords don't match!");
        } else {
          alert(`"Success!"`);
        }
    };

    const handleUserIdChange = (event) => {
        setUsername(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleConfirmPasswordChange = (event) => {
        setConfirmPassword(event.target.value);
    };


	return (
		<PageDiv>
			<WrapperRegister>
				<div>
				    <h1>Welcome to Registration</h1>
					<form onSubmit={handleSubmit}>
					    <FormRegister>
                        <TextField
                          label="User ID"
                          value={username}
                          onChange={handleUserIdChange}
                        />
                        <TextField
                          label="Password"
                          type="password"
                          value={password}
                          onChange={handlePasswordChange}
                        />
                        <TextField
                          label="Confirm Password"
                          type="password"
                          value={confirmPassword}
                          onChange={handleConfirmPasswordChange}
                        />
                        <Button type="submit" variant="contained" color="primary">
                            Register New Account
                        </Button>
                        </FormRegister>
                    </form>
                    <a style={{ cursor: 'pointer' }} onClick={() => navigateHome()}>
						Back to Home Page
				    </a>
				</div>
				<script src='./script.js'></script>
			</WrapperRegister>
		</PageDiv>
	);
};
