import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './css/experience_detail.css'
import { useParams } from 'react-router-dom';
import Header from "../header";
import {Col, Container, Nav, Row, Tab} from "react-bootstrap";
import { convertDateToWords } from '../services/DateToWords';
const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

function ExperienceDetail() {
    const [experience, setExperience] = useState(null);
    const [loading, setLoading] = useState(true);
    const { slug } = useParams();

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/biography/${slug}/`)
            .then(response => {
                setExperience(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setLoading(false);
            });
    }, [slug]);

    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <>
            <Header/>
            <Container className={"mt-3"}>
                <Tab.Container id="ledt-tabs-example" defaultActiveKey="first">
                    <Row>
                        <Col sm={3}>
                            <Nav variant="pills" className="flex-column mt-2 custom-nav">
                                <Nav.Item>
                                    <Nav.Link eventKey="first">About me</Nav.Link>
                                </Nav.Item>
                                <Nav.Item>
                                    <Nav.Link href={"/"}>Back</Nav.Link>
                                </Nav.Item>
                            </Nav>
                        </Col>
                        <Col sm={9}>
                            <div className="experience-container">
                                <div className="experience-detail">
                                    <h2>{experience.title}</h2>
                                    <h5><strong>Company:</strong> {experience.company}</h5>
                                    <h5><strong>Position:</strong> {experience.position}</h5>
                                    <p><strong>
                                        {convertDateToWords(experience.begin_time)} {" - "}
                                        {experience.end_time === null
                                            ? "CURRENT TIME"
                                            : convertDateToWords(experience.end_time)}
                                    </strong></p>
                                    <p>{experience.description.split('\n').map((line, index) => (
                                        <React.Fragment key={index}>
                                        {line}
                                            <br/>
                                        </React.Fragment>
                                    ))}</p>

                                </div>
                            </div>
                            {experience.projects.length > 0
                                ?
                                (
                                    <>
                                        <h2 className="projects-header">Related projects</h2>
                                        <div className="experience-container">
                                            <div className="experience-detail">
                                                {experience.projects.map((project, index) => (
                                                    <div key={index}>
                                                        <h3>{project.title}</h3>
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
                                                ))}
                                            </div>
                                        </div>
                                    </>
                                )
                                :
                                <></>
                            }
                        </Col>
                    </Row>
                </Tab.Container>
            </Container>
        </>
    );
}

export default ExperienceDetail;
