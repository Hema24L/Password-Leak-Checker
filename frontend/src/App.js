import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LeakChecker from "./pages/LeakChecker.js";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LeakChecker />} />
      </Routes>
    </Router>
  );
}

export default App;
