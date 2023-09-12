import './App.css';
import React from 'react'


class App extends React.Component {
  constructor() {
    super();
    this.state={
        inputValue: '',
        setInputValue: ''
    }
  }

  handleInputChange = (event) => {
    this.state.setInputValue(event.target.value);
  };

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <input
            type="text"
            placeholder="Enter text here"
            value={this.state.inputValue} // Set the input value
            onChange={this.state.handleInputChange} // Handle input changes
          />
        </header>
      </div>
    )
  };
}

export default App;
