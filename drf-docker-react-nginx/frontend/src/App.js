import React, { Component } from "react";
import ReactDOM from "react-dom";
import Topmenu from './components/Topmenu'
import Todo from './components/Todo'
import Settings from './components/Settings'
import axios from 'axios';

import News from './components/News'


class App extends Component {
    state = {
        topmenu: [
        {  name: 'Todo', title: 'Список дел', comp: <Todo /> },
        { name: 'News', title: 'Список новостей', comp: <News/> },
        {  name: 'Settings', title: 'Настройки', comp: <Settings /> }
        ],
        centerComponent: <Todo/>,
        items: [],
        emails: [],
        themeNews: 'Python,Javascript',


    }


    componentDidMount() {
        this.getNews()
        this.getEmail()
        console.log(this.state.emails)
    }

    getNews() {
        axios.get('api/newsmail/news',{params:{q: this.state.themeNews}})
            .then((response) => {
                // console.log(response.data)
                this.setState({ items: response.data })
            }
            );
    }


    getEmail() {
        axios.get('api/newsmail/email')
            .then((response) => {
                this.setState({ emails: response.data })
            }
            );
    }

    changeQuery(event) {
        this.setState({ themeNews: event.target.value })
    }


    handleChangeComponent = (myComponent) => {
        if (myComponent.type.name =='News'){
            this.setState({
                centerComponent: <News items= {this.state.items} emails = {this.state.emails} />
            })    
        }
        else {
        this.setState({
            centerComponent: myComponent
        })
    }
    }

    render() {

        return (
            <div>
                <div className="row" >
                    {this.state.topmenu.map((elementbutton,index) => {
                        
                        return (
                            
                            <div  key={index} style={{margin:10}}>
                                <Topmenu
                                    onClick={this.handleChangeComponent.bind(this, elementbutton.comp)}
                                    name={elementbutton.name}
                                    title={elementbutton.title}
                                />
                            </div>
                        )
                    })}
                </div>

                {this.state.centerComponent}
            </div>
        )
    }
}
export default App;
