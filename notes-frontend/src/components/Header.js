import React from 'react'
import { Link } from 'react-router-dom'

const Header = () => {
  return (
    <div>
      <div className="notes-header">
        <Link className="notes-title" to="/">All Posts</Link>

      </div>
    </div>
  )
}

export default Header
