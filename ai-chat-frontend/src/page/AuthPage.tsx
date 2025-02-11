import React from "react";
import Auth from "../components/Auth";

interface Props {
  setToken: (token: string | null) => void;
}

const AuthPage: React.FC<Props> = ({ setToken }) => {
  return <Auth setToken={setToken} />;
};

export default AuthPage;
