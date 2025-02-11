import React from "react";
import Chat from "../components/Chat";

interface Props {
  token: string | null;
}

const ChatPage: React.FC<Props> = ({ token }) => {
  return token ? <Chat token={token} /> : <h2>Please Login</h2>;
};

export default ChatPage;
