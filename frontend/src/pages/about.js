import React, {Component} from 'react';
import {Col, Container, Nav, Row, Tab} from "react-bootstrap";
import './about.css';
import Experience from "../components/about/experience";
import Header from "../components/header";
import Projects from "../components/about/projects";
import AboutInfo from "../components/about/about";
class About extends Component {
    render() {
        return (
            <>
                <Header/>
                <Container className={"mt-3"}>
                    <Tab.Container id="ledt-tabs-example" defaultActiveKey="first">
                        <Row>
                            <Col sm={3}>
                                <Nav variant="pills" className="flex-column mt-2 custom-nav">
                                    <Nav.Item>
                                        {/*Создать компонент About ME*/}
                                        <Nav.Link eventKey="first">About me</Nav.Link>
                                    </Nav.Item>
                                    <Nav.Item>
                                        {/*Создать компонент Experience*/}
                                        <Nav.Link eventKey="second">Experience</Nav.Link>
                                    </Nav.Item>
                                    <Nav.Item>
                                        {/*Создать компонент Projects*/}
                                        <Nav.Link eventKey="third">Projects</Nav.Link>
                                    </Nav.Item>
                                </Nav>
                            </Col>
                            <Col sm={9}>
                                <Tab.Content className="mt-2">
                                    <Tab.Pane eventKey="first">
                                        <AboutInfo/>
                                    </Tab.Pane>
                                    <Tab.Pane eventKey="second">
                                        <Experience/>
                                    </Tab.Pane>
                                    <Tab.Pane eventKey="third">
                                        <Projects/>
                                    </Tab.Pane>
                                </Tab.Content>
                            </Col>
                        </Row>
                    </Tab.Container>
                </Container>
            </>
        );
    }
}

export default About;