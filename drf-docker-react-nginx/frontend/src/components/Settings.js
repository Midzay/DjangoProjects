
import React, { Component } from 'react';
import axios from 'axios';

export default class Settings extends Component {

    constructor(props) {
        super(props);
        this.state = {
            settings: {
                email: "",
                password: "",
                timeForSend: "",
                rangTodo: ""
            }
        };
    }


    componentDidMount() {
        this.refreshList();
    }

    refreshList = () => {
        axios.get('api/newsmail/settings')
            .then(res => {
                this.setState({ settings: res.data });
            }).catch(err => console.log(err));


    };

    handleChange = (e) => {
        let { name, value } = e.target;
        let settings = { ...this.state.settings, [name]: value }
        this.setState({ settings: settings })


    }

    handleSubmit = (event) => {
        event.preventDefault();
        const settings = this.state.settings
        const json_data = {
            email: settings.email,
            password: settings.password,
            time_for_send: settings.timeForSend,
            rang_todo: settings.rangTodo
        }
        if (settings.email) {
            axios.put("/api/newsmail/settings", json_data)
                .then(res => this.refreshList());
            return;
        };
        axios.post("http://localhost:8181/api/newsmail/settings/", json_data)
            .then(res => this.refreshList());
        this.createItem()
    };


    render() {
        return (
            <div className="main-container">
                <div className="create-task">
                    <form onSubmit={this.handleSubmit} >
                        <div className="container">

                            <legend>Настройки почты</legend>
                            <div className="row">
                                <div className="col-md-3">
                                    <input type="text" id="email" placeholder="Email" className="form-control" name="email" value={this.state.settings.email} required onChange={this.handleChange} />
                                </div>
                                <div className="col-md-3">
                                <input type="password" id="password" placeholder="Password" className="form-control" name="password" value={this.state.settings.password} required onChange={this.handleChange} />
                                </div>
                                <button className="btn btn-success" onClick={this.handlesubmitForm} >Сохранить</button>
                            </div>
                        </div>
                    </form>

                </div>




            </div>

        )
    }

}