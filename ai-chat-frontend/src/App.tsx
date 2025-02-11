import React,  { useState } from "react";
import { BrowserRouter , Route, Routes } from "react-router-dom";
import AuthPage from "./page/AuthPage";
import ChatPage from "./page/ChatPage";


const App: React.FC = () => {
  const [token, setToken] = useState<string | null>(localStorage.getItem("token"));

  return (
   <BrowserRouter>
      <Routes>
        <Route path="/" element={<AuthPage setToken={setToken} />} />
        <Route path="/chat" element={<ChatPage token={token} />} />
      </Routes>
    </BrowserRouter> 
  );
};

export default App;
