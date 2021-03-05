import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {
	Col,
	Row,
	Image,
	Container
} from "react-bootstrap"

export default class FooterBar extends React.Component {
	render() {
		return (
			<div className="fixed" style={{ backgroundColor: '#E5EAFF' }}>
				<Container>
					<Row className='justify-content-center'>
						<Col className="align-self-start" style={{ marginTop: '1.5em' }}>
							<a href="/about" rel="noopener noreferrer" style={{ fontSize: '1.7em', color: 'black' }}>
							About Us</a>
						</Col>
						<Col className="col-sm-4 align-self-end order-sm-2" style={{ marginTop: '1.5em', textAlign: 'right' }}>
							<a href="https://github.com/due-lakers/LA-lakers"
								target="_blank" rel="noopener noreferrer"
								style={{ fontSize: '1.7em', color: 'black' }}>
								Follow us at <Image src="/images/github.png" style={{ height: '1em', width: 'auto', paddingRight: '0.15em', marginBottom: '0.3em' }} />Github
						</a>
						</Col>
					</Row>
					<br></br>
				</Container>
			</div >
		)
	}

}

