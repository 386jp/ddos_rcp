import React, { useEffect, useState } from "react";
import { Navbar, Nav, Container, Row, Button, Alert } from "react-bootstrap";
import LOGO from "./logo.svg";
import axios from "axios";

interface RcpResult {
	choice: string;
	result: string;
};

interface ApiResult {
	[name: string]: RcpResult;
}

interface RcpChoiceDict {
	[name: string]: string;
}

const RcpChoices = {
	ROCK: "👊",
	SCISSORS: "✌️",
	PAPER: "🖐",
} as RcpChoiceDict;

function App() {
	const [rcpData, setRcpData] = useState<ApiResult>();
	const getRcpResult = (v: string) => {
		const urlAPI = process.env.REACT_APP_API_HOST_NAME + "/gamemgr/vs_bot/?user_choice=" + v;
		axios.get(urlAPI).then((res) => {
			setRcpData(res.data);
		});
	};

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
					<Alert variant={rcpData.user.result == "WIN" ? "success" : "danger"}>
						<Alert.Heading>{"YOU " + rcpData.user.result}</Alert.Heading>
						<p>Bot: {RcpChoices[rcpData.bot.choice]}</p>
            <p>You: {RcpChoices[rcpData.user.choice]}</p>
					</Alert>
				</Container>
			) : null}
		</div>
	);
}

export default App;
