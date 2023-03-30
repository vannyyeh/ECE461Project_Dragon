import React, { useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { InputBox } from './inputs/InputBox';
import { CheckInButton, Header1, Header2, PageDiv, Wrapper, InputBoxContainer } from './styles/GlobalStyles';
import { Stack, TextField, Button } from "@mui/material"

export const LandingPage = () => {
    let navigate = useNavigate();

	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const [errorMessage, setErrorMessage] = useState('');
    //const url = process.env.REACT_APP_BASE_URL

	const handleLogin = () => {
    if (!username) {
      setErrorMessage('Please enter a username');
      return;
    }

    if (!password) {
      setErrorMessage('Please enter a password');
      return;
    }

    fetch(`$/login/${username}/${password}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.response === 'successfully logged in') {
          localStorage.setItem('user', data.userID);
          navigate('./components/Projects');
        } else {
          setErrorMessage(data.response);
        }
      })
      .catch((error) => {
        setErrorMessage('Error');
      });
  };


	function registerNavigation() {
		navigate(`/register`);
	}

	return (
		<PageDiv>
			<Header1>
				<text>Dragon</text>
				<link href='./stylesheet.css' rel='stylesheet' />
			</Header1>
			<Header2>
				<Wrapper>
					<h1>Welcome to Dragon Check-in System!</h1>
					<Stack>
					<InputBoxContainer>
                        <p>
                            Username:
                        </p>
                        <TextField
                            value={username}
                            type="string"
                            id="outlined-basic"
                            label="Enter Your Username"
                            variant="outlined"
                            onChange={(e) => {
                              setUsername(e.target.value);
                              setErrorMessage('');
                            }}
                          />
                      </InputBoxContainer>
                      <InputBoxContainer>
                        <p>
                            Password:
                        </p>
                        <TextField
                            value={password}
                            type="password"
                            id="outlined-basic"
                            label="Enter Your Password"
                            variant="outlined"
                            onChange={(e) => {
                              setPassword(e.target.value);
                              setErrorMessage('');
                            }}
                          />
                        </InputBoxContainer>
                        <br />
                        <InputBoxContainer>
                        <Button variant="contained" size="large" onClick={handleLogin} sx={{ width: '200px' }}>
                            LogIn
                        </Button>
                        </InputBoxContainer>
                    </Stack>
					<br /><br />
					<a style={{ cursor: 'pointer' }} onClick={() => registerNavigation()}>
						I am a new user
					</a>
				</Wrapper>
				<script src='./script.js'></script>
			</Header2>
		</PageDiv>
	);
};
