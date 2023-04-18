import React, { useEffect, useState } from 'react';
import ProjectTab from './ProjectTab';
import styled from 'styled-components';
import Api from './Api';
import { useNavigate } from 'react-router-dom';
import { useAuthentification } from './AuthentificationContext';
import { Button, TextField } from '@mui/material';
import { Header2, Wrapper } from '../styles/GlobalStyles';
import { Navigation } from './Navigation';

const Projects = () => {
	let navigate = useNavigate();

	const [queryProject, setQueryProject] = useState('');

	const [projects, setProjects] = useState([]);
	const [loaded, setLoaded] = useState(false);
	const { authorized, authUserID } = useAuthentification();

	const joinQueryProject = async () => {
		if (queryProject) {
			setLoaded(false);
			try {
				let res = await Api.patch(`/user_join_project/`, { projectID: queryProject, userID: authUserID });
				if (res.status == 200) {
					let resProjects = await Api.get(`/get_user_projects/${authUserID}`);
					if (resProjects.status == 200) {
						setProjects(resProjects.data.projects);
					}
				} else if (res.status == 204) {
					alert('You are already in this project!');
				}
				setQueryProject('');
				setLoaded(true);
			} catch (error) {
				console.log(error);
				setLoaded(true);
			}
		}
	};

	const requestProjects = async () => {
		let res = await Api.get(`/get_user_projects/${authUserID}`);
		console.log(res.data);
		setProjects(res.data.projects);
		setLoaded(true);
	};

	useEffect(() => {
		if (authUserID) {
			requestProjects();
		}
	}, [authUserID]);

	useEffect(() => {
		if (!loaded && authUserID) {
			requestProjects();
		}
		setLoaded(true);
	}, [loaded]);

	return (
		<PageContainer>
			<Navigation />
			<Wrapper style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
				<PageTitle>Project Portal</PageTitle>
				<ProjectQuery>
					<Header2 style={{ marginRight: '25px' }}>Query Project:</Header2>
					<TextField
						value={queryProject}
						id='outlined-basic'
						label='Requested Project ID'
						variant='outlined'
						onChange={(e) => {
							setQueryProject(e.target.value);
						}}
					/>
					<Button variant='contained' size='large' style={{ marginLeft: '25px' }} onClick={joinQueryProject}>
						Join
					</Button>
				</ProjectQuery>
			</Wrapper>
			<ProjectContainer>
				{authorized && loaded ? (
					projects.map((project) => (
						<ProjectTab
							key={project.projectID}
							projectID={project.projectID}
							title={project.name}
							description={project.desc}
							users={project.users}
							grabHW={project.grabHW}
							hwSets={project.grabHW}
							join={project.join}
							setLoaded={setLoaded}
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

const ProjectQuery = styled.div`
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
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
