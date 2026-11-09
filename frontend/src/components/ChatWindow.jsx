import { useState, useRef, useEffect } from "react";
import axios from "axios";
import { Bot, Trash2 } from "lucide-react";

import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";

const API_URL = "http://localhost:8000";

function ChatWindow() {
  const [messages, setMessages] = useState([
    {
      role: "model",
      content: "Hello! Welcome to AI Customer Support. How can I help you today?"
    }
  ]);

  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const sendMessage = async () => {
    const text = message.trim();

    if (!text || loading) return;

    const previousMessages = messages.filter(
      (item) => item.role === "user" || item.role === "model"
    );

    const updatedMessages = [
      ...previousMessages,
      { role: "user", content: text }
    ];

    setMessages(updatedMessages);
    setMessage("");
    setLoading(true);
    setError("");

    try {
      const response = await axios.post(`${API_URL}/chat`, {
        message: text,
        history: previousMessages.slice(-20)
      });

      setMessages([
        ...updatedMessages,
        {
          role: "model",
          content: response.data.reply
        }
      ]);

    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Unable to connect to AI support. Please try again."
      );

    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([
      {
        role: "model",
        content: "Hello! Welcome to AI Customer Support. How can I help you today?"
      }
    ]);

    setError("");
    setMessage("");
  };

  return (
    <div className="chat-container">

      <header className="chat-header">
        <div className="header-info">
          <div className="header-icon">
            <Bot size={24} />
          </div>

          <div>
            <h2>AI Support Assistant</h2>
            <span>Online · Powered by Gemini</span>
          </div>
        </div>

        <button className="clear-btn" onClick={clearChat} title="Clear chat">
          <Trash2 size={20} />
        </button>
      </header>

      <div className="chat-body">

        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg} />
        ))}

        {loading && (
          <div className="typing">
            AI is thinking...
          </div>
        )}

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        <div ref={bottomRef} />

      </div>

      <ChatInput
        message={message}
        setMessage={setMessage}
        sendMessage={sendMessage}
        loading={loading}
      />

      <p className="footer-text">
        AI responses may not always be accurate.
      </p>

    </div>
  );
}

export default ChatWindow;