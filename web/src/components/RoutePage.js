import React from "react";
import PredictPage from "./PredictPage";
import HomePage from "./Home";
import Dataset from "./Dataset";
import AboutUs from "./AboutUs";
import { Route } from "react-router-dom";

export default function RoutePage() {
  return (
    <div>
      <Route exact path="/" component={HomePage} />
      <div className="container">
        <Route exact path="/predict" component={PredictPage} />
        <Route exact path="/about" component={AboutUs} />
        <Route exact path="/dataset" component={Dataset} />
      </div>
    </div>
  );
}
