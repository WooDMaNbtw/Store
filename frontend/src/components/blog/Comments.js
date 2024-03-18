import React, {useState} from 'react';
import {Col, Row} from "react-bootstrap";
import svgReply from '../media/reply-solid.svg'
import axios from "axios";
const REACT_APP_APP_ID = process.env.REACT_APP_APP_ID

const Comments = ({ comments, slug, postId, updateComments }) => {
    const [replyContent, setReplyContent] = useState('');
    const [replyTo, setReplyTo] = useState(null);

    const handleReplyClick = (commentId) => {
        setReplyTo(commentId);
    };

    const handleReplySubmit = () => {
        if (replyContent.trim() !== '') {
            axios.post(
                `http://127.0.0.1:8000/api/v0/${REACT_APP_APP_ID}/comments/create/`, {
                    content: replyContent
                },
                {
                    params: {
                        parent_id: replyTo,
                        type: "post",
                        slug: slug,
                    },
                    headers: {
                        Authorization: "JWT " + localStorage.getItem('access_token')
                    }
                }).then(response => {
                console.log("Reply created successfully:", response.data);

                // Обновляем состояние комментариев в родительском компоненте
                updateComments(postId, response.data)
                // Очищаем содержимое поля ответа
                setReplyContent('');
                // Сбрасываем выбранный комментарий для ответа
                setReplyTo(null);
            }).catch(error => {
                if (error.response.status === 401){
                    window.location.href = "/sign-in/";
                }
                console.log("Error while creating reply", error);
            });
        }

    };

    return (
        <div className="comments">
            {comments.map(comment => (
                <div key={comment.id} className="comment">
                    <Row>
                        <Col sm={6}>
                            <p className="comment-content"><strong>{comment.user && comment.user.email}</strong>: {comment.content}</p>
                            <p className="comment-date">Posted on: {new Date(comment.timestamp).toLocaleString()}</p>
                        </Col>
                        <Col sm={6}>
                            <div className="reply-container">
                                <button className="reply-btn" onClick={() => handleReplyClick(comment.id)}>
                                    <img src={svgReply} alt="Reply"/>
                                </button>
                            </div>
                        </Col>
                    </Row>
                    {comment.replies && comment.replies.length > 0 && (
                        <div className="replies">
                            {comment.replies.map(reply => (
                                <div key={reply.id} className="reply">
                                    <p className="reply-content"><strong>{reply.user && reply.user.email}</strong>: {reply.content}</p>
                                    <p className="reply-date">Posted on: {new Date(reply.timestamp).toLocaleString()}</p>
                                </div>
                            ))}
                        </div>
                    )}

                    {replyTo === comment.id && (
                        <div className="reply-form">
                            <textarea value={replyContent} onChange={(e) => setReplyContent(e.target.value)} placeholder="Enter your reply"/>
                            <button onClick={handleReplySubmit}>Submit Reply</button>
                        </div>
                    )}
                </div>
            ))}

        </div>
    );
};

export default Comments;
