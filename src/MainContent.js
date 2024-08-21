// src/components/MainContent.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MainContent = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/items/')
      .then(response => {
        setItems(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the data!", error);
      });
  }, []);

  return (
    <main>
      <h2>Item List</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}: {item.description}</li>
        ))}
      </ul>
    </main>
  );
};

export default MainContent;
