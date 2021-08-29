import React from "react";
import "./MyTradesLender.css";
import { Card, CardGroup } from "react-bootstrap";
import { PieChart } from 'react-minimal-pie-chart';

export default function MyTradesower() {

    return (
        <div className='my-trades-lender'>
            <h1 className="mt-4">Pending Trades</h1>
            <CardGroup style={{ marginBottom: 20 + 'px' }}>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        3641
                    </Card.Body>
                </Card>
                {/* <Card className="align-items-center" style={{ borderRadius: 5 + 'px' }}> */}
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        You lent $xx.yy
                    </Card.Body>
                </Card>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        You will receive $xx.yy
                    </Card.Body>
                </Card>
                <Card className="d-flex align-items-center justify-content-center">
                    <Card.Body className="d-flex align-items-center justify-content-center ">
                        <PieChart
                            radius='40'
                            data={[
                                { title: 'One', value: 47, color: '#00FF00' },
                                { title: 'Two', value: 53, color: '#FF0000' }
                            ]}
                        />
                        You have received 47%!
                    </Card.Body>
                </Card>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        37 days to completion
                    </Card.Body>
                </Card>
            </CardGroup>

            <CardGroup style={{ marginBottom: 20 + 'px' }}>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        3641
                    </Card.Body>
                </Card>
                {/* <Card className="align-items-center" style={{ borderRadius: 5 + 'px' }}> */}
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        You lent $xx.yy
                    </Card.Body>
                </Card>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        You will receive $xx.yy
                    </Card.Body>
                </Card>
                <Card className="d-flex align-items-center justify-content-center">
                    <Card.Body className="d-flex align-items-center justify-content-center ">
                        <PieChart
                            radius='40'
                            data={[
                                { title: 'One', value: 47, color: '#00FF00' },
                                { title: 'Two', value: 53, color: '#FF0000' }
                            ]}
                        />
                        You have received 47%!
                    </Card.Body>
                </Card>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        37 days to completion
                    </Card.Body>
                </Card>
            </CardGroup>

            

            <h1 className="mt-4">Completed Trades</h1>
            <CardGroup style={{ marginBottom: 20 + 'px' }}>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        2742
                    </Card.Body>
                </Card>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        You received $xx.yy
                    </Card.Body>
                </Card>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        You earned x in interest
                    </Card.Body>
                </Card>
                <Card className="align-items-center" >
                    <Card.Body className="d-flex align-items-center">
                        Trade closed on dd/mm/yy
                    </Card.Body>
                </Card>
            </CardGroup>
            </div>
        );
}