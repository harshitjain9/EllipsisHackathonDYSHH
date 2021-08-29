import React from "react";
import "./StartTradeLender.css";
import { Card, CardGroup, ListGroup } from "react-bootstrap";

export default function StartTradeLender() {
    return (
        <div className='start-trade-lender '>
            <h1 className="mt-4">Start a trade</h1>
            <CardGroup style={{ marginBottom: 20 + 'px' }}>
                <Card>
                    <ListGroup horizontal>
                        <ListGroup.Item>Name: x</ListGroup.Item>
                        <ListGroup.Item>Location: x</ListGroup.Item>
                        <ListGroup.Item>Credit Score: x</ListGroup.Item>
                        <ListGroup.Item>Funds required: x</ListGroup.Item>
                        <ListGroup.Item>Purpose: x</ListGroup.Item>
                        <ListGroup.Item>Desired Payback Date: x</ListGroup.Item>
                        <ListGroup.Item>Desired Interest Rate: x</ListGroup.Item>
                        <ListGroup.Item variant="success" className="d-flex align-items-center">Accept</ListGroup.Item>
                        <ListGroup.Item variant="danger" className="d-flex align-items-center">Decline</ListGroup.Item>
                    </ListGroup>
                </Card>
            </CardGroup>

            <CardGroup style={{ marginBottom: 20 + 'px' }}>
                <Card>
                    <ListGroup horizontal>
                        <ListGroup.Item>Name: x</ListGroup.Item>
                        <ListGroup.Item>Location: x</ListGroup.Item>
                        <ListGroup.Item>Credit Score: x</ListGroup.Item>
                        <ListGroup.Item>Funds required: x</ListGroup.Item>
                        <ListGroup.Item>Purpose: x</ListGroup.Item>
                        <ListGroup.Item>Desired Payback Date: x</ListGroup.Item>
                        <ListGroup.Item>Desired Interest Rate: x</ListGroup.Item>
                        <ListGroup.Item variant="success" className="d-flex align-items-center">Accept</ListGroup.Item>
                        <ListGroup.Item variant="danger" className="d-flex align-items-center">Decline</ListGroup.Item>
                    </ListGroup>
                </Card>
            </CardGroup>
        </div>
    );
}