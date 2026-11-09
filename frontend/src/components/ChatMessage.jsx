import { Bot, User } from "lucide-react";

function ChatMessage({ message }) {
  const isUser = message.role === "user";

  return (
    <div className={`message-row ${isUser ? "user-row" : "bot-row"}`}>
      <div className="avatar">
        {isUser ? <User size={18} /> : <Bot size={18} />}
      </div>

      <div className={`message ${isUser ? "user-message" : "bot-message"}`}>
        {message.content}
      </div>
    </div>
  );
}

export default ChatMessage;