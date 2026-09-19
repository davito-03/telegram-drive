<p align="center">
  <img src="https://davito.es/media/projects/davogram.jpg" width="160" alt="Telegram Drive">
</p>

<h1 align="center">telegram-drive</h1>

<p align="center">
  Userbot de Telegram: lo que mandas a <strong>Mensajes Guardados</strong> acaba en Google Drive <em>sin comprimir</em>.<br>
  Pyrogram + rclone. Lo uso para películas hacia Jellyfin.
</p>

<p align="center">
  <a href="https://davito.es/proyectos/telegram-drive">Ficha</a>
  ·
  <a href="https://davito.es/proyectos">Portfolio</a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img alt="Pyrogram" src="https://img.shields.io/badge/Pyrogram-Telegram-26A5E4?logo=telegram&logoColor=white">
  <img alt="rclone" src="https://img.shields.io/badge/rclone-Google%20Drive-4285F4?logo=googledrive&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow">
</p>

No es un bot de BotFather. Es una sesión de **usuario** (API_ID / API_HASH). El Bot API corta en ~20&nbsp;MB; este camino no.

## Flujo

```
Saved Messages → cola en disco (queue.json, no un broker) → rclone
                                              ↘ Drive API resumable (fallback)
```

La carpeta de Drive es `RCLONE_DEST` (env), no un path de homelab. El contenedor corre como uid 1000; `rclone.conf` se monta en `$HOME/.config/rclone/`.

```bash
pytest
```

Pides el nombre del archivo antes de subir. No hay ffmpeg de recodificar: la calidad original se queda.

`userbot_pc_amd.py` es una variante para un PC; el de producción es `userbot_drive.py`.

## Arranque

```bash
cp .env.example .env   # API_ID, API_HASH en my.telegram.org
# rclone config   → remote "gdrive"
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python userbot_drive.py
```

La primera vez Pyrogram pide teléfono y código y escribe `my_account.session`. **No lo subas.**

```bash
docker compose up -d --build
```

## Secretos (fuera del repo)

`*.session`, `rclone.conf`, `credentials.json`, `token.json`, `gdrive_credentials.json`, `queue.json` con rutas locales. `.env` vacío en git.

Diagrama: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
