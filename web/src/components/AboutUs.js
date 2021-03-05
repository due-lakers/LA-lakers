import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Button, Col, Row, Card, Image } from "react-bootstrap";
export default function AboutUs() {
  return (
    <div>
      <Container>
        <Row style={{ marginTop: "5em", marginBottom: "21.2em" }}>
          <Card style={{ width: "100%" }}>
            <Card.Img variant="top" src="images/dataset-cover.jpg" />
            <Card.ImgOverlay style={{ color: "white", height: "200px" }}>
              <Card.Title>
                <h2>Students' Academic Performance Dataset</h2>
              </Card.Title>
              <Card.Text>xAPI-Educational Mining Dataset</Card.Text>
            </Card.ImgOverlay>
            <Card.Body>
              <Card.Text>
                <code>
                  Source: Elaf Abu Amrieh, Thair Hamtini, and Ibrahim Aljarah,
                  The University of Jordan, Amman, Jordan,
                  http://www.Ibrahimaljarah.com www.ju.edu.jo
                </code>
                <hr></hr>
                <h5>Dataset Information:</h5>
                <p>
                  This is an educational data set which is collected from
                  learning management system (LMS) called Kalboard 360. Kalboard
                  360 is a multi-agent LMS, which has been designed to
                  facilitate learning through the use of leading-edge
                  technology. Such system provides users with a synchronous
                  access to educational resources from any device with Internet
                  connection.
                </p>
                <p>
                  The data is collected using a learner activity tracker tool,
                  which called experience API (xAPI). The xAPI is a component of
                  the training and learning architecture (TLA) that enables to
                  monitor learning progress and learner’s actions like reading
                  an article or watching a training video. The experience API
                  helps the learning activity providers to determine the
                  learner, activity and objects that describe a learning
                  experience.
                </p>
                <p>
                  The dataset consists of 480 student records and 16 features.
                  The features are classified into three major categories: (1)
                  Demographic features such as gender and nationality. (2)
                  Academic background features such as educational stage, grade
                  Level and section. (3) Behavioral features such as raised hand
                  on class, opening resources, answering survey by parents, and
                  school satisfaction.
                </p>
                <p>
                  The dataset consists of 305 males and 175 females. The
                  students come from different origins such as 179 students are
                  from Kuwait, 172 students are from Jordan, 28 students from
                  Palestine, 22 students are from Iraq, 17 students from
                  Lebanon, 12 students from Tunis, 11 students from Saudi
                  Arabia, 9 students from Egypt, 7 students from Syria, 6
                  students from USA, Iran and Libya, 4 students from Morocco and
                  one student from Venezuela.
                </p>
                <p>
                  The dataset is collected through two educational semesters:
                  245 student records are collected during the first semester
                  and 235 student records are collected during the second
                  semester.
                </p>
                <p>
                  The data set includes also the school attendance feature such
                  as the students are classified into two categories based on
                  their absence days: 191 students exceed 7 absence days and 289
                  students their absence days under 7.
                </p>
                <p>
                  This dataset includes also a new category of features; this
                  feature is parent parturition in the educational process.
                  Parent participation feature have two sub features: Parent
                  Answering Survey and Parent School Satisfaction. There are 270
                  of the parents answered survey and 210 are not, 292 of the
                  parents are satisfied from the school and 188 are not.
                </p>
                (See the related papers for more details).
              </Card.Text>
              <Row>
                <Col className="d-none d-md-block col-md-6 text-center">
                  <Image
                    src="images/socoLogo.png"
                    className="img-fluid visible-lg-block"
                    style={{ height: "7em", width: "auto", marginTop: "2em" }}
                  />
                  <Image
                    src="images/uniLogo.png"
                    className="img-fluid visible-lg-block"
                    style={{ height: "7em", marginTop: "2em" }}
                  />
                </Col>
                <Col
                  className="align-self-center"
                  style={{ paddingLeft: "4em" }}
                >
                  <p style={{ fontSize: "3.5em" }}>
                    We are <strong style={{ color: "#FCDC00" }}>LAkers</strong>
                  </p>
                  <p style={{ fontSize: "1.5em" }}>
                    Team members
                    <ul style={{ fontSize: "0.8em" }}>
                      <li>Ao Sun</li>
                      <li>Chengzhi Wei</li>
                      <li>Dexuan Zhang</li>
                      <li>Shahab Aldin Abbaszadeh</li>
                      <li>Yunlong Zhao</li>
                    </ul>
                  </p>
                  <br />
                </Col>
              </Row>
            </Card.Body>
          </Card>
        </Row>
      </Container>
      <br></br>
    </div>
  );
}
