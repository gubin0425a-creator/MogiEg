import os

file_path = 'templates/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 사이드바 반응형 적용
old_sidebar = '<aside id="sidebar" class="w-72 bg-dark-card border-r border-dark-border flex flex-col p-3 transition-all duration-300 shrink-0 z-30">'
new_sidebar = '<div id="sidebar-overlay" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 hidden md:hidden" onclick="toggleMobileSidebar()"></div>\n    <aside id="sidebar" class="fixed md:relative inset-y-0 left-0 w-72 bg-dark-card border-r border-dark-border flex flex-col p-3 transition-transform duration-300 shrink-0 z-50 transform -translate-x-full md:translate-x-0">'
content = content.replace(old_sidebar, new_sidebar)

# 2. JS 수정
old_js_setup = """    function setupSidebar() {
      const sidebar = document.getElementById('sidebar');
      const toggleBtn = document.getElementById('sidebar-toggle-btn');
      const mobileBtn = document.getElementById('mobile-menu-btn');
      if (toggleBtn && sidebar) toggleBtn.addEventListener('click', () => sidebar.classList.toggle('-ml-72'));
      if (mobileBtn && sidebar) mobileBtn.addEventListener('click', () => sidebar.classList.toggle('hidden'));
    }"""

new_js_setup = """    function setupSidebar() {
      const sidebar = document.getElementById('sidebar');
      const toggleBtn = document.getElementById('sidebar-toggle-btn');
      const mobileBtn = document.getElementById('mobile-menu-btn');
      if (toggleBtn && sidebar) toggleBtn.addEventListener('click', () => {
         sidebar.classList.toggle('md:-ml-72');
      });
      if (mobileBtn) mobileBtn.addEventListener('click', toggleMobileSidebar);
    }
    
    function toggleMobileSidebar() {
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('sidebar-overlay');
        if(!sidebar || !overlay) return;
        
        const isOpen = !sidebar.classList.contains('-translate-x-full');
        if(isOpen) {
            sidebar.classList.add('-translate-x-full');
            overlay.classList.add('hidden');
        } else {
            sidebar.classList.remove('-translate-x-full');
            overlay.classList.remove('hidden');
        }
    }"""
content = content.replace(old_js_setup, new_js_setup)

# 3. 사이드바 내 X 버튼이 모바일에서 동작하게
old_close_btn = '<button id="sidebar-toggle-btn" class="p-1.5 rounded-lg text-slate-400 hover:bg-dark-surface hover:text-white transition">'
new_close_btn = '<button onclick="toggleMobileSidebar()" class="md:hidden p-1.5 rounded-lg text-slate-400 hover:bg-dark-surface hover:text-white transition"><i data-lucide="x" class="w-5 h-5"></i></button>\n        <button id="sidebar-toggle-btn" class="hidden md:block p-1.5 rounded-lg text-slate-400 hover:bg-dark-surface hover:text-white transition">'
content = content.replace(old_close_btn, new_close_btn)

# 모바일 UI 개선 (채팅창 영역 마진 최적화)
content = content.replace('<main class="flex-1 overflow-y-auto p-4 md:p-6">', '<main class="flex-1 overflow-y-auto p-3 sm:p-4 md:p-6 pb-24 md:pb-6 relative">')
content = content.replace('<div class="mt-auto pt-2">', '<div class="absolute md:relative bottom-0 left-0 w-full pt-2 bg-dark-bg/80 backdrop-blur-md pb-4 md:pb-0 px-3 md:px-0">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Mobile responsiveness applied.')
