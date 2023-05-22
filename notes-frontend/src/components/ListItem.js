import React from 'react'
import { Link } from 'react-router-dom'

const ListItem = ({ notepage }) => {
  return (
    <Link to={`/note/${notepage.id}`}>
      <div className="notes-list-item">
      <h3>{notepage.body}</h3>
      </div>
    </Link>
  )
}

export default ListItem
