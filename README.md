# Kompetenzmatrizen ZH

Öffentlich zugängliche Kompetenzmatrizen des Projekts **Modulentwicklung ZH** für die ICT-Module
der Fachrichtungen Applikationsentwicklung und Plattformentwicklung nach **BiVo2021**.

Live: **https://kompetenzmatrix.ch** · Bearbeiten: **/admin/** (Decap CMS)

## Was ist das hier?

Das **Arbeitsrepo** (Single Source of Truth) für die Matrizen. Inhalt = strukturierte YAML-Daten,
gerendert mit [Hugo](https://gohugo.io) (+ Theme `hugo-theme-learn` als Submodul).

```
content/<cluster>/<modul>/
  _index.md               # Kompetenzmatrix (YAML) + Bloom-Analyse/Änderungsprotokoll
  umsetzungsvorschlag.md   # Lektionsplanung
  handlungssituationen.md  # Handlungssituationen
layouts/                   # Matrix-Rendering (partials/matrix.html) + Navigation
static/admin/              # Decap CMS (Web-Editor)
schema/                    # JSON-Schema der Moduldaten
scripts/validate_modules.py# CI-Validierung (EHB-Regeln)
.github/workflows/         # validate.yml (PR) + deploy.yml (rsync nach it.bzz.ch)
```

Cluster: `cluster-api`, `cluster-cloud`, `cluster-data`, `cluster-math`, `cluster-org`,
`cluster-platform`.

## Versionen

`main` enthält die aktuelle (vormals „v2") Matrix. Die alte **Version 1** ist auf dem Branch
`v1-archive` eingefroren (nicht in Bearbeitung, nicht auf der Website).

## Lokale Entwicklung

```bash
git clone --recurse-submodules <repo-url>
cd kompetenzmatrix
hugo server
```

## Beitragen

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) — Editieren via CMS oder PR, inkl. EHB-Inhaltsregeln.
Den vollständigen Ablauf (Bearbeiten → CI → Deploy) zeigt
[docs/matrix-bearbeiten.md](docs/matrix-bearbeiten.md).

## Setup-Hinweise (einmalig)

- **CMS-Auth** (Open Authoring): selbst-gehostetes PHP-Relay auf dem Server unter
  `https://kompetenzmatrix.ch/cms-oauth` (Code: `/var/www/kompetenzmatrix.ch/cms-oauth/index.php`).
  GitHub-OAuth-App erstellen (Callback `https://kompetenzmatrix.ch/cms-oauth/callback`),
  `client_id`/`client_secret` in `/etc/cms-oauth-config.php` eintragen. `base_url` steht in
  `static/admin/config.yml`. Das Relay ist via `rsync --exclude=cms-oauth/` vor Deploys geschützt.
- **Deploy** (kein root!): Auf dem Server einen **unprivilegierten** Benutzer anlegen, dem nur
  das Web-Verzeichnis gehört:
  ```bash
  sudo adduser --disabled-password --gecos "" deploy
  sudo install -d -o deploy -g www-data /var/www/kompetenzmatrix
  sudo -u deploy mkdir -p /home/deploy/.ssh && sudo -u deploy chmod 700 /home/deploy/.ssh
  # Public-Key des Deploy-Keys auf rsync einschränken (forced command via rrsync):
  #   command="rrsync /var/www/kompetenzmatrix",no-pty,no-agent-forwarding,no-port-forwarding,no-X11-forwarding ssh-ed25519 AAAA... deploy
  ```
  Damit kann der Key (selbst wenn er leakt) **nur** in dieses Verzeichnis rsyncen — keine Shell,
  kein root. GitHub-Konfiguration:
  - Secret `DEPLOY_SSH_KEY` — privater Key des `deploy`-Users.
  - Secret `DEPLOY_KNOWN_HOSTS` — Host-Key pinnen (`ssh-keyscan it.bzz.ch`); ohne ihn fällt der
    Workflow auf TOFU-Keyscan zurück.
  - Variablen `DEPLOY_HOST` (`it.bzz.ch`), `DEPLOY_USER` (`deploy`), `DEPLOY_PATH`. Der
    Workflow bricht ab, falls `DEPLOY_USER=root`.
    - **Mit** rrsync-Forced-Command: `DEPLOY_PATH` = `./` (rrsync rootet bereits auf das Verzeichnis).
    - **Ohne** (nur unprivilegierter User, der das Verzeichnis besitzt): `DEPLOY_PATH` = `/var/www/kompetenzmatrix/`.
