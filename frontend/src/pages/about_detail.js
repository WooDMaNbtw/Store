import React, {Component} from 'react';
import {Col, Container, Nav, Row, Tab} from "react-bootstrap";
import './about_detail.css';
import Experience from "../components/about/experience";
import Header from "../components/header";
import ExperienceDetail from "../components/about/experience_detail";
import {Link} from "react-router-dom";
class AboutDetail extends Component {
    render() {
        return (
            <>
                <Header/>
                <Container className={"mt-3"}>
                    <Tab.Container id="ledt-tabs-example">
                        <Row>
                            <Col sm={3}>
                                <Nav variant="pills" className="flex-column mt-2 custom-nav">
                                    <Nav.Item>
                                        <Nav.Link>
                                            <Link to={`/`} className="experience-link">
                                                {"<- Back"}
                                            </Link>
                                        </Nav.Link>
                                    </Nav.Item>
                                </Nav>
                            </Col>
                            <Col sm={9}>
                                <Tab.Content className="mt-2">
                                    <Tab.Pane>
                                        <ExperienceDetail/>
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

export default AboutDetail;