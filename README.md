Development:
```bash
# Initial build (only needed once)
docker compose up --build -d
# Stop
docker compose down
# Run built container
docker compose up -d
```

Production: (needs .env.prod)
```bash
docker-compose -f docker-compose.prod.yml --env-file .env.prod up -d --build
```
