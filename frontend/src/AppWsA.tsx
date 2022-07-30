import React, { useEffect, useState } from "react";
import { Navbar, Nav, Container, Row, Button, Alert } from "react-bootstrap";
import LOGO from "./logo.svg";
import axios from "axios";

interface ApiResult {
	[name: string]: number;
}

interface WsResponseType {
	[name: string]: any;
}

interface RcpChoiceDict {
	[name: string]: string;
}

const RcpChoices = {
	ROCK: "👊",
	SCISSORS: "✌️",
	PAPER: "🖐",
} as RcpChoiceDict;

function AppWsA() {
	const [rcpAnalyticsData, setRcpAnalyticsData] = useState<ApiResult>();
	const WS_URL = process.env.REACT_APP_WS_API_HOST_NAME + '/gamemgr/analytics/';
	const [ws, setWs] = useState<WebSocket>();

	useEffect(() => {
		setWs(new WebSocket(WS_URL));
	}, []);

	if (ws !== undefined) {
		ws.onopen = (event) => {
			console.log('WebSocket Client Connected');
		};
		ws.onmessage = function (event) {
			console.log(event);
			const msg: WsResponseType = JSON.parse(event.data.toString());
			if (msg.type == "analytics") {
				setRcpAnalyticsData(msg.data);
			}
		};
	}


	return (
		<div>
			<Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
				<Navbar.Brand href="/">
					<img src={LOGO} width="30" height="30" alt="React Bootstrap logo" />
					ddos_rcp
				</Navbar.Brand>
				<Navbar.Toggle aria-controls="responsive-navbar-nav" />
				<Navbar.Collapse id="responsive-navbar-nav">
					<Nav className="mr-auto">
						<Nav.Link href="/">API</Nav.Link>
						<Nav.Link href="/ws/1">WebSocket</Nav.Link>
						<Nav.Link href="/wsa">WebSocket_Analytics</Nav.Link>
					</Nav>
				</Navbar.Collapse>
			</Navbar>
			{rcpAnalyticsData ? (
				<Container>
					<Alert variant="success">
						<Alert.Heading>Realtime Analytics</Alert.Heading>
						{Object.entries(rcpAnalyticsData).map(([k,v]) => (
							<p key={k}>{RcpChoices[k]}: {v}</p>
						))}
					</Alert>
				</Container>
			) : null}
		</div>
	);
}

export default AppWsA;
