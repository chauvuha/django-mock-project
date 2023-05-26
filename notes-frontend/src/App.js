import "./App.css";
import Header from "./components/Header";
import NotesListPage from "./pages/NotesListPage";
import ListItem from "./components/ListItem";
import NotePage from "./pages/NotePage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LogIn from "./pages/LogIn";

function App() {
  return (
    <Router>
      <div className="container">
        <div className="app">
          <Header />
          <Routes>
            <Route path="/" element={<NotesListPage />} />
            <Route path="/note/:id" element={<NotePage />} />
            <Route path="/login" element={<LogIn />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
