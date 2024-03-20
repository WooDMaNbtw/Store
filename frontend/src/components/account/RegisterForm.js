import React, { useState } from 'react';
import { Form, Button, Container, Row, Col, Alert } from 'react-bootstrap';
import axios from 'axios';
import './css/AuthForm.css';
import {Link, Navigate} from "react-router-dom"; // Импорт стилей
const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

const RegisterForm = ({ onRegisterSuccess }) => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        confirmPassword: ''
    });
    const [errorMessage, setErrorMessage] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [isRegistered, setIsRegistered] = useState(false); // Состояние для определения, зарегистрирован ли пользователь


    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (formData.password !== formData.confirmPassword) {
                setErrorMessage('Passwords do not match');
                return;
            }
            const response = await axios.post(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/auth/users/`, formData);
            if (response.status === 200 || response.status === 204)
                setSuccessMessage('Registration successful. Please verify your email.');
                setIsRegistered(true);
            console.log(response.data)
        } catch (error) {
            console.error('Registration error:', error.message);
        }
    };

    if (isRegistered) {
        return <Navigate to="/sign-in" />;
    }

    return (
        <Container>
            <Row className="justify-content-md-center">
                <Col md="6">
                    <Form className="auth-form" onSubmit={handleSubmit}>
                        <h2>Sign-Up</h2>
                        <Form.Group controlId="formBasicEmail">
                            <Form.Control type="email" name="email" value={formData.email} onChange={handleInputChange}
                                          placeholder="Enter email" required/>
                        </Form.Group>

                        <Form.Group controlId="formBasicPassword">
                            <Form.Control type="password" name="password" value={formData.password}
                                          onChange={handleInputChange} placeholder="Password" required/>
                        </Form.Group>

                        {errorMessage && <p className="PassDontMatch" style={{ color: 'red' }}>{errorMessage}</p>}

                        <Form.Group controlId="formBasicConfirmPassword">
                            <Form.Control type="password" name="confirmPassword" value={formData.confirmPassword}
                                          onChange={handleInputChange} placeholder="Confirm Password" required/>
                        </Form.Group>

                        {successMessage && <Alert variant="success">{successMessage}</Alert>}
                        <Button variant="primary" type="submit">
                            Register
                        </Button>
                    </Form>
                    <div className="register-link">
                        <p>Already have an account? <Link to="/sign-in">Log in</Link></p>
                    </div>
                </Col>
            </Row>
        </Container>
    );
};

export default RegisterForm;
