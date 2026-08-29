# -*- coding: utf-8 -*-
"""
MogiEgg 데스크톱 프로그램 런처

- 로컬 정적 서버(127.0.0.1)를 백그라운드 스레드로 실행
- 기본 브라우저로 스튜디오 자동 오픈
- tkinter 제어판 제공 (GUI 불가 환경에서는 콘솔 모드로 자동 전환)

빌드(Windows):
    pip install pyinstaller
    pyinstaller --clean --noconfirm mogieg.spec
    -> dist\\MogiEgg.exe
"""
import os
import sys
import socket
import threading
import time
import webbrowser


def find_free_port(start=8501, tries=50):
    for p in range(start, start + tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', p))
                return p
            except OSError:
                continue
    return start


def start_server(host='127.0.0.1', port=None):
    """서버를 백그라운드로 실행하고 (httpd, 실제포트) 반환."""
    from server import create_server
    if port is None:
        port = find_free_port()
    httpd = create_server(host, port)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd, port


def main():
    httpd, port = start_server('127.0.0.1')
    url = 'http://127.0.0.1:%d' % port
    print('🥚 MogiEgg 스튜디오 실행 중 -> %s' % url)

    try:
        import tkinter as tk
    except Exception:
        # GUI 불가 환경(서버/헤드리스): 브라우저만 열고 콘솔 대기
        try:
            webbrowser.open(url)
        except Exception:
            pass
        print('(GUI 없이 콘솔 모드로 실행 중 — Ctrl+C 로 종료)')
        try:
            while True:
                time.sleep(3600)
        except KeyboardInterrupt:
            print('종료합니다.')
        return

    BG = '#0a0e14'
    CARD = '#121720'
    SURFACE = '#181f2a'
    FG = '#e5e7eb'
    MUTED = '#94a3b8'
    BRAND = '#10b981'
    FONT = ('Malgun Gothic', 10)

    root = tk.Tk()
    root.title('모기에그 (MogiEgg) 스튜디오')
    root.geometry('440x250')
    root.resizable(False, False)
    root.configure(bg=BG)

    try:
        root.iconphoto(False, tk.PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'mascot.png')))
    except Exception:
        pass

    # 상단
    tk.Label(root, text='🥚', bg=BG, font=('Malgun Gothic', 28)).pack(pady=(18, 2))
    tk.Label(root, text='모기에그 (MogiEgg)', bg=BG, fg=FG, font=('Malgun Gothic', 16, 'bold')).pack()
    tk.Label(root, text='우리만의 AI 숏폼 & 마케팅 스튜디오', bg=BG, fg=MUTED, font=FONT).pack(pady=(0, 10))

    # 상태 바
    status = tk.Label(
        root,
        text='✅ 스튜디오 실행 중 — %s' % url,
        bg=CARD, fg=BRAND,
        font=('Malgun Gothic', 10, 'bold'),
        padx=16, pady=8,
    )
    status.pack(fill='x', padx=24)

    # 버튼
    btns = tk.Frame(root, bg=BG)
    btns.pack(pady=14)

    def open_studio():
        webbrowser.open(url)

    def quit_app():
        try:
            httpd.shutdown()
        except Exception:
            pass
        root.destroy()

    tk.Button(btns, text='🌐 스튜디오 열기', command=open_studio,
              bg=BRAND, fg='#04120c', activebackground='#0d9b6e', activeforeground='#04120c',
              relief='flat', font=('Malgun Gothic', 10, 'bold'), padx=18, pady=8,
              cursor='hand2').pack(side='left', padx=6)
    tk.Button(btns, text='🛑 종료', command=quit_app,
              bg=SURFACE, fg=FG, activebackground='#26303f', activeforeground=FG,
              relief='flat', font=('Malgun Gothic', 10), padx=18, pady=8,
              cursor='hand2').pack(side='left', padx=6)

    tk.Label(root, text='브라우저에서 실행됩니다 · 종료하면 스튜디오도 함께 꺼집니다',
             bg=BG, fg='#64748b', font=('Malgun Gothic', 9)).pack(side='bottom', pady=(0, 12))

    # 브라우저 자동 오픈
    root.after(800, open_studio)
    root.protocol('WM_DELETE_WINDOW', quit_app)
    root.mainloop()


if __name__ == '__main__':
    main()
