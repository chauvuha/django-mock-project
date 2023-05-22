import React from "react";
import { Link } from "react-router-dom";

const AddButton = () => {
  return (
    <div>
      <Link to='/note/create'>
        <button onSubmit={AddButton}>Add</button>
      </Link>
    </div>
  );
};

export default AddButton;
