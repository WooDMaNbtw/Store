import React from 'react';
import Header from "../components/header";
import {Container} from "react-bootstrap";
import PostContent from "../components/blog/PostContent";

const Blog = () => {

    return (
        <>
            <Header />
            <Container>
                <PostContent />
            </Container>
        </>
    );
}

export default Blog;