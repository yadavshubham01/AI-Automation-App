import React, { useEffect, useState } from "react";
import {io, Socket} from "socket.io-client"
import { Message } from "../type";

interface Props {
   token :string;
}

const Chat:React.FC<Props> = ({ token }) => {
  const [socket , setSocket]=useState<Socket | null>(null);
  const [message , setMessage ]= useState<string>("");
  const [chat ,setChat] = useState<Message[]>([]);

  useEffect(() => {
    if (token) {
      const ws = io(`ws://127.0.0.1:8000/ws/ws/?token=${token}`);

      ws.on("message", (data: string) => {
        setChat((prev) => [...prev, { type: "ai", text: data }]);
      });

      setSocket(ws);
      
       ws.disconnect();
    }
  }, [token]);

   const sendMessage = () =>{
    if(socket && message.trim()){
        setChat([...chat,{type:"user", text:message}])
        socket.emit("message",message);
        setMessage("");
    }
   };

    return (
        <div>
            <div>
             {chat.map((msg, index) => (
                <div key={index} className={`chat-message ${msg.type}`}>
                {msg.text}
             </div>
             ))} 
            </div>
            <input value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Type a message..." />
            <button onClick={sendMessage}>Send</button>
        </div>
    )
}

export default Chat;