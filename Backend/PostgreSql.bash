//Set Up PostgreSQL Database
docker run --name flight_postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres