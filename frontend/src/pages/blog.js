import React, { useState } from 'react';
import Header from "../components/header";
import {Container} from "react-bootstrap";
import PostContent from "../components/blog/PostContent";

const Blog = () => {

    const [query, setQuery] = useState('');

    const handleQueryChange = (queryObject) => {
        setQuery(queryObject);
        alert(query)
    };


    return (
        <>
            <Header onQueryChange={handleQueryChange}/>
            <Container>
                <PostContent query={query}/>
            </Container>
        </>
    );
}

export default Blog;