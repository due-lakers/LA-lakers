import React from "react";
import { Container, Col, Row, Image, Button } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import jwt_decode from "jwt-decode";

export default class LandingPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstname: "",
      lastname: "",
    };
  }

  handleJoin = (e) => {
    e.preventDefault();
    this.props.history.push("/predict");
  };

  componentDidMount() {
    if (localStorage.usertoken) {
      const token = localStorage.usertoken;
      const decoded = jwt_decode(token);
      this.setState({
        firstname: decoded.identity.firstname,
        lastname: decoded.identity.lastname,
      });
    }
  }

  render() {
    const notLoggedIn = (
      <Button
        onClick={this.handleJoin}
        style={{
          float: "right",
          borderRadius: "0.8em",
          backgroundColor: "#1E38BF",
          WebkitBoxShadow: "0px 0px 20px -1px rgba(0,0,0,0.75)",
          MozBoxShadow: "0px 0px 20px -1px rgba(0,0,0,0.75)",
          boxShadow: "0px 0px 5px -1px rgba(0,0,0,0.75)",
          fontSize: "1.4em",
          paddingLeft: "0.8em",
          paddingRight: "0.8em",
        }}
      >
        Predict Now!
      </Button>
    );

    const LoggedIn = (
      <p style={{ fontSize: "2.0em" }}>
        Welcome {this.state.firstname} {this.state.lastname}
      </p>
    );
    return (
      <div>
        <Container style={{ paddingTop: "2em" }}>
          <Row style={{ marginTop: "5em" }}>
            <Col className="align-self-center">
              <p style={{ fontSize: "4em" }}>
                {" "}
                Welcome to<u style={{ color: "#1E38BF" }}> APAS </u>!
              </p>

              <p style={{ fontSize: "1.5em" }}>
                {" "}
                <u style={{ color: "#1E38BF" }}>
                  Academic Performance Analysis System(APAS){" "}
                </u>{" "}
                is designed to predict students' scores and performance in
                certain subjects.
              </p>

              <br />
            </Col>
            <Col className="d-none d-md-block col-md-5">
              <Image src="images/bg.png" style={{ width: "400px" }} />
            </Col>
          </Row>
          <hr></hr>
          <Row style={{ marginTop: "8em", padding: "4em" }}>
            <Col className="d-none d-md-block col-md-6">
              <Image src="images/predict.png" style={{ width: "550px" }} />
            </Col>
            <Col className="align-self-center">
              <p style={{ fontSize: "2em" }}>
                We are always working to provide better prediction results.
              </p>

              <br />

              {localStorage.usertoken ? LoggedIn : notLoggedIn}
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}
