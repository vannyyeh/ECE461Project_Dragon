import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import Api from './Api';
import { useNavigate } from 'react-router-dom';
import { useAuthentification } from './AuthentificationContext';
import { NavigationPage, Wrapper } from '../styles/GlobalStyles';
import { Navigation } from './Navigation';
import { CreateProject } from './CreateProject';
import ProjectTabAdmin from './ProjectTabAdmin';
import HardwareSetsTabAdmin from './HardwareSetsTabAdmin';
import { CreateHardwareSet } from './CreateHardwareSet';

const ProjectView = ({ projects }) => {
	return projects.map((project) => (
		<ProjectTabAdmin
			key={project.projectID}
			title={project.name}
			description={project.desc}
			users={project.users}
			grabHW={project.grabHW}
			join={project.join}
		/>
	));
};

const HardwareSetView = ({ hardwareSets }) => {
	return hardwareSets.map((hardwareSet) => (
		<HardwareSetsTabAdmin
			key={hardwareSet.hwID}
			name={hardwareSet.name}
			capacity={hardwareSet.capacity}
			availability={hardwareSet.availability}
			tiedProjects={hardwareSet.tiedProjects}
		/>
	));
};

const ViewHeader = ({ text, setView, bias, view }) => {
	return (
		<NavigationPage
			style={{ width: '250px', color: view === bias ? 'red' : 'black' }}
			onMouseEnter={(e) => {
				e.target.style.color = 'red';
			}}
			onMouseLeave={(e) => {
				e.target.style.color = view === bias ? 'red' : 'black';
			}}
			onClick={() => {
				setView(bias);
			}}
		>
			{text}
		</NavigationPage>
	);
};

const Admin = () => {
	let navigate = useNavigate();

	const [view, setView] = useState(true);
	const [projects, setProjects] = useState([]);
	const [hardwareSets, setHardwareSets] = useState([]);
	const [projectsLoaded, setProjectsLoaded] = useState(false);
	const [hardwareSetsLoaded, setHardwareSetsLoaded] = useState(false);

	const { authorized, admin } = useAuthentification();

	const requestAllProjects = async () => {
		let res = await Api.get(`/get_all_projects/${admin}`);
		console.log(res);
		setProjects(res.data.projects);
		setProjectsLoaded(true);
	};

	const requestAllHardwareSets = async () => {
		let res = await Api.get(`/get_all_hardware_sets/${admin}`);
		console.log(res);
		setHardwareSets(res.data.hardwareSets);
		setHardwareSetsLoaded(true);
	};

	useEffect(() => {
		if (admin) {
			requestAllProjects();
			requestAllHardwareSets();
		}
	}, [admin]);

	useEffect(() => {
		if (!projectsLoaded && admin) {
			requestAllProjects();
		}
		if (!hardwareSetsLoaded && admin) {
			requestAllHardwareSets();
		}
	}, [projectsLoaded, hardwareSetsLoaded]);

	return (
		<PageContainer>
			<Navigation />
			<PageTitle style={{ marginBottom: '20px' }}>Admin Portal</PageTitle>
			{admin ? (
				<>
					<ViewSelector>
						<ViewHeader text={'Projects'} setView={setView} bias={true} view={view} />
						<ViewHeader text={'Hardware Sets'} setView={setView} bias={false} view={view} />
					</ViewSelector>
					<Wrapper style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
						{view ? (
							<CreateProject setLoaded={setProjectsLoaded} />
						) : (
							<CreateHardwareSet setLoaded={setHardwareSetsLoaded} />
						)}
					</Wrapper>
					<ProjectContainer>
						{authorized && projectsLoaded && hardwareSetsLoaded ? (
							<>
								{view && projects ? <ProjectView projects={projects} /> : null}
								{!view && hardwareSets ? <HardwareSetView hardwareSets={hardwareSets} /> : null}
							</>
						) : authorized && !(projectsLoaded && hardwareSetsLoaded) ? (
							<PageTitle style={{ fontSize: '35px' }}>Loading...</PageTitle>
						) : (
							<PageTitle style={{ fontSize: '35px' }} onClick={navigate('/')}>
								You do not have permission to view this. Please login.
							</PageTitle>
						)}
					</ProjectContainer>
				</>
			) : authorized && !(projectsLoaded && hardwareSetsLoaded) ? (
				<PageTitle style={{ fontSize: '35px' }}>Loading...</PageTitle>
			) : (
				<PageTitle style={{ fontSize: '35px' }} onClick={navigate('/')}>
					You do not have permission to view this. Please login.
				</PageTitle>
			)}
		</PageContainer>
	);
};

export default Admin;

const PageTitle = styled.div`
	font-size: 50px;
`;

const ProjectQuery = styled.div`
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
`;

const ViewSelector = styled.div`
	font-weight: bold;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
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
