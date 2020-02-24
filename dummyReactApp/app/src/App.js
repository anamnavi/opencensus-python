import './App.css';
import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      posts: [],
      name1: "",
      name2: "",
      name3: "",
      isToggleOn: true
    }
    this.handleClick = this.handleClick.bind(this);
  }

  getData = () => {
    var xhr = new XMLHttpRequest();
    let currentComponent = this;
    xhr.addEventListener('load', ()=>{
      console.log(xhr.responseText);
      var jsonResponse = JSON.parse(xhr.responseText);
      currentComponent.setState({name1: jsonResponse['name']})

    })
    xhr.open('GET', '/getmethod1')
    xhr.send()
  }

    getData2 = () => {
    var xhr = new XMLHttpRequest();
    let currentComponent = this;
    xhr.addEventListener('load', ()=>{
      console.log(xhr.responseText);
      var jsonResponse = JSON.parse(xhr.responseText);
      currentComponent.setState({name2: jsonResponse['name']})
    })
    xhr.open('GET', '/getmethod2')
    xhr.send()
  }

    getData3 = () => {
    var xhr = new XMLHttpRequest();
    let currentComponent = this;
    xhr.addEventListener('load', ()=>{
      console.log(xhr.responseText);
      var jsonResponse = JSON.parse(xhr.responseText);
      currentComponent.setState({name3: jsonResponse['name']})
    })
    xhr.open('GET', '/getmethod3')
    xhr.send()
  }

  handleClick() {
    this.setState(state => ({
      isToggleOn: !state.isToggleOn
    }));
  }


  render() {
    const { posts } = this.state;
    return (
      <div>
        <button onClick={this.getData}>Call Method1</button>
        <button onClick={this.getData2}>Call Method2</button>
        <button onClick={this.getData3}>Call Method3</button>
        <p>Name 1: {this.state.name1}</p>
        <p>Name 2: {this.state.name2}</p>
        <p>Name 3: {this.state.name3}</p>
      </div>

    );
  }
}
export default App;
