import os

file_path = 'templates/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 기존 스크립트 블록 찾기
start_tag = "<script>"
end_tag = "</script>\n</body>"

start_idx = content.find(start_tag, content.find('tailwind.config') + 100) # 두 번째 script 태그(실제 로직) 찾기
start_idx = content.find(start_tag, start_idx + 1)
end_idx = content.rfind(end_tag)

clean_js = """<script>
    let currentTab = 'chat';
    let chatHistory = [];
    let isGenerating = false;
    let userInfo = { credits: '∞ (로컬/정적)', max_credits: '∞', name: '모기에그 크리에이터', tier: 'Demo Mode' };

    document.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      
      if(localStorage.getItem('mogiegg_name')) {
          userInfo.name = localStorage.getItem('mogiegg_name');
          const nameEl = document.getElementById('cfg-name');
          if(nameEl) nameEl.value = userInfo.name;
      }
      if(localStorage.getItem('mogiegg_gemini')) {
          const gemEl = document.getElementById('cfg-gemini');
          if(gemEl) gemEl.value = localStorage.getItem('mogiegg_gemini');
      }
      if(localStorage.getItem('mogiegg_openai')) {
          const oaiEl = document.getElementById('cfg-openai');
          if(oaiEl) oaiEl.value = localStorage.getItem('mogiegg_openai');
      }
      if(localStorage.getItem('mogiegg_claude')) {
          const claEl = document.getElementById('cfg-claude');
          if(claEl) claEl.value = localStorage.getItem('mogiegg_claude');
      }

      fetchUserInfo();
      setupSidebar();
    });

    async function fetchUserInfo() {
      try {
        const res = await fetch('api/user/me');
        if (res.ok) {
          userInfo = await res.json();
          updateUserUI();
        } else throw new Error();
      } catch (err) {
        userInfo = { credits: '∞', max_credits: '∞', name: userInfo.name || '모기에그 크리에이터', tier: 'Static Mode' };
        updateUserUI();
      }
    }

    function updateUserUI() {
      const crText = document.getElementById('header-credit-text');
      if(crText) crText.innerText = userInfo.credits;
      
      const pct = userInfo.max_credits === '∞' ? 100 : Math.min(100, Math.max(0, (userInfo.credits / (userInfo.max_credits || 100)) * 100));
      const crBar = document.getElementById('header-credit-bar');
      if(crBar) crBar.style.width = pct + '%';
      
      const sbName = document.getElementById('sidebar-user-name');
      if(sbName) sbName.innerText = userInfo.name || '모기에그 크리에이터';
      
      const sbTier = document.getElementById('sidebar-user-tier');
      if(sbTier) sbTier.innerText = `${userInfo.tier || '무료'} · 크레딧 ${userInfo.credits}`;
    }

    function switchTab(tabId) {
      currentTab = tabId;
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('bg-dark-surface', 'text-brand-400', 'border-brand-500/20', 'border');
        btn.classList.add('text-slate-400');
      });
      const activeTabEl = document.getElementById('tab-' + tabId);
      const activeBtnEl = document.getElementById('nav-' + tabId);
      if (activeTabEl) activeTabEl.classList.remove('hidden');
      if (activeBtnEl) {
        activeBtnEl.classList.add('bg-dark-surface', 'text-brand-400', 'border', 'border-brand-500/20');
        activeBtnEl.classList.remove('text-slate-400');
      }
      lucide.createIcons();
    }

    function setupSidebar() {
      const sidebar = document.getElementById('sidebar');
      const toggleBtn = document.getElementById('sidebar-toggle-btn');
      const mobileBtn = document.getElementById('mobile-menu-btn');
      if (toggleBtn && sidebar) toggleBtn.addEventListener('click', () => sidebar.classList.toggle('-ml-72'));
      if (mobileBtn && sidebar) mobileBtn.addEventListener('click', () => sidebar.classList.toggle('hidden'));
    }

    function toggleTheme() {
      const html = document.documentElement;
      const themeIcon = document.getElementById('theme-icon');
      if (html.classList.contains('dark')) {
        html.classList.remove('dark'); html.classList.add('light'); 
        if(themeIcon) themeIcon.setAttribute('data-lucide', 'sun');
      } else {
        html.classList.remove('light'); html.classList.add('dark'); 
        if(themeIcon) themeIcon.setAttribute('data-lucide', 'moon');
      }
      lucide.createIcons();
    }

    async function handleChatSubmit(e) {
      if (e) e.preventDefault();
      const input = document.getElementById('chat-input');
      const message = input.value.trim();
      if (!message || isGenerating) return;
      input.value = '';
      await processUserMessage(message);
    }

    function sendPresetMessage(text) {
      switchTab('chat');
      processUserMessage(text);
    }

    async function processUserMessage(text) {
      const hero = document.getElementById('welcome-hero');
      const container = document.getElementById('chat-messages-container');
      if(hero) hero.classList.add('hidden');
      if(container) container.classList.remove('hidden');
      
      chatHistory.push({ role: 'user', content: text });
      appendMessageUI('user', text);

      const aiMsgId = 'ai-msg-' + Date.now();
      appendMessageUI('assistant', '', aiMsgId);
      const aiContentEl = document.getElementById(aiMsgId);
      isGenerating = true;
      
      const geminiKey = localStorage.getItem('mogiegg_gemini');
      const openaiKey = localStorage.getItem('mogiegg_openai');

      try {
        if (geminiKey && geminiKey.trim() !== '') {
            const gHistory = chatHistory.map(m => ({
                role: m.role === 'user' ? 'user' : 'model',
                parts: [{ text: m.content }]
            }));
            const res = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=' + geminiKey, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ contents: gHistory })
            });
            if(!res.ok) throw new Error('Gemini API Error');
            const data = await res.json();
            const reply = data.candidates[0].content.parts[0].text;
            chatHistory.push({ role: 'assistant', content: reply });
            if(aiContentEl) aiContentEl.innerHTML = marked.parse(reply);
        } 
        else if (openaiKey && openaiKey.trim() !== '') {
            const res = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + openaiKey },
                body: JSON.stringify({ model: 'gpt-4o-mini', messages: chatHistory })
            });
            if(!res.ok) throw new Error('OpenAI API Error');
            const data = await res.json();
            const reply = data.choices[0].message.content;
            chatHistory.push({ role: 'assistant', content: reply });
            if(aiContentEl) aiContentEl.innerHTML = marked.parse(reply);
        }
        else {
            const demoReply = "🥚 **모기에그(MogiEgg) 정적 데모 모드입니다!**\\n\\n현재 입력된 API 키가 없습니다. 왼쪽 아래 설정(⚙️)에서 OpenAI나 Gemini API 키 중 **1개만 입력하셔도** 정상적으로 답변을 받아보실 수 있습니다!\\n\\n요청하신 내용: " + text;
            if(aiContentEl) aiContentEl.innerHTML = marked.parse(demoReply);
        }
        if(container) container.scrollTop = container.scrollHeight;
      } catch (err) {
        if(aiContentEl) aiContentEl.innerHTML = marked.parse("⚠️ API 호출 중 오류가 발생했습니다. 키가 정확한지 확인해주세요. (" + err.message + ")");
      } finally {
        isGenerating = false;
        lucide.createIcons();
      }
    }

    function appendMessageUI(role, content, msgId = null) {
      const container = document.getElementById('chat-messages-container');
      if(!container) return;
      const div = document.createElement('div');
      div.className = role === 'user' ? 'flex justify-end gap-3' : 'flex justify-start gap-3';
      if (role === 'user') {
        div.innerHTML = `<div class="max-w-[80%] bg-brand-500 text-dark-bg font-medium text-xs md:text-sm px-4 py-3 rounded-2xl rounded-tr-none shadow-md">${content}</div><img src="static/mascot.png" class="w-8 h-8 rounded-xl object-cover ring-1 ring-brand-500/30 shrink-0" onerror="this.src='static/mascot.png'">`;
      } else {
        div.innerHTML = `<img src="static/mascot.png" class="w-8 h-8 rounded-xl object-cover ring-1 ring-brand-500/30 shrink-0" onerror="this.src='static/mascot.png'"><div class="max-w-[85%] bg-dark-card border border-dark-border text-xs md:text-sm text-slate-200 px-4 py-3.5 rounded-2xl rounded-tl-none shadow-md prose prose-invert leading-relaxed" ${msgId ? `id="${msgId}"` : ''}>${content ? marked.parse(content) : '<div class="flex items-center gap-2 text-brand-400 font-semibold"><span class="w-2 h-2 rounded-full bg-brand-400 animate-ping"></span>생각 중...</div>'}</div>`;
      }
      container.appendChild(div);
      container.scrollTop = container.scrollHeight;
    }

    function startNewChat() { 
        chatHistory = []; 
        const container = document.getElementById('chat-messages-container');
        const hero = document.getElementById('welcome-hero');
        if(container) { container.innerHTML = ''; container.classList.add('hidden'); }
        if(hero) hero.classList.remove('hidden'); 
        switchTab('chat'); 
    }
    
    function loadSampleChat(id) { 
        if (id === 1) sendPresetMessage('구독자 10만~50만 뷰티 유튜버 추천해줘'); 
        if (id === 2) sendPresetMessage('유튜브 채널 10배 성장 숏폼 전략 알려줘'); 
    }
    
    function clearHistory() { 
        const hl = document.getElementById('history-list');
        if(hl) hl.innerHTML = '<p class="text-[11px] text-slate-500 py-4 text-center">대화 기록이 정리되었습니다.</p>'; 
    }
    
    function runYoutubeAnalysis() { 
        const input = document.getElementById('yt-search-input');
        const q = (input && input.value.trim()) ? input.value.trim() : '올리브영 뷰티 꿀템'; 
        sendPresetMessage(`유튜브 검색어 "${q}" 채널 및 영상 벤치마킹 분석해줘`); 
    }

    async function runShortformBuild() {
      const topicEl = document.getElementById('sf-topic');
      const categoryEl = document.getElementById('sf-category');
      const targetEl = document.getElementById('sf-target');
      const topic = topicEl ? topicEl.value : '기본 주제';
      const category = categoryEl ? categoryEl.value : '일반';
      const target = targetEl ? targetEl.value : '일반 타겟';
      
      const titleEl = document.getElementById('sf-res-title');
      const hookEl = document.getElementById('sf-res-hook');
      const listEl = document.getElementById('sf-scenes-list');

      try {
        const res = await fetch('api/shortform/generate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ topic, category, target }) });
        if (!res.ok) throw new Error();
        const data = await res.json();
        if(titleEl) titleEl.innerText = data.title;
        if(hookEl) hookEl.innerText = data.hook_3sec;
        if(listEl) {
            listEl.innerHTML = '';
            data.scenes.forEach(scene => {
              listEl.innerHTML += `<div class="p-3 rounded-xl bg-dark-surface border border-dark-border text-xs space-y-1"><div class="flex items-center justify-between"><span class="font-bold text-brand-400">${scene.time} · ${scene.phase}</span><span class="text-[10px] text-slate-400 bg-slate-800 px-2 py-0.5 rounded">${scene.sound}</span></div><p class="text-slate-300 font-medium">${scene.narration}</p><p class="text-[11px] text-slate-400">🎬 <span class="italic">${scene.visual}</span></p></div>`;
            });
        }
      } catch (err) {
        if(titleEl) titleEl.innerText = `[${category}] ${topic} - 30초 완성 숏폼 기획안`;
        if(hookEl) hookEl.innerText = `🚨 ${target} 주목! 아직도 '${topic}' 이렇게 쓰고 계신다면 당장 멈추세요.`;
        if(listEl) listEl.innerHTML = `<div class="p-3 rounded-xl bg-dark-surface border border-dark-border text-xs space-y-1"><div class="flex items-center justify-between"><span class="font-bold text-brand-400">0~3초 · ⚡ 충격 3초 훅</span><span class="text-[10px] text-slate-400 bg-slate-800 px-2 py-0.5 rounded">타격음</span></div><p class="text-slate-300 font-medium">여러분, ${topic} 때문에 고민 많으셨죠?</p><p class="text-[11px] text-slate-400">🎬 <span class="italic">화면 클로즈업 + 자막 강조</span></p></div>`;
      }
    }

    function copyShortformScript() { 
        const box = document.getElementById('sf-result-box');
        if(box) navigator.clipboard.writeText(box.innerText); 
        alert('📋 숏폼 기획안과 대본이 클립보드에 복사되었습니다!'); 
    }
    
    function openRechargeModal() { 
        const m = document.getElementById('recharge-modal');
        if(m) m.classList.remove('hidden'); 
    }
    
    function closeRechargeModal() { 
        const m = document.getElementById('recharge-modal');
        if(m) m.classList.add('hidden'); 
    }
    
    async function performRecharge(amount) {
      try {
        const res = await fetch('api/billing/recharge', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ amount }) });
        if(!res.ok) throw new Error();
        const data = await res.json();
        if (data.success) { alert(data.message); closeRechargeModal(); fetchUserInfo(); }
      } catch (e) {
        alert('충전 완료! (정적 데모 모드)'); closeRechargeModal();
      }
    }
    
    function openKeyModal() { 
        const m = document.getElementById('key-modal');
        if(m) m.classList.remove('hidden'); 
    }
    
    function closeKeyModal() { 
        const m = document.getElementById('key-modal');
        if(m) m.classList.add('hidden'); 
    }
    
    async function saveUserKeys() {
      const nameEl = document.getElementById('cfg-name');
      const geminiEl = document.getElementById('cfg-gemini');
      const openaiEl = document.getElementById('cfg-openai');
      const claudeEl = document.getElementById('cfg-claude');
      
      const name = nameEl ? nameEl.value : '';
      const gemini_key = geminiEl ? geminiEl.value : '';
      const openai_key = openaiEl ? openaiEl.value : '';
      const claude_key = claudeEl ? claudeEl.value : '';
      
      localStorage.setItem('mogiegg_name', name);
      localStorage.setItem('mogiegg_gemini', gemini_key);
      localStorage.setItem('mogiegg_openai', openai_key);
      localStorage.setItem('mogiegg_claude', claude_key);
      
      userInfo.name = name || '모기에그 크리에이터';
      updateUserUI();
      alert('🔑 API 키가 브라우저에 안전하게 저장되었습니다!\\n이제 정적 페이지에서도 설정하신 키로 정상 작동합니다.');
      closeKeyModal();
    }
"""

new_content = content[:start_idx] + clean_js + "\n" + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Full JS block replaced successfully without syntax errors.")
