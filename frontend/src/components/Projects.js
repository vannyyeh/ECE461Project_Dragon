import React, { useEffect, useState } from 'react';
import ProjectTab from './ProjectTab';
import styled from 'styled-components';
import Api from '../Api';
import { useNavigate } from 'react-router-dom';
import { useAuthentification } from '../AuthentificationContext';
import { TextField } from '@mui/material';
import { Wrapper } from '../styles/GlobalStyles';

const getProjects = async () => {
	let res = Api.get('/');
};

const Projects = () => {
	let navigate = useNavigate();

	const [queryProject, setQueryProject] = useState('');

	const [projects, setProjects] = useState([]);
	const [loaded, setLoaded] = useState(false);
	const { authorized, authUserID, loadAuth } = useAuthentification();

	const requestProjects = async () => {
		let res = await Api.get(`/get_user_projects/${authUserID}`);
		setProjects(res.data.projects);
		setLoaded(true);
	};

	useEffect(() => {
		if (authUserID) {
			requestProjects();
		}
	}, [authUserID]);

	return (
		<PageContainer>
			{/* <Wrapper style={{ flex: 'display', flexDirection: 'row', marginLeft: 'auto' }}> */}
			<PageTitle>Project Portal</PageTitle>
			{/* going to put the query function here to join projects*/}
			{/* <TextField
					value={queryProject}
					id='outlined-basic'
					label='Requested Project ID'
					variant='outlined'
					onChange={(e) => {
						setQueryProject(e.target.value);
					}}
				/> */}
			{/* </Wrapper> */}
			<ProjectContainer>
				{authorized && loaded ? (
					projects.map((project) => (
						<ProjectTab
							key={project.projectID}
							title={project.name}
							description={project.desc}
							users={project.users}
							grabHW={project.grabHW}
							join={project.join}
						/>
					))
				) : authorized && !loaded ? (
					<PageTitle style={{ fontSize: '35px' }}>Loading...</PageTitle>
				) : (
					<PageTitle style={{ fontSize: '35px' }} onClick={navigate('/')}>
						You do not have permission to view this. Please login.
					</PageTitle>
				)}
			</ProjectContainer>
		</PageContainer>
	);
};

export default Projects;

const PageTitle = styled.div`
	font-size: 50px;
`;

const PageContainer = styled.div`
	display: flex;
	align-items: center;
	flex-direction: column;
`;

const ProjectContainer = styled.div`
	display: flex;
	align-items: center;
	flex-direction: column;
`;
