import React from 'react';
import ProjectTab from './ProjectTab';
import './Projects.css';

const projects = [
  {
    title: 'Project Name 1',
    description: 'list, of, authorized, users'
  },
  {
    title: 'Project Name 2',
    description: 'list, of, authorized, users'
  },
  {
    title: 'Project Name 3',
    description: 'list, of, authorized, users'
  }
];

function Projects() {
  return (
    <div>
      <h1>Projects</h1>
      <div className="projects-container">
          {projects.map(project => (
            <ProjectTab
                key = {project.title}
                title = {project.title}
                description = {project.description}
                />
            ))}
      </div>
    </div>
  );
}

export default Projects;