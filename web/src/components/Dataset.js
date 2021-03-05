import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Card, ListGroupItem } from "react-bootstrap";
import axios from "axios";
import * as echarts from "echarts";
import "../custom.css";
import { prod, dev } from "../App";
export default class Dataset extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      barChart: {},
      pieChart: {},
      performanceChart: {},
    };
  }

  componentDidMount() {
    this.initCharts();
    this.getData();
  }
  initCharts = () => {
    // 基于准备好的dom，初始化echarts实例
    let pieChart = echarts.init(document.getElementById("pieChart"));
    let performanceChart = echarts.init(
      document.getElementById("performanceChart")
    );
    let barChart = echarts.init(document.getElementById("barChart"));
    // 绘制图表
    pieChart.setOption(this.getPieOptions());
    performanceChart.setOption(this.getPerformanceOption());
    barChart.setOption(this.getBarOption());
    barChart.showLoading();
    pieChart.showLoading();
    performanceChart.showLoading();
    this.setState({
      barChart,
      pieChart,
      performanceChart,
    });
  };

  getBarOption() {
    let option = {
      legend: {
        data: [
          "IT",
          "French",
          "Arabic",
          "Science",
          "English",
          "Biology",
          "Spanish",
          "Chemistry",
          "Geology",
          "Quran",
          "Math",
          "History",
        ],
      },
      xAxis: {
        type: "category",
      },
      yAxis: {
        type: "value",
      },
      toolbox: {
        show: true,
        feature: {
          dataZoom: {
            yAxisIndex: "none",
          },
          dataView: { readOnly: true },
          saveAsImage: {},
        },
      },
      series: [
        {
          data: [],
          type: "bar",
          showBackground: true,
          backgroundStyle: {
            color: "rgba(180, 180, 180, 0.2)",
          },
        },
      ],
    };
    return option;
  }
  getPerformanceOption() {
    let option = {
      tooltip: {
        trigger: "axis",
        axisPointer: {
          // Use axis to trigger tooltip
          type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
        },
      },
      toolbox: {
        show: true,
        feature: {
          dataView: { readOnly: true },
          magicType: { type: ["line", "bar"] },
          saveAsImage: {},
        },
      },
      legend: {
        left: 0,
        zlevel: 99,
        data: [
          "raisedhands",
          "VisitedResources",
          "Discussion",
          "AnnouncementsView",
          "StudentAbsenceDays",
        ],
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "3%",
        containLabel: true,
      },
      xAxis: {
        type: "value",
      },
      yAxis: {
        type: "category",
        data: ["L", "M", "H"],
      },
      series: [
        {
          name: "raisedhands",
          type: "bar",
          stack: "total",
          label: {
            show: true,
          },
          emphasis: {
            focus: "series",
          },
          data: [],
        },
        {
          name: "VisitedResources",
          type: "bar",
          stack: "total",
          label: {
            show: true,
          },
          emphasis: {
            focus: "series",
          },
          data: [],
        },
        {
          name: "Discussion",
          type: "bar",
          stack: "total",
          label: {
            show: true,
          },
          emphasis: {
            focus: "series",
          },
          data: [],
        },
        {
          name: "AnnouncementsView",
          type: "bar",
          stack: "total",
          label: {
            show: true,
          },
          emphasis: {
            focus: "series",
          },
          data: [],
        },
        {
          name: "StudentAbsenceDays",
          type: "bar",
          color: "gray",
          stack: "total",
          label: {
            show: true,
          },
          emphasis: {
            focus: "series",
          },
          data: [],
        },
      ],
    };
    return option;
  }
  getPieOptions() {
    let option = {
      tooltip: {
        trigger: "item",
        formatter: "{a} <br/>{b}: {c} ({d}%)",
      },
      legend: {
        orient: "vertical",
        align: "right",
        right: 0,
        bottom: 0,
        zlevel: 99,
        data: [
          "KW",
          "Jordan",
          "Palestine",
          "Iraq",
          "lebanon",
          "Tunis",
          "SaudiArabia",
          "Egypt",
          "Syria",
          "Lybia",
          "USA",
          "Iran",
          "Morocco",
          "venzuela",
          "M",
          "F",
        ],
      },
      toolbox: {
        top: 20,
        show: true,
        feature: {
          dataView: { readOnly: true },
          saveAsImage: {},
        },
      },
      series: [
        {
          name: "Gender",
          type: "pie",
          selectedMode: "single",
          radius: [0, "30%"],
          label: {
            position: "inner",
            fontSize: 14,
          },
          labelLine: {
            show: false,
          },
          data: [],
        },
        {
          name: "Nationality",
          type: "pie",
          radius: ["45%", "60%"],
          labelLine: {
            length: 100,
          },
          label: {
            formatter: "{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ",
            backgroundColor: "#F6F8FC",
            borderColor: "#8C8D8E",
            borderWidth: 1,
            borderRadius: 4,

            rich: {
              a: {
                color: "#6E7079",
                lineHeight: 22,
                align: "center",
              },
              hr: {
                borderColor: "#8C8D8E",
                width: "100%",
                borderWidth: 1,
                height: 0,
              },
              b: {
                color: "#4C5058",
                fontSize: 14,
                fontWeight: "bold",
                lineHeight: 33,
              },
              per: {
                color: "#fff",
                backgroundColor: "#4C5058",
                padding: [3, 4],
                borderRadius: 4,
              },
            },
          },
          data: [],
        },
      ],
    };
    return option;
  }

  getGenderData() {
    return axios({
      url: `${prod}/get_gender_data`,
      method: "GET",
    });
  }
  getTopicData() {
    return axios({
      url: `${prod}/get_topic_data`,
      method: "GET",
    });
  }

  getNationalData() {
    return axios({
      url: `${prod}/get_national_data`,
      method: "GET",
    });
  }

  getNumData() {
    return axios({
      url: `${prod}/get_num_data`,
      method: "GET",
    });
  }

  getData = (e) => {
    let _this = this;

    axios
      .all([
        this.getGenderData(),
        this.getTopicData(),
        this.getNationalData(),
        this.getNumData(),
      ])
      .then(
        axios.spread(function (gres, tres, nares, nres) {
          console.log(gres, tres, nares, nres);
          let innerPie = gres.data.data;
          let upperPie = nares.data.data;
          let { pieChart, barChart, performanceChart } = _this.state;
          let tmpPie = pieChart.getOption();
          let tmpBar = barChart.getOption();
          let tmpPer = performanceChart.getOption();
          tmpPie.series[0].data = innerPie;
          tmpPie.series[1].data = upperPie;
          let legends = upperPie.map((e) => {
            return e.name;
          });
          legends.push("M", "F");
          console.log(legends);
          tmpPie.legend.data = legends;
          tmpPer.legend.data = nres.data.label;
          tmpPer.yAxis.data = nres.data.yData;
          tmpPer.series[0].data = nres.data.xData["raisedhands"];
          tmpPer.series[1].data = nres.data.xData["VisITedResources"];

          tmpPer.series[2].data = nres.data.xData["Discussion"];
          tmpPer.series[3].data = nres.data.xData["AnnouncementsView"];
          tmpPer.series[4].data = nres.data.xData["StudentAbsenceDays"];
          pieChart.clear();
          pieChart.setOption(tmpPie);
          performanceChart.clear();

          performanceChart.setOption(tmpPer);

          barChart.setOption({
            xAxis: {
              data: tres.data.name,
            },
            dataZoom: [
              {
                type: "inside",
              },
            ],
            series: [
              {
                type: "bar",
                data: tres.data.value,
              },
            ],
          });
          pieChart.hideLoading();
          barChart.hideLoading();
          performanceChart.hideLoading();
        })
      );
  };

  render() {
    return (
      <div>
        <Container>
          <div>
            <p className="bs-callout bs-callout-info">
              This data set has a total of 480 rows data, which will be divided
              into three charts for analysis.
            </p>
            <hr></hr>

            <div
              id="pieChart"
              style={{ width: "1150px", height: "650px" }}
            ></div>
            <p className="bs-callout bs-callout-info">
              This pie chart shows the ratio of males to females and the ratio
              of countries from the data set. We can see that most of the
              testers are male, and most of the testers are from KW
            </p>
            <hr></hr>

            <div
              id="performanceChart"
              style={{ width: "1150px", height: "650px" }}
            ></div>
            <p className="bs-callout bs-callout-info">
              This stacked horizontal chart shows the distribution of students'
              "raisedhands", "VisITedResources", "Discussion",
              "AnnouncementsView", and "StudentAbsenceDays" in the three levels
              of L, M, and H.
            </p>
            <hr></hr>

            <div
              id="barChart"
              style={{ width: "1150px", height: "550px" }}
            ></div>
            <p className="bs-callout bs-callout-info">
              This bar chart shows the distribution of students' subjects.
            </p>
          </div>
        </Container>
      </div>
    );
  }
}
