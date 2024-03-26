import React, {Component} from 'react';
import LoginForm from "../components/account/LoginForm";
import Header from "../components/header";

class Login extends Component {
    render() {
        return (
            <div>
                <Header/>
                <LoginForm/>
            </div>
        );
    }
}

export default Login;