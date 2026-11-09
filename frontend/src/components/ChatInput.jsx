import { Send } from "lucide-react";

function ChatInput({ message, setMessage, sendMessage, loading }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    sendMessage();
  };

  return (
    <form className="chat-input" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Ask me anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        disabled={loading}
      />

      <button type="submit" disabled={loading || !message.trim()}>
        <Send size={18} />
      </button>
    </form>
  );
}

export default ChatInput;