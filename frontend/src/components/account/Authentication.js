import React, { useState } from 'react';
import RegisterForm from './RegisterForm';
import LoginForm from './LoginForm';

const Authentication = ({ onLoginSuccess }) => {
    const [isRegistering, setIsRegistering] = useState(false);

    const handleRegisterSuccess = () => {
        setIsRegistering(false);
    };

    return (
        <div>
            {isRegistering ? (
                <RegisterForm onRegisterSuccess={handleRegisterSuccess} />
            ) : (
                <LoginForm onLoginSuccess={onLoginSuccess} />
            )}
            <button onClick={() => setIsRegistering(!isRegistering)}>
                {isRegistering ? 'Login Instead' : 'Register Instead'}
            </button>
        </div>
    );
};

export default Authentication;
