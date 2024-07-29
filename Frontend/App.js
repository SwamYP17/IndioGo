//Creating the main frontend for the flight status:

import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    const fetchFlights = async () => {
      const response = await fetch('http://localhost:5000/flights');
      const data = await response.json();
      setFlights(data);
    };

    fetchFlights();
    const interval = setInterval(fetchFlights, 5000); // Fetch updates every 5 seconds
    return () => clearInterval(interval); // Clean up
  }, []);

  return (
    <div className="App">
      <h1>Flight Status Updates</h1>
      <table>
        <thead>
          <tr>
            <th>Flight Number</th>
            <th>Status</th>
            <th>Gate</th>
          </tr>
        </thead>
        <tbody>
          {flights.map((flight) => (
            <tr key={flight.flightNumber}>
              <td>{flight.flightNumber}</td>
              <td>{flight.status}</td>
              <td>{flight.gate}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;