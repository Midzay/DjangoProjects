import React from 'react'



export default (props) => (
    <div>
        <button  className="btn btn-secondary" onClick={props.onClick} name={props.name} id={props.name} >{props.title}</button>
    </div>
)