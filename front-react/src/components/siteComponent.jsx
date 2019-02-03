import React, { Component } from "react";

class Site extends Component {
  constructor() {
    super();
    this.state = {
      pictures: []
    };
  }
  componentDidMount() {
    fetch("http://localhost:8000/storage/")
      .then(results => {
        return results.json();
      })
      .then(data => {
        this.setState({ pictures: data });
      });
  }
  render() {
    console.log(this.state.pictures);
    return (
      <div>
        {this.state.pictures.map(picture => {
          let pic_src = "data:image/jpeg;base64,";
          pic_src = pic_src + picture.base64;
          return (
            <div>
              <img src={pic_src} />
            </div>
          );
        })}
      </div>
    );
  }
}

export default Site;
