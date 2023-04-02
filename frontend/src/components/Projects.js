import React, { useEffect } from 'react';
import ProjectTab from './ProjectTab';
import styled from 'styled-components';
import Api from '../Api';

const projects = [
	{
		title: 'Project Na me 1',
		description: 'hellaidhaand',
	},
	{
		title: 'Project Name 2',
		description: 'list, of, authorized, users',
	},
	{
		title: 'Project Name 3',
		description: 'list, of, authorized, users',
	},
];

const getProjects = async () => {
	let res = Api.get('/');
};

const Projects = () => {
	// const [projects, Projects] = useState([]);

	console.log('hello everybody');

	// useEffect(() => {}, []);

	return (
		<PageContainer>
			<PageTitle>Project Portal</PageTitle>
			<ProjectContainer>
				{projects.map((project) => (
					<ProjectTab
						key={project.title}
						title={project.title}
						description={project.description}
						join={project.join}
					/>
				))}
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
