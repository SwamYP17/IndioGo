In this project, I developed a Flight Status Tracking Application that provides real-time updates on flight statuses. The application allows users to view the current status of flights,
including any delays or gate changes. I utilized a combination of modern technologies and libraries to create a seamless user experience.

1.Tech Stack
a)Frontend
->React.js: I used React.js to build a responsive and dynamic user interface. The frontend fetches flight data from the backend and displays it in a user-friendly format.
->CSS: I styled the application using CSS to ensure it is visually appealing and easy to navigate.
b)Backend
->Flask: I chose Flask as the web framework for the backend. It allows me to create RESTful APIs to serve flight data to the frontend efficiently.
->PostgreSQL: I used PostgreSQL as the relational database to store flight information. This ensures data integrity and allows for complex queries.
->Psycopg2: This library enables the Flask application to connect to the PostgreSQL database and execute SQL queries.
2. Additional Tools and Libraries
->Docker: I used Docker to run the PostgreSQL database in a containerized environment, making it easy to set up and manage.
->JavaScript Fetch API: I utilized the Fetch API in the React application to make asynchronous requests to the Flask backend for retrieving flight data.
Conclusion
Overall, this project provided me with a practical understanding of full-stack development.
I gained hands-on experience in integrating a frontend application with a backend service and managing a relational database. 
The combination of these technologies allowed me to create a functional and efficient flight status tracking application that can be extended with additional features in the future.

The Poject Structure is as follows:

Project Structure
flight-status-app/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── App.css
│   ├── package.json
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── database/
│   ├── init_db.py
