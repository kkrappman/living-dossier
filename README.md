# The Living Dossier

A personal app for keeping details about the people in your life. It installs to the iPhone home screen and keeps everything on the device. Nothing is sent to a server.

Live at https://kkrappman.github.io/living-dossier/

- `index.html`, `manifest.webmanifest`, `sw.js`, icons: the app GitHub Pages serves.
- `source/app.html`: the app source, shared with the Claude-hosted version. Run `python3 source/build.py` to rebuild `index.html` after editing it.

Data moves between devices with Backup and transfer: Save a copy on one device, then Receive a copy on the other. The newer copy replaces everything.
