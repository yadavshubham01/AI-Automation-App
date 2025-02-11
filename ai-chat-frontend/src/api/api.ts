import axios from "axios";
import { AuthResponse } from "../type";

const API_URL = "http://127.0.0.1:8000/auth/";

export const registerUser = async (username: string, password: string) => {
  return axios.post(`${API_URL}register/`, { username, password });
};

export const loginUser = async (username: string, password: string) => {
  return axios.post<AuthResponse>(`${API_URL}login/`, { username, password });
};
