import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const NotePage = () => {
  const { id } = useParams();

  let [note, setNote] = useState(null);
  let [notes, setNotes] = useState(null);

  useEffect(() => {
    getNote();
    getNotes();
    console.log(id)
  }, [id]);

  let getNote = async () => {
    let response = await fetch(`/api/note/${id}`);
    let data = await response.json();
    // console.log(data);
    setNote(data);
  };

  let getNotes = async () => {
    let response = await fetch("/api/notes/");
    let data = await response.json();
    // console.log(data);
    setNotes(data);
  };

  let updateNote = async () => {
    fetch(`/api/note/${id}/update`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(note),
    });
  };

  let handleSubmit = () => {
    updateNote();
  };

  let deleteNote = async () => {
    await fetch(`/api/note/${id}/delete`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(note),
    });
  };

  let handleDelete = () => {
    deleteNote();
  };

  let createNote = async () => {
    await fetch(`/api/note/create`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(note),
    });
  };

  return (
    <div>
      <div className="note">
        {id !== "create" ? (
          <div>
            <button onClick={handleSubmit}>Update</button>
            <button onClick={handleDelete}>Delete</button>
          </div>
        ) : (
          <div>
            <button onClick={createNote}>Done</button>
          </div>
        )}

        
        {/* Remember that {id} is the current id in the link because of useParams */}
        <h2 className="note-id">Note ID: {id}</h2>
        <textarea
          onChange={(e) => {
            setNote({ ...note, body: e.target.value });
          }}
          defaultValue={note?.body}
        ></textarea>
      </div>
    </div>
  );
};

export default NotePage;
