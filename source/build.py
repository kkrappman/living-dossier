# Wraps the shared app source into the home-screen app (index.html at the repo root)
import re, pathlib
src = pathlib.Path(__file__).parent / 'app.html'.read_text()
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#2E6B57">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Dossier">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>html,body{margin:0}</style>
</head>
<body>
'''
tail = '''
<script>
if ('serviceWorker' in navigator) window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
</script>
</body>
</html>
'''
(pathlib.Path(__file__).parent.parent / 'index.html').write_text(head + src + tail)
print('built', len(head + src + tail))
