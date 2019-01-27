import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import audoBind from 'react-autobind';
import './index.css';

let config = require('./config/config.json')

function ListingItem(props){
    return(
        <div className="listingItem">
            {props.image}
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
        }
        this.items = []
        this.updateListing=this.updateListing.bind(this)
        this.getListing=this.getListing.bind(this)
    }

    queryButton(){
        return(
            <button className="btn-menu" onClick={this.updateListing}>
                Pokaż memy    
            </button>
        );
    }
    getListing = () => {
        axios.get(config.storage_queryall).then(response=>{
        this.res = response.data
        console.log(this.res)
        return this.res;
        })
    }

    updateListing(){
        let data;
        this.getListing().then(result => {data = result})
    }
    renderListingItem(i){
        return(
            <ListingItem 
                image={this.state.items[i].base64}
            />
        )
    }
    render(){
        return(
            <div>
                {this.queryButton()}
                {this.renderListingItem(0)}
            </div>

        );
        
    }
}




ReactDOM.render(
    <Site />,
    document.getElementById('root')
)