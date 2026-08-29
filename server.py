# -*- coding: utf-8 -*-
"""
MogiEgg — 정적 스튜디오 로컬 서버 (표준 라이브러리만 사용)

- /            -> templates/index.html (모기에그 스튜디오)
- /index.html  -> templates/index.html
- /static/*    -> static/* (마스코트, 이미지 등)

별도 의존성 없이 실행 가능합니다:
    python server.py
"""
import os
import sys
import http.server
import socketserver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
}


class MogiEggHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?', 1)[0]

        if path in ('/', '/index.html'):
            self._serve_file(os.path.join(TEMPLATE_DIR, 'index.html'))
        elif path.startswith('/static/'):
            # 경로 탈출 방지 (.. 필터링)
            rel = os.path.normpath(path[len('/static/'):])
            self._serve_file(os.path.join(STATIC_DIR, rel))
        else:
            self.send_error(404)

    def _serve_file(self, filepath):
        filepath = os.path.normpath(filepath)
        # 반드시 허용된 디렉터리 안의 파일만 제공
        allowed_dirs = (os.path.normpath(TEMPLATE_DIR), os.path.normpath(STATIC_DIR))
        if not any(filepath.startswith(d + os.sep) or filepath == d for d in allowed_dirs):
            self.send_error(404)
            return
        if not os.path.isfile(filepath):
            self.send_error(404)
            return

        ext = os.path.splitext(filepath)[1].lower()
        self.send_response(200)
        self.send_header('Content-Type', MIME_TYPES.get(ext, 'application/octet-stream'))
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        with open(filepath, 'rb') as f:
            self.wfile.write(f.read())

    def log_message(self, fmt, *args):
        sys.stderr.write("[MogiEgg] %s\n" % (fmt % args))


def main():
    port = int(os.environ.get('PORT', 8501))
    handler = MogiEggHandler
    with socketserver.ThreadingTCPServer(('0.0.0.0', port), handler) as httpd:
        print(f'🥚 MogiEgg 스튜디오 실행 중 -> http://localhost:{port}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n서버를 종료합니다.')


if __name__ == '__main__':
    main()
