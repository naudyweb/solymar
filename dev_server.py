"""Local dev server that resolves clean URLs like production's .htaccess.

Internal links use extensionless URLs (`/islas-ballestas`, `blog/`), which
`python3 -m http.server` can't serve. This maps `/foo` -> `foo.html` when that
file exists, and keeps the default behaviour for everything else.

Usage: python3 dev_server.py [port]   (default 8000)
"""
import http.server
import os
import sys


class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = super().translate_path(path)
        if not os.path.exists(local) and os.path.exists(local + ".html"):
            return local + ".html"
        return local


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Serving on http://localhost:{port}")
    http.server.ThreadingHTTPServer(("", port), CleanURLHandler).serve_forever()
