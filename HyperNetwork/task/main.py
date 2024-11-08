# Run related Docker commands in the terminal, and press the `Check` button.
# Bash command
# Task 2
# docker run -d --name hyper-postgres --env POSTGRES_PASSWORD=hyper2023 --env POSTGRES_USER=hyper --env POSTGRES_DB=hyper-db --network hyper-network -p 5432:5432 -v hyper-volume:/var/lib/postgresql/data postgres:15.3
# Task 3
# docker run -d