export interface AuthResponse {
    access_token: string;
  }
  
  export interface Message {
    type: "user" | "ai";
    text: string;
  }
  