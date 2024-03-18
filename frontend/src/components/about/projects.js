import React, {useEffect, useState} from 'react';
import axios from 'axios';
import './css/projects.css'
const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID


function Projects() {
    const [projects, setProjects] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/projects/`)
            .then(response => {
                setProjects(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <div className="projects-container">
            <h2>Projects</h2>
            <div className="projects-list">
                {projects.map((project, index) => (
                    <div key={index} className="projects-item">
                        <div className="projects-link">
                            <h2>{project.title}</h2>
                            <p><strong>link:</strong> <a href={project.link}>{project.link}</a></p>
                            <p>
                                {project.description.split('\n').map((line, index) => (
                                    <React.Fragment key={index}>
                                        {line}
                                        <br/>
                                    </React.Fragment>
                                ))}
                            </p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Projects;