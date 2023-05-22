import React, { useState, useEffect } from "react";
import ListItem from "../components/ListItem";
import { Link } from "react-router-dom";
import AddButton from "../components/AddButton";

const NotesListPage = () => {
  let [notes, setNotes] = useState([]);
  useEffect(() => {
    getNotes();
  }, []);

  let getNotes = async () => {
    let response = await fetch("/api/notes/");
    let data = await response.json();
    console.log(data);
    setNotes(data);
  };

  // let createNote = async () => {
  //   await fetch(`api/note/create`, {
  //     method: "CREATE",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify(notes),
  //   });
  // };

  // let handleCreate = () => {
  //   createNote()
  // }

  return (
    <div className="notes">
      <div className="notes-header">
        <p className="notes-count">Total number: {notes.length}</p>
      </div>
      <AddButton />

      <div className="notes-list">
        {notes.map((note) => (
          <ListItem notepage={note} />
        ))}
      </div>
    </div>
  );
};

export default NotesListPage;
