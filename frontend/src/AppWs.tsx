import React, { useEffect, useState } from "react";
import { Navbar, Nav, Container, Row, Button, Alert } from "react-bootstrap";
import LOGO from "./logo.svg";
import axios from "axios";
import { useParams } from "react-router-dom";


interface RcpResult {
	choice: string;
	result: string;
};

interface ApiResult {
	[name: string]: RcpResult;
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

function AppWs() {
	let { roomId } = useParams();
	const [rcpData, setRcpData] = useState<ApiResult>();
	const [wsId, setWsId] = useState<keyof ApiResult>("");
	const WS_URL = process.env.REACT_APP_WS_API_HOST_NAME + '/gamemgr/realtime/' + roomId;
	const [ws, setWs] = useState<WebSocket>();


	useEffect(() => {
		setWs(new WebSocket(WS_URL));
	}, []);

	const getRcpResult = (v: string) => {
		if (ws !== undefined) {
			ws.send(JSON.stringify({
				"type": "rcp_my_choice",
				"data": v
			}));
		}
	};

	if (ws !== undefined) {
		ws.onopen = (event) => {
			console.log('WebSocket Client Connected');
		};
		ws.onmessage = function (event) {
			console.log(event);
			const msg = JSON.parse(event.data);
			if (msg.type == "your_ws_id") {
				setWsId(msg.data);
			}
			if (msg.type == "result") {
				setRcpData(msg.data);
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
			<Container>
				<Row className="mx-0">
					{["ROCK", "SCISSORS", "PAPER"].map((v) => (
						<Button variant="primary" onClick={() => getRcpResult(v)} key={v}>
							{RcpChoices[v]}
						</Button>
					))}
				</Row>
			</Container>
			{rcpData ? (
				<Container>
					<Alert variant={rcpData[wsId].result == "WIN" ? "success" : "danger"}>
					{/* <Alert variant="success"> */}
						<Alert.Heading>{"YOU " + rcpData[wsId].result}</Alert.Heading>
						{Object.entries(rcpData).map(([k,v]) => (
							<p key={k}>{k}: {RcpChoices[v.choice]}</p>
						))}
					</Alert>
				</Container>
			) : null}
		</div>
	);
}

export default AppWs;
