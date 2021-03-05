import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import NavigationBar from "./components/NavigationBar";
import FooterBar from "./components/FooterBar";
import RoutePage from "./components/RoutePage";

export const prod = "http://localhost:8080/api";
function App() {
  return (
    <div className="App">
      <Router>
        <NavigationBar />
        <div className="App">
          <RoutePage />
        </div>
        <FooterBar />
      </Router>
    </div>
  );
}

export default App;
