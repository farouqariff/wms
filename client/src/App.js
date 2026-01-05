import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import AdminPage from "./components/AdminPage";
import ManagerPage from "./components/ManagerPage";
import OperatorPage from "./components/OperatorPage";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/admin" element={<AdminPage />} />
          <Route path="/manager" element={<ManagerPage />} />
          <Route path="/operator" element={<OperatorPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
