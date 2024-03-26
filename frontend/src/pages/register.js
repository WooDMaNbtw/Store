import React, {Component} from 'react';
import RegisterForm from "../components/account/RegisterForm";
import Header from "../components/header";

class Register extends Component {
    render() {
        return (
            <div>
                <Header/>
                <RegisterForm/>
            </div>
        );
    }
}

export default Register;