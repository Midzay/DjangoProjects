import React, { Component } from 'react';
import axios from 'axios';


export default class Todo extends Component {

    constructor(props) {
        super(props);
        this.state = {
            viewCompleted: false,
            todoList: [1],
            activeItem: {
                title: "",
                completed: false,
                class_task: "1",

            }
        };
    }

    componentDidMount() {
        this.refreshList();
    }

    refreshList = () => {
        axios.get('api/todos')
            .then(res => {
                this.setState({ todoList: res.data });
            }).catch(err => console.log(err));


    };
    displayCompleted = status => {
        if (status) {
            return this.setState({ viewCompleted: true });
        }
        return this.setState({ viewCompleted: false });
    };



    renderItems = (num_task) => {
        const { viewCompleted } = this.state;

        const newItems = this.state.todoList.filter(
            item => item.completed === viewCompleted
        ).filter(item => item.class_task === num_task);
        return newItems.map(item => (

            <div className="mt-2 border" key={item.id}>
                <div className="card-title" name={item.id}>{item.title}</div>
                <div className="button-block-task " >
                    <button className="btn btn-success ml-1" onClick={() => this.complitedItem(item)}>OK</button>
                    <button className="btn btn-warning ml-1" onClick={() => this.editItem(item)}>Edit</button>
                    <button className="btn btn-danger ml-1" onClick={() => this.handleDelete(item)}>Del</button>
                </div>
            </div>

        ));


    };

    togle = () => {
        this.setState({ modal: !this.state.modal });
    };

    handleChange = (e) => {
        let { name, value } = e.target;
        let activeItem = { ...this.state.activeItem, [name]: value }
        this.setState({ activeItem: activeItem })


    }

    handleSubmit = (event) => {
        event.preventDefault();
        const item = this.state.activeItem
        if (item.id) {
            axios.put(`http://localhost:8181/api/todos/${item.id}/`, item)
                .then(res => this.refreshList());
            this.createItem()
            return;
        };
        axios.post("http://localhost:8181/api/todos/", item)
            .then(res => this.refreshList());
        this.createItem()
    };

    handleDelete = item => {
        axios.delete(`http://localhost:8181/api/todos/${item.id}`)
            .then(res => this.refreshList());
        this.createItem()
    };

    createItem = () => {
        const item = { title: "", class_task: "1", completed: false };
        this.setState({ activeItem: item });
    };

    editItem = item => {
        this.setState({ activeItem: item }, () => { console.log('this.state.activeItem: ', this.state.activeItem); });

    };

    complitedItem = (item) => {
        let activeItem = { ...item, completed: true };
        axios.put(`http://localhost:8181/api/todos/${item.id}/`, activeItem)
            .then(res => this.refreshList());
        this.createItem()

    }
    render() {
        return (
            <div className="main-container ">
                <div className="create-task ">
                    <form onSubmit={this.handleSubmit}>

                        <div className="form-row mt-5 ">
                            <div className="form-group col-md-8 ">

                                <input type="text" className="form-control" id="input-task" name="title"
                                    value={this.state.activeItem.title} required onChange={this.handleChange} placeholder="Задача" />

                            </div>
                            <div className="form-group col-md-3">
                                <select name="class_task" className="form-control" id="select-task" value={this.state.activeItem.class_task} onChange={this.handleChange}>
                                    <option value="1">Важно-Срочно</option>
                                    <option value="2">Важно-Не срочно</option>
                                    <option value="3">Не Важно-Срочно</option>
                                    <option value="4">Не важно-Не срочно</option>
                                </select>

                            </div>
                            <div className="form-group col-md-1">

                                <button className="btn btn-success" onClick={this.handlesubmitForm} >Создать</button>
                            </div>

                        </div>
                    </form>

                </div>
                    
                <div className="container fieldset">

                    <div className="row todo-row">
                        <div className="col-6">
                            <div className="title-element">Важно-Срочно</div>
                            {this.renderItems(1)}



                        </div>
                        <div className="col-6">
                            <div className="title-element">Важно-Не срочно</div>
                            {this.renderItems(2)}

                        </div>
                    </div>
                    <div className="row todo-row">
                        <div className="col-6">
                            <div className="title-element">Не Важно-Срочно</div>
                            {this.renderItems(3)}


                        </div>
                        <div className="col-6">
                            <div className="title-element">Не Важно-Не Срочно</div>
                            {this.renderItems(4)}

                        </div>
                    </div>
                </div>


            </div>

        )
    }

}




