import React, { useState, useEffect } from 'react';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import './css/AuthForm.css';
import {Link, Navigate, useLocation} from "react-router-dom";

const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

const LoginForm = ({ onLoginSuccess }) => {
    const location = useLocation(); // Получаем объект location для доступа к query-параметрам URL
    const [formData, setFormData] = useState({ email: '', password: '' });
    const [isLogin, setIsLogin] = useState(false); // Состояние для определения, зарегистрирован ли пользователь
    const [isRegistered, setIsRegistered] = useState(true); // Состояние для определения, зарегистрирован ли пользователь

    useEffect(() => {
        const searchParams = new URLSearchParams(location.search);
        const uid = searchParams.get('uid');
        const token = searchParams.get('token');
        if (uid && token) {
            // Если есть uid и token в query-параметрах URL, устанавливаем их в состояние formData
            setFormData({ ...formData, uid, token });
        }
    }, [location.search]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleActivation = async () => {
        try {
            if (!localStorage.getItem('access_token')) {
                const { uid, token } = formData;
                console.log(uid, token)
                if (uid !== undefined && token !== undefined){
                    const response = await axios.post(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/auth/users/activation/`, {uid, token});
                }
                setIsRegistered(false);
            }
            // Если ответ получен успешно (204), авторизируем пользователя через email и password
            const loginResponse = await axios.post(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/auth/jwt/create/`, formData);
            // Получаем токены из ответа и записываем их в localStorage
            console.log(loginResponse)
            const { refresh, access } = loginResponse.data;
            localStorage.setItem('refresh_token', refresh);
            localStorage.setItem('access_token', access);
            // Вызываем функцию обратного вызова для успешной авторизации
            setIsLogin(true)

        } catch (error) {
            console.error('Activation error:', error.message);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Вызываем функцию для активации пользователя
            await handleActivation();
        } catch (error) {
            console.error('Login error:', error.message);
        }
    };

    if (!isRegistered) {
        return <Navigate to="/sign-up/" />
    }

    if (isLogin) {
        return <Navigate to="/blog/" />;
    }

    return (
        <Container>
            <Row className="justify-content-md-center">
                <Col md="6">
                    <Form className="auth-form" onSubmit={handleSubmit}>
                        <h2>Sign-In</h2>
                        <Form.Group controlId="formBasicEmail">
                            <Form.Control type="email" name="email" value={formData.email} onChange={handleInputChange}
                                          placeholder="Enter email" required/>
                        </Form.Group>

                        <Form.Group controlId="formBasicPassword">
                            <Form.Control type="password" name="password" value={formData.password}
                                          onChange={handleInputChange} placeholder="Password" required/>
                        </Form.Group>

                        <Button variant="primary" type="submit">
                            Login
                        </Button>
                    </Form>
                    <div className="register-link">
                        <p>Don't have an account? <Link to="/sign-up">Register</Link></p>
                    </div>
                </Col>
            </Row>
        </Container>
    );
};

export default LoginForm;
