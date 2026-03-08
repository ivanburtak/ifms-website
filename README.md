Development:
```bash
docker compose up --build -d
```

Production: (needs .env.prod)
```bash
docker compose -f docker-compose.prod.yml up -d --build
```
