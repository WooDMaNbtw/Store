import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './css/about.css';
import photo from '../media/photo.jpeg';
import {Col, Row} from "react-bootstrap";
const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

function AboutInfo() {
    const [datas, setDatas] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/biography/about/info/`)
            .then(response => {
                setDatas(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <div className="about-container">
            {datas.map((data, index) => (
                <div key={index} className="about-list">
                    <div className="about-item">
                        <Row className="name-info">
                            <div className="header-info">
                                    <Col sm={7}>
                                        <h2>{data.first_name} {data.last_name}</h2>
                                        <h3>{data.position}</h3>
                                        <div className="details">
                                            <p>Age: {data.age}</p>
                                            <p>Birth: {data.birth}</p>
                                            <p>Residing: {data.residence}</p>
                                            <p>Nationality: {data.nationality}</p>
                                            <p>Email: {data.email}</p>
                                            <p>Phone: {data.phone}</p>
                                        </div>
                                    </Col>
                                    <Col sm={5}>
                                        <div className="profile-image">
                                            <img src={photo} alt="Profile"/>
                                        </div>
                                    </Col>
                            </div>
                        </Row>
                        <Row>
                            <div className="about-info">
                                <h3>About Me</h3>
                                <div>{data.about.split('\n').map((line, index) => (
                                    <React.Fragment key={index}>
                                        <p>{line}</p>
                                    </React.Fragment>
                                ))}</div>
                            </div>
                        </Row>
                        <Row>
                            <div className="social-networks">
                                <h3>Social Networks</h3>
                                <div className="details">
                                    {data.linkedin && <p>LinkedIn: <a href={data.linkedin} target="blank">{data.linkedin}</a></p>}
                                    {data.twitter && <p>Twitter: <a href={data.twitter} target="blank">{data.twitter}</a></p>}
                                    {data.vkontakte && <p>VKontakte: <a href={data.vkontakte} target="blank">{data.vkontakte}</a></p>}
                                    {data.facebook && <p>Facebook: <a href={data.facebook} target="blank">{data.facebook}</a></p>}
                                    {data.instagram && <p>Instagram: <a href={data.instagram} target="blank">{data.instagram}</a></p>}
                                    {data.youtube && <p>Youtube: <a href={data.youtube} target="blank">{data.youtube}</a></p>}
                                    {data.github && <p>GitHub: <a href={data.github} target="blank">{data.github}</a></p>}
                                    {data.telegram && <p>Telegram: <a href={data.telegram} target="blank">{data.telegram}</a></p>}
                                </div>
                            </div>
                        </Row>
                    </div>
                </div>
            ))}
        </div>
    );
}

export default AboutInfo;
