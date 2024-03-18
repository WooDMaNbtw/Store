import './App.css';
import 'bootstrap/dist/css/bootstrap-grid.min.css'
import React from 'react';
import { BrowserRouter as Router} from "react-router-dom";
import {Route, Routes} from "react-router-dom";
import ExperienceDetail from "./components/about/experience_detail";
import About from "./pages/about";
import Blog from "./pages/blog";
import Contacts from "./pages/contacts";
import Register from "./pages/register";
import Login from "./pages/login";


function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<About />} />
                <Route path="/blog/" element={<Blog />} />
                <Route path="/contacts/" element={<Contacts />} />
                <Route path="/experience/:slug/" element={<ExperienceDetail />} />
                <Route path="/sign-up/" element={<Register />} />
                <Route path="/sign-in/" element={<Login />} />
            </Routes>
        </Router>
    );
}

export default App;
