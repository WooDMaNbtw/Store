import React, {useEffect, useState} from 'react';
import axios from 'axios';
import './css/about.css'
import {Link} from "react-router-dom";
const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

function Experience() {
    const [experiences, setExperiences] = useState(null);
    const [loading, setLoading] = useState(true);


    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/biography/`)
            .then(response => {
                setExperiences(response.data);
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
        <div className="experience-container">
            <h2>Experience</h2>
            <div className="experience-list">
                {experiences.map((experience, index) => (
                    <div key={index} className="experience-item">
                        <Link to={`/experience/${experience.slug}`} className="experience-link">
                            <h2>{experience.title}</h2>
                            <h5><strong>Company:</strong> {experience.company}</h5>
                            <h5><strong>Position:</strong> {experience.position}</h5>
                            <p>
                                {experience.description.split('\n').map((line, index) => (
                                    <React.Fragment key={index}>
                                        {line}
                                        <br/>
                                    </React.Fragment>
                                ))}
                            </p>
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Experience;