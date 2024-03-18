import React, {useEffect, useState} from 'react';
import {Button, Container, Dropdown, Form, FormControl, Nav, Navbar} from "react-bootstrap";
import logo from '../logo.svg'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link, useLocation} from "react-router-dom";
import axios from "axios";
import userIcon from "../user.png"
import './header.css'

const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID


const Header = ({ onQueryChange }) => {
    const location = useLocation();
    const [searchQuery, setSearchQuery] = useState("");
    const [account, setAccount] = useState(null)
    const [showDropdown, setShowDropdown] = useState(false);


    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/auth/users/me/`, {
            headers: {
                Authorization: "JWT " + localStorage.getItem('access_token')
            }
        })
            .then(response => {
                setAccount(response.data);
            })
            .catch(error => {
                console.log("Unauthorized! ", error);
            });
    }, []);

    const handleDropdownBlur = () => {
        setShowDropdown(false);
    };

    const handleDropdownFocus = () => {
        setShowDropdown(true);
    };

    const handleSearchChange = (event) => {
        setSearchQuery(event.target.value);
    };

    const handleSearchSubmit = (event) => {
        event.preventDefault();
        const url = new URL(window.location.href);
        url.searchParams.set('query', searchQuery);
        window.location.href = url.toString();
        onQueryChange(searchQuery);
    }

    const isBlogPage = location.pathname === '/blog';

    return (
        <>
            <Navbar sticky='top' collapseOnSelect expand="md" bg="dark" variant="dark">
                <Container>
                    <Navbar.Brand href="/">
                        <img
                            src={logo}
                            height="40"
                            width="40"
                            className="d-inline-block align-top"
                            alt="logo"
                            style={{scale: '1.8'}}
                        />
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav className="me-auto">
                            <Dropdown show={showDropdown} onMouseEnter={() => setShowDropdown(true)} onMouseLeave={() => setShowDropdown(false)}>
                                <Dropdown.Toggle variant="link" id="dropdown-basic" onFocus={handleDropdownFocus} onBlur={handleDropdownBlur}>
                                    <img
                                        src={userIcon}
                                        style={{
                                            color: 'white',
                                            background: 'white',
                                            marginRight: '5px',
                                            marginTop: '5px',
                                            width: '20px',
                                            scale: '2',
                                            borderRadius: '15px',
                                            height: 'auto'
                                        }}
                                    />
                                </Dropdown.Toggle>

                                {account !== null ? (
                                    <Dropdown.Menu style={{ backgroundColor: 'white', color: 'black' }}>
                                        <Dropdown.Item>
                                            <span
                                                className='user-email'>{account.email}
                                            </span>
                                        </Dropdown.Item>
                                    </Dropdown.Menu>
                                ) : (
                                    <Dropdown.Menu style={{ backgroundColor: 'white', color: 'black' }}>
                                        <Dropdown.Item as={Link} to="/sign-in">Sign-in</Dropdown.Item>
                                    </Dropdown.Menu>
                                )}
                            </Dropdown>

                            <Nav.Link as={Link} to="/" style={{ scale: "1.2", marginInline: '10px', marginTop: "5px" }}> Home </Nav.Link>
                            <Nav.Link as={Link} to="/blog" style={{ scale: "1.2", marginRight: '10px', marginTop: "5px" }}> Blog </Nav.Link>
                        </Nav>
                        {isBlogPage && (
                            <Form className='d-flex' onSubmit={handleSearchSubmit}>
                                <FormControl
                                    type="text"
                                    placeholder="Search"
                                    className="me-sm-2"
                                    value={searchQuery}
                                    onChange={handleSearchChange}
                                />
                                <Button type="submit" variant="outline-info"> Search </Button>
                            </Form>
                        )}
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

export default Header;