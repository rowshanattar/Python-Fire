curl -X POST 'http://0.0.0.0:8000/summarize' \
  -H 'Content-Type: application/json' \
  -d '{"topic": "Google", "sentences": 1}'
