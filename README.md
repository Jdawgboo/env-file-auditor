# env-file-auditor

A no-dependency CLI for simple dotenv-style files. It flags duplicate keys, blank values, and malformed entries without reading any network resource.

```bash
python env_file_auditor.py .env
python -m unittest -v
```

This is a text auditor, not a secrets manager. MIT licensed.