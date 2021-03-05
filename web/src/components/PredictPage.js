import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import {
  Modal,
  Container,
  Col,
  Row,
  Form,
  Button,
  ListGroupItem,
  Alert,
} from "react-bootstrap";
import axios from "axios";
import * as echarts from "echarts";
import "../custom.css";
import { prod, dev } from "../App";
export default class RegistrationPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      NationalITy: "",
      PlaceofBirth: "",
      StageID: "",
      GradeID: "",
      SectionID: "",
      Topic: "",
      Semester: "",
      VisITedResources: "",
      raisedhands: "",
      gender: "",
      AnnouncementsView: "",
      Discussion: "",
      StudentAbsenceDays: "",
      result: "",
      showModal: false,
      predict: "",
      eigen: "",
      chart: "",
      options: [],
      gaugeChart: {},
      rStudents: 0,
      errInput: false,
    };
  }

  getOption1 = () => {
    var dataAxis = [
      "AnnouncementsView",
      "Discussion",
      "GradeID",
      "NationalITy",
      "PlaceofBirth",
      "SectionID",
      "Semester",
      "StageID",
      "StudentAbsenceDays",
      "Topic",
      "VisITedResources",
      "gender",
      "raisedhands",
    ];
    var data = [
      6.296367193292755,
      2.101389616467447,
      0.19108965355389684,
      2.901540226848912,
      3.5255663369341366,
      0.10604810712246222,
      1.0441940144458841,
      0.2841978467782654,
      12.072858339809247,
      5.999152727424881,
      9.661327373899752,
      4.527614145295542,
      15.996324150917879,
    ];
    var yMax = 500;
    var dataShadow = [];

    for (var i = 0; i < data.length; i++) {
      dataShadow.push(yMax);
    }
    let option = {
      name: "eigen",
      title: {
        text: "Feature Map",
      },
      xAxis: {
        data: dataAxis,
        axisLabel: {
          rotate: 25,
          textStyle: {
            color: "#000",
          },
        },
        axisTick: {
          show: false,
        },
        axisLine: {
          show: false,
        },
        z: 1,
      },
      yAxis: {
        axisLine: {
          show: false,
        },
        axisTick: {
          show: false,
        },
        axisLabel: {
          textStyle: {
            color: "#999",
          },
        },
      },
      dataZoom: [
        {
          type: "inside",
        },
      ],
      series: [
        {
          type: "bar",
          showBackground: true,
          itemStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: "#83bff6" },
              { offset: 0.5, color: "#188df0" },
              { offset: 1, color: "#188df0" },
            ]),
          },
          emphasis: {
            itemStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: "#2378f7" },
                { offset: 0.7, color: "#2378f7" },
                { offset: 1, color: "#83bff6" },
              ]),
            },
          },
          data: data,
        },
      ],
    };
    let options = this.state.options;

    options.push(option);
    this.setState({
      options,
    });
    return option;
  };
  setDateOption(data) {
    var data = data;

    var dateList = data.map(function (item) {
      return item[0];
    });
    var valueList = data.map(function (item) {
      return item[1];
    });

    let option = {
      title: {
        text: "Recent users",
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: ["show Recent"],
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "3%",
        containLabel: true,
      },
      toolbox: {
        show: true,
        feature: {
          dataZoom: {
            yAxisIndex: "none",
          },
          dataView: { readOnly: false },
          magicType: { type: ["line", "bar"] },
          restore: {},
          saveAsImage: {},
        },
      },
      xAxis: {
        type: "category",
        data: dateList,
      },
      yAxis: {
        type: "value",
      },
      series: [
        {
          name: "Step Start",
          type: "line",
          step: "start",
          data: valueList,
        },
      ],
    };
    return option;
  }
  initChart() {
    // 基于准备好的dom，初始化echarts实例
    let myChart = echarts.init(document.getElementById("forms"));
    let gaugeChart = echarts.init(document.getElementById("gauge"));
    // 绘制图表
    myChart.setOption(this.getOption1());
    this.setState({
      chart: myChart,
      gaugeChart,
    });
    return [myChart, gaugeChart];
  }
  getGaugeOption() {
    let option = {
      series: [
        {
          type: "gauge",
          startAngle: 180,
          endAngle: 0,
          min: 0,
          max: 1,
          splitNumber: 8,
          axisLine: {
            lineStyle: {
              width: 6,
              color: [
                [0.33, "#FDDD60"],
                [0.67, "#58D9F9"],
                [1, "#7CFFB2"],
              ],
            },
          },
          pointer: {
            icon: "path://M12.8,0.7l12,40.1H0.7L12.8,0.7z",
            length: "12%",
            width: 20,
            offsetCenter: [0, "-60%"],
            itemStyle: {
              color: "auto",
            },
          },
          axisTick: {
            length: 12,
            lineStyle: {
              color: "auto",
              width: 2,
            },
          },
          splitLine: {
            length: 20,
            lineStyle: {
              color: "auto",
              width: 5,
            },
          },
          axisLabel: {
            color: "#464646",
            fontSize: 12,
            distance: -80,
            formatter: function (value) {
              if (value === 0.875) {
                return "Execellent";
              } else if (value === 0.625) {
                return "Good";
              } else if (value === 0.375) {
                return "Normal";
              }
            },
          },
          title: {
            offsetCenter: [0, "-20%"],
            fontSize: 15,
          },
          detail: {
            fontSize: 40,
            offsetCenter: [0, "0%"],
            valueAnimation: true,
            formatter: function (value) {
              return Math.round(value * 100) + "%";
            },
            color: "auto",
          },
          data: [
            {
              value: 0.7,
              name: "Performance evaluation",
            },
          ],
        },
      ],
    };
    return option;
  }
  componentDidMount() {
    this.getInitialState();
  }
  handleRegistation = (e) => {
    e.preventDefault();
    axios({
      url: `${prod}/predict`,
      method: "POST",
      data: {
        VisITedResources: this.state.VisITedResources,
        raisedhands: this.state.raisedhands,
        gender: this.state.gender,
        AnnouncementsView: this.state.AnnouncementsView,
        Discussion: this.state.Discussion,
        Topic: this.state.Topic,
        Semester: this.state.Semester,
        StageID: this.state.StageID,
        SectionID: this.state.SectionID,
        NationalITy: this.state.NationalITy,
        GradeID: this.state.GradeID,
        PlaceofBirth: this.state.PlaceofBirth,
        StudentAbsenceDays: this.state.StudentAbsenceDays,
      },
    })
      .then((response) => {
        console.log("res", response);
        response = JSON.parse(response.data);
        let code = response.code;
        if (code == 1) {
          this.setState({
            showModal: true,
            errInput: true,
          });
        } else {
          const data = response.data;
          const code = response.code;
          let eigen = data.eigen;
          let rate = data.rate;
          let rs = data.rs;
          let rStudents = data.rStudents;

          this.setState(
            {
              errInput: false,
              result: data.result,
              predict: data.result,
              eigen: eigen,
              showModal: true,
              rStudents,
            },
            () => {
              let chart = this.initChart()[0];
              let gauge = this.initChart()[1];
              let option = this.state.options[0];
              let gaugeOption = this.getGaugeOption();
              option.series[0].data = Object.values(eigen);
              option.xAxis.data = Object.keys(eigen);
              chart.setOption(option);

              gauge.setOption({
                series: [
                  {
                    type: "gauge",
                    axisLabel: {
                      formatter: function (value) {
                        if (value == rs[2]) {
                          return "execellent";
                        } else if (value == rs[1]) {
                          return "good";
                        } else if (value == rs[0]) {
                          return "normal";
                        }
                      },
                    },
                  },
                ],
              });
              gaugeOption.series[0].data[0]["value"] = rate;
              gauge.setOption(gaugeOption);
            }
          );
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };
  getInitialState = () => {
    let recentChart = echarts.init(document.getElementById("recent"));
    recentChart.showLoading();
    axios({
      url: `${prod}/get_recent_nums`,
      method: "GET",
    })
      .then((res) => {
        console.log("reee", res);
        recentChart.setOption(this.setDateOption(res.data));
        this.setState({ recentChart });
        recentChart.hideLoading();
      })
      .catch((e) => {});
  };

  close = () => {
    this.setState({ showModal: false });
  };

  open = () => {
    this.setState({ showModal: true });
  };

  handleLogin = (e) => {
    e.preventDefault();
    this.props.history.push("/dataset");
  };

  handleInputs = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };
  render() {
    const RelationError = <Alert variant="danger">{this.state.result}</Alert>;
    const AnnouncementsViewError = (
      <Alert variant="danger">{this.state.AnnouncementsView}</Alert>
    );
    const NameError = <Alert variant="danger">{this.state.gender}</Alert>;
    const RegistrationComplete = (
      <Alert variant="success">{this.state.success}</Alert>
    );
    return (
      <div>
        <Container>
          <Row style={{ marginTop: "2em", marginBottom: "11.1em" }}>
            <Col
              className="align-self-center md-6"
              style={{ paddingBottom: "5em" }}
            >
              <p style={{ fontSize: "3.32em" }}>
                Input your information and obtain{" "}
                <u style={{ color: "#1E38BF" }}>
                  <strong>your prediction</strong>
                </u>
              </p>
            </Col>
            <div
              id="recent"
              style={{
                width: "650px",
                height: "420px",
                padding: 0,
                margin: 0,
              }}
            ></div>
            <Col
              className="align-self-center md-4"
              style={{ paddingLeft: "4em", paddingTop: "5em" }}
            >
              <Form
                style={{
                  border: "1px solid #fff",
                  padding: "50px 60px",
                  backgroundColor: "#fff",
                  borderRadius: "0.8em",
                  WebkitBoxShadow: "0px 0px 20px -1px rgba(0,0,0,0.75)",
                  MozBoxShadow: "0px 0px 20px -1px rgba(0,0,0,0.75)",
                  boxShadow: "0px 0px 20px -1px rgba(0,0,0,0.75)",
                }}
              >
                <Form.Group controlId="formRelation">
                  <Form.Label>NationalITy</Form.Label>
                  <Form.Control
                    as="select"
                    name="NationalITy"
                    id="NationalITy"
                    defaultValue="Choose..."
                    value={this.state.NationalITy}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>Egypt</option>
                    <option>Iraq</option>
                    <option>Iran</option>
                    <option>Jordan</option>
                    <option>KW</option>
                    <option>lebanon</option>
                    <option>Lybia</option>
                    <option>Morocco</option>
                    <option>Palestine</option>
                    <option>SaudiArabia</option>
                    <option>Syria</option>
                    <option>Tunis</option>
                    <option>USA</option>
                    <option>venzuela</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formPlaceofBirth">
                  <Form.Label>PlaceofBirth</Form.Label>
                  <Form.Control
                    as="select"
                    name="PlaceofBirth"
                    id="PlaceofBirth"
                    defaultValue="Choose..."
                    value={this.state.PlaceofBirth}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>Egypt</option>
                    <option>Iraq</option>
                    <option>Iran</option>
                    <option>Jordan</option>
                    <option>KuwaIT</option>
                    <option>lebanon</option>
                    <option>Lybia</option>
                    <option>Morocco</option>
                    <option>Palestine</option>
                    <option>SaudiArabia</option>
                    <option>Syria</option>
                    <option>Tunis</option>
                    <option>USA</option>
                    <option>venzuela</option>
                  </Form.Control>
                </Form.Group>

                {/* display if error exists */}
                {/* {this.state.result.name ? NameError : null} */}

                <Form.Group controlId="exampleForm.ControlSelect1">
                  <Form.Label>Gender</Form.Label>
                  <Form.Control
                    as="select"
                    name="gender"
                    id="gender"
                    defaultValue="Choose..."
                    value={this.state.gender}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>M</option>
                    <option>F</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formGradeID">
                  <Form.Label>GradeID</Form.Label>
                  <Form.Control
                    as="select"
                    name="GradeID"
                    id="GradeID"
                    defaultValue="Choose..."
                    value={this.state.GradeID}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>G-02</option>
                    <option>G-05</option>
                    <option>G-06</option>
                    <option>G-07</option>
                    <option>G-08</option>
                    <option>G-09</option>
                    <option>G-10</option>
                    <option>G-11</option>
                    <option>G-12</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formSectionID">
                  <Form.Label>SectionID</Form.Label>
                  <Form.Control
                    as="select"
                    name="SectionID"
                    id="SectionID"
                    defaultValue="Choose..."
                    value={this.state.SectionID}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>A</option>
                    <option>B</option>
                    <option>C</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formStageID">
                  <Form.Label>StageID</Form.Label>
                  <Form.Control
                    as="select"
                    name="StageID"
                    id="StageID"
                    defaultValue="Choose..."
                    value={this.state.StageID}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>lowerlevel</option>
                    <option>MiddleSchool</option>
                    <option>HighSchool</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formTopic">
                  <Form.Label>Topic</Form.Label>
                  <Form.Control
                    as="select"
                    name="Topic"
                    id="Topic"
                    defaultValue="Choose..."
                    value={this.state.Topic}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>Arabic</option>
                    <option>Biology</option>
                    <option>Chemistry</option>
                    <option>English</option>
                    <option>French</option>
                    <option>Geology</option>
                    <option>History</option>
                    <option>IT</option>
                    <option>Math</option>
                    <option>Quran</option>
                    <option>Science</option>
                    <option>Spanish</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formSemester">
                  <Form.Label>Semester</Form.Label>
                  <Form.Control
                    as="select"
                    name="Semester"
                    id="Semester"
                    defaultValue="Choose..."
                    value={this.state.Semester}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>F</option>
                    <option>S</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formStudentAbsenceDays">
                  <Form.Label>StudentAbsenceDays</Form.Label>
                  <Form.Control
                    as="select"
                    name="StudentAbsenceDays"
                    id="StudentAbsenceDays"
                    defaultValue="Choose..."
                    value={this.state.StudentAbsenceDays}
                    onChange={this.handleInputs}
                    required
                  >
                    <option>Not specified</option>
                    <option>Above-7</option>
                    <option>Under-7</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="formVisITedResources">
                  <Form.Label>VisITedResources</Form.Label>
                  <Form.Control
                    type="number"
                    name="VisITedResources"
                    id="VisITedResources"
                    placeholder="e.g. 20..."
                    value={this.state.VisITedResources}
                    onChange={this.handleInputs}
                    required
                  />
                </Form.Group>

                <Form.Group controlId="formraisedhands">
                  <Form.Label>raisedhands</Form.Label>
                  <Form.Control
                    type="number"
                    name="raisedhands"
                    id="raisedhands"
                    placeholder="e.g. 20..."
                    value={this.state.raisedhands}
                    onChange={this.handleInputs}
                    required
                  />
                </Form.Group>

                {/* display if error exists */}

                <Form.Group controlId="formInputAnnouncementsView">
                  <Form.Label>AnnouncementsView</Form.Label>
                  <Form.Control
                    type="number"
                    name="AnnouncementsView"
                    id="AnnouncementsView"
                    placeholder="e.g. 20..."
                    value={this.state.AnnouncementsView}
                    onChange={this.handleInputs}
                    required
                  ></Form.Control>
                </Form.Group>

                <Form.Group controlId="formDiscussion">
                  <Form.Label>Discussion</Form.Label>
                  <Form.Control
                    type="number"
                    name="Discussion"
                    placeholder="e.g. 20..."
                    id="Discussion"
                    value={this.state.Discussion}
                    onChange={this.handleInputs}
                    required
                  ></Form.Control>
                </Form.Group>

                <br></br>
                <Button
                  className="float-right"
                  onClick={this.handleRegistation}
                  style={{
                    borderRadius: "0.7em",
                    backgroundColor: "#1E38BF",
                    WebkitBoxShadow: "0px 0px 20px -1px rgba(0,0,0,0.75)",
                    MozBoxShadow: "0px 0px 20px -1px rgba(0,0,0,0.75)",
                    boxShadow: "0px 0px 5px -1px rgba(0,0,0,0.75)",
                    fontSize: "1.5em",
                  }}
                >
                  Predict
                </Button>
                <br></br>
                <br></br>
              </Form>
            </Col>
          </Row>
          <Modal show={this.state.showModal} onHide={this.close}>
            <Modal.Header closeButton>
              <Modal.Title>
                {this.state.errInput ? "Error" : "Success"}
              </Modal.Title>
            </Modal.Header>
            <Modal.Body>
              {this.state.errInput ? (
                "bad input, please check your input!"
              ) : (
                <div>
                  <ListGroupItem
                    header={`Your prediction result is ${this.state.predict}`}
                    style={{ backgroundColor: "#DFF0D8" }}
                  >
                    <p>
                      {"Your prediction result is: " + this.state.predict}
                      <text style={{ color: "gray" }}>
                        <br />
                        There are <code> {this.state.rStudents}</code> students
                        who get the same performance as you
                      </text>
                    </p>
                  </ListGroupItem>
                  <hr></hr>
                  <div>
                    <div
                      id="gauge"
                      style={{
                        width: "650px",
                        height: "390px",
                        padding: 0,
                        margin: 0,
                      }}
                    ></div>
                    <hr></hr>
                    <div
                      id="forms"
                      style={{ width: "650px", height: "350px" }}
                    ></div>
                    <ListGroupItem style={{ backgroundColor: "#D9EDF7" }}>
                      Feature map, These attributes show the relationship
                      between the input item and the result
                    </ListGroupItem>
                  </div>
                </div>
              )}
            </Modal.Body>
            <Modal.Footer>
              <Button onClick={this.close}>Ok</Button>
            </Modal.Footer>
          </Modal>
        </Container>
      </div>
    );
  }
}
