import React, { useState } from "react";
import { loginUser, registerUser } from "../api/api";

interface Props {
  setToken: (token: string | null) => void;
}

const Auth: React.FC<Props> = ({ setToken }) => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [isRegister, setIsRegister] = useState<boolean>(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = isRegister
        ? await registerUser(username, password)
        : await loginUser(username, password);
      
      if (!isRegister) {
        localStorage.setItem("token", response.data.access_token);
        setToken(response.data.access_token);
      }
      alert(isRegister ? "User Registered" : "Login Successful");
    } catch (err) {
      alert("Error: Login Failed");
    }
  };

  return (
    <div className="auth-container">
      <h2>{isRegister ? "Register" : "Login"}</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} required />
        <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} required />
        <button type="submit">{isRegister ? "Register" : "Login"}</button>
      </form>
      <button onClick={() => setIsRegister(!isRegister)}>
        {isRegister ? "Switch to Login" : "Switch to Register"}
      </button>
    </div>
  );
};

export default Auth;
