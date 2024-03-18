import React, {Component} from 'react';
import Header from "../components/header";
import {Container} from "react-bootstrap";

class Contacts extends Component {
    render() {
        return (
            <>
                <Header/>
                <Container>
                    HelloWorld!
                </Container>
            </>
        );
    }
}

export default Contacts;