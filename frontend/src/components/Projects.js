import React from 'react';
import ProjectTab from './ProjectTab';


const projects = [];

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