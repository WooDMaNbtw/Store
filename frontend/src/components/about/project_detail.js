import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './css/project_detail.css'
import { useParams } from 'react-router-dom';
import Header from "../header";
import {Col, Container, Nav, Row, Tab} from "react-bootstrap";

function ProjectDetail() {
    const [project, setProject] = useState(null);
    const [loading, setLoading] = useState(true);
    const { id } = useParams();

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/projects/${id}/`)
            .then(response => {
                setProject(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setLoading(false);
            });
    }, [id]);

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
                                    <Nav.Link eventKey="first">Project</Nav.Link>
                                </Nav.Item>
                                <Nav.Item>
                                    <Nav.Link href={"/"}>Back</Nav.Link>
                                </Nav.Item>
                            </Nav>
                        </Col>
                        <Col sm={9}>
                            <div className="experience-container">
                                <div className="experience-detail">
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
                        </Col>
                    </Row>
                </Tab.Container>
            </Container>
        </>
    );
}

export default ProjectDetail;
