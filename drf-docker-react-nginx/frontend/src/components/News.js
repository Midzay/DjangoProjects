import React, { Component } from 'react'
import axios from 'axios';


export default class News extends Component {

    constructor(props) {
        super(props);
        console.log(props)

        this.state = {
            themeNews: 'Python,Javascript',
            items: props.items,
            emails: props.emails
        }
    }
    componentDidMount() {

        this.getEmail()
    }

    getNews() {
        axios.get('api/newsmail/news', { params: { q: this.state.themeNews } })
            .then((response) => {
                console.log(response.data)
                this.setState({ items: response.data })
            }
            );
    }


    getEmail() {
        axios.get('api/newsmail/email')
            .then((response) => {
                console.log(response.data)
                this.setState({ emails: response.data })
            }
            );
    }

    changeQuery(event) {
        this.setState({ themeNews: event.target.value })
    }


    render() {


        return (
            <div>
                <p>Здесь можно выбрать статьи с хабра по конкретной теме</p>
                <div className="container fieldset">
                    <div className="container ">
                        <div className="row mt-1 ">
                            <div className="col-md-4 card ">
                                <form method="get">
                                    <label htmlFor="theme">Интересующая тема</label>
                                    <input type="text" onChange={this.changeQuery.bind(this)} className="form-control" id="theme" aria-describedby="text" name="themenews" defaultValue={this.state.themeNews} />
                                </form>
                                <button type="submit" onClick={this.getNews.bind(this)} className="btn btn-success mt-4">Отправить</button>
                            </div>

                            <div className="col-md-8 text-left">

                                {Object.keys(this.state.items).map((item, index) => (
                                    <li key={index} style={{ paddingLeft: 5 }} dangerouslySetInnerHTML={{ __html: this.state.items[item] }}></li>))}
                            </div>
                        </div>

                    </div>
                </div>

                {/* 2 блок */}
                <hr />
                <h6>Письма</h6>
                <div className="container fieldset left-text">

                        {Object.keys(this.state.emails).map((item, index) => (
                            <div key={index} className="row" >
                                <div className="col-md-5" >
                                    {this.state.emails[item][0]}
                                </div>
                                <div className="col-md-7">
                                    {this.state.emails[item][1]}
                                </div>
                            </div>))}
                    
                </div>
            </div>
        )
    }

}
