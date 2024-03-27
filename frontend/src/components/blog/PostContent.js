import React, { useState, useEffect } from 'react';
import Comments from './Comments';
import './css/postContent.css';
import axios from "axios";

const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

const BlogPosts = () => {
    const [posts, setPosts] = useState([]);
    const [comment, setComment] = useState('');
    const [isBlankPosts, setIsBlankPosts] = useState(false)

    let query = ''
    const currentUrl = window.location.href;
    const questionMarkIndex = currentUrl.indexOf('?');

    if (questionMarkIndex !== -1){
        const queryString = currentUrl.slice(questionMarkIndex + 1);
        const paramValue = queryString.split('=')[1];
        if (paramValue !== undefined) {
            // Декодируем значение параметра и сохраняем его
            query = decodeURIComponent(paramValue);
        }
    }

    // const [comments, setComments] = useState([]);
    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/posts/?query=${query.replace('+', ' ')}`)
            .then(response => {
                console.log(response.data.results)
                if (response.data.results.length !== 0){
                    setPosts(response.data.results);
                } else {
                    setIsBlankPosts(true)
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, [query]);

    const toggleComments = (postId) => {
        setPosts(posts.map(post => {
            if (post.id === postId) {
                return { ...post, showComments: !post.showComments };
            }
            return post;
        }));
    };

    const handleInputChange = (event) => {
        setComment(event.target.value); // Update the comment input value
    };

    const addComment = (postId, slug) => {

        if (!comment.trim()) {
            // Если комментарий пустой или содержит только пробельные символы, не отправлять запрос
            return;
        }

        const newComment = {
            id: Math.round(Math.random() * 1000000),
            user: { email: 'From you' },
            content: comment,
            timestamp: new Date().toISOString()
        };
        axios.post(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/comments/create/`, {
            content: comment // Content of the comment
        },
    {
        params: {
            parent_id: null, // Assuming it's a top-level comment,
            type: 'post',
            slug: slug, // You might need to pass the post slug here if available
        },
        headers: {
            Authorization: "JWT " + localStorage.getItem('access_token')
        }
            }).then(response => {
                console.log('Comment created successfully:', response.data);
                newComment.id = response.data.id
                newComment.user = { email: response.data.user.email }
                console.log(response.data.user.email)
                setPosts(posts.map(post => {
                    if (post.id === postId) {
                        return { ...post, comments: [newComment, ...post.comments], showComments: true };
                    }
                    return post;
                }));
            })
            .catch(error => {
                if (error.response.status === 401){
                    window.location.href = "/sign-in/";
                }
                console.error('Error creating comment:', error);
                // Handle error, show error message to user, etc.
            });
    };

    const updateComments = (postId, repliedComment) => {
        const updatedPosts = posts.map(post => {
            if (post.id === postId) {
                const updatedComments = post.comments.map(comment => {
                    if (comment.id === repliedComment.parent) {
                        return {
                            ...comment,
                            replies: [...(comment.replies || []), repliedComment]
                        };
                    }
                    return comment;
                });

                return { ...post, comments: updatedComments, showComments: true };
            }
            return post;
        });

        setPosts(updatedPosts);
    };


    return (
        <div className="blog-posts-container">
            {!isBlankPosts
                ?
                (
                    posts.map(post => (
                        <div key={post.id} className="post">
                            <h2 className="post-title">{post.title}</h2>
                            <p className="post-content">{post.content}</p>
                            <p className="post-date">Published on: {new Date(post.publish).toLocaleDateString()}</p>
                            <button className="toggle-comments-btn" onClick={() => toggleComments(post.id)}>
                                {post.showComments ? 'Hide Comments' : 'Show Comments'}
                            </button>
                            {post.showComments &&
                                <Comments
                                    comments={post.comments}
                                    slug={post.slug}
                                    postId={post.id}
                                    updateComments={updateComments}
                                />
                            }
                            <div className="add-comment">
                                <input
                                    type="text"
                                    className="comment-input"
                                    placeholder="Add a comment"
                                    onChange={handleInputChange}
                                />
                                <button className="add-comment-btn" onClick={() => addComment(post.id, post.slug)}>Add
                                    Comment
                                </button>
                            </div>
                            <hr className="post-divider"/>
                        </div>
                    )))
                :
                (
                    <div style={{display: 'table', width: '100%', height: '80vh'}}>
                        <div style={{display: 'table-cell', verticalAlign: 'middle', textAlign: 'center', alignItems: "center", justifyContent: "center"}}>
                            <p className="animate-text" style={{fontSize: '30px', fontWeight: 'bold', color: 'black', marginBottom: '0px'}}>There are no blogs were found!</p>
                            <p style={{marginBottom: '0px'}}> Please try to remove your specified query. In other cases there are no articles posted yet</p>
                            {/*<p style={{fontSize: '20px', marginBottom: '0px'}}>To <a href='/'>home</a></p>*/}
                            <div className="circles" style={{
                                display: "flex",
                                verticalAlign: 'middle',
                                textAlign: 'center', alignItems: "center", justifyContent: "center"}}>
                                <div className="animation circle-1"></div>
                                <div className="animation circle-2"></div>
                                <div className="animation circle-3"></div>
                                <div className="animation circle-4"></div>
                                <div className="animation circle-5"></div>
                            </div>
                        </div>
                    </div>
                )
            }
        </div>
    );
};

export default BlogPosts;
