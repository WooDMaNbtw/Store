import React, { useState, useEffect } from 'react';
import Comments from './Comments';
import './css/postContent.css';
import axios from "axios";
import {Navigate} from "react-router-dom";


const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

const BlogPosts = ({ query }) => {
    const [posts, setPosts] = useState([]);
    const [comment, setComment] = useState('');
    // const [comments, setComments] = useState([]);
    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/posts/?query=${query}`)
            .then(response => {
                // alert(query)
                // alert(`http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/posts/?query=${query}`)
                setPosts(response.data.results);
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
            <h1>Blog Posts</h1>
            {posts.map(post => (
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
                        <button className="add-comment-btn" onClick={() => addComment(post.id, post.slug)}>Add Comment</button>
                    </div>
                    <hr className="post-divider" />
                </div>
            ))}
        </div>
    );
};

export default BlogPosts;
