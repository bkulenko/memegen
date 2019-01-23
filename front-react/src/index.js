import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import './index.css';

let config = require('./config/config.json')

function ListingItem(props){
    return(
        <div className="listingItem">
            OBRAZEK HERE
            <img src={props.image} alt=""/>
        </div>
    );
}


class Site extends React.Component {
    render(){
        return(
            <div>
                <div><Menu /></div>
                <div><Listing /></div>
            </div>
        );
    }
}

class Menu extends React.Component{
    render(){
    return(
        <div>
            <button className="btn-menu" onClick={() => renderForm()}>
                Generuj mem
            </button>
            <button className="btn-menu" >
                Pokaż memy
            </button>
        </div>
        );
    }
}

function renderForm(){
    return null;
}

class Listing extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            items: [{base64: ""}],
        };
    }
    getListing(){
        return null;
    }
    renderListingItem(i){
        return(
            <ListingItem 
                image={this.state.items[i].base64}
            />
        )
    }
    render(){
        let items = []
        return(
            <div>
                {console.log(this.state.items)}
                {this.renderListingItem(0)}
                

            </div>

        );
        
    }
}



ReactDOM.render(
    <Site />,
    document.getElementById('root')
)