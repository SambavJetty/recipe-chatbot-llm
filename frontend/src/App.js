import Chatbot from "./Chatbot"
import "./App.css"

function App() {
  return (
    <div className="App">
      <div className="app-container">
        <header className="app-header">
          <h1>AI Assistant</h1>
          <p>Powered by your fine-tuned Vertex AI model</p>
        </header>
        <main className="app-main">
          <Chatbot />
        </main>
      </div>
    </div>
  )
}

export default App
