import os

file_path = 'templates/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

js_init = """    document.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      
      if(localStorage.getItem('mogiegg_name')) {
          userInfo.name = localStorage.getItem('mogiegg_name');
          document.getElementById('cfg-name').value = userInfo.name;
      }
      if(localStorage.getItem('mogiegg_gemini')) document.getElementById('cfg-gemini').value = localStorage.getItem('mogiegg_gemini');
      if(localStorage.getItem('mogiegg_openai')) document.getElementById('cfg-openai').value = localStorage.getItem('mogiegg_openai');
      if(localStorage.getItem('mogiegg_claude')) document.getElementById('cfg-claude').value = localStorage.getItem('mogiegg_claude');

      fetchUserInfo();
      setupSidebar();
    });"""

start_init = content.find("document.addEventListener('DOMContentLoaded', () => {")
end_init = content.find("setupSidebar();\n    });") + len("setupSidebar();\n    });")
content = content[:start_init] + js_init + content[end_init:]


js_save = """    async function saveUserKeys() {
      const name = document.getElementById('cfg-name').value;
      const gemini_key = document.getElementById('cfg-gemini').value;
      const openai_key = document.getElementById('cfg-openai').value;
      const claude_key = document.getElementById('cfg-claude').value;
      
      localStorage.setItem('mogiegg_name', name);
      localStorage.setItem('mogiegg_gemini', gemini_key);
      localStorage.setItem('mogiegg_openai', openai_key);
      localStorage.setItem('mogiegg_claude', claude_key);
      
      userInfo.name = name || '모기에그 크리에이터';
      updateUserUI();
      alert('🔑 API 키가 브라우저에 안전하게 저장되었습니다! 이제 정적 페이지에서도 1개의 키만 있으면 정상 작동합니다.');
      closeKeyModal();
    }"""

start_save = content.find("async function saveUserKeys() {")
end_save = content.find("}", start_save) + 1
content = content[:start_save] + js_save + content[end_save:]


js_chat = """    async function processUserMessage(text) {
      const hero = document.getElementById('welcome-hero');
      const container = document.getElementById('chat-messages-container');
      hero.classList.add('hidden');
      container.classList.remove('hidden');
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
            aiContentEl.innerHTML = marked.parse(reply);
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
            aiContentEl.innerHTML = marked.parse(reply);
        }
        else {
            const demoReply = "🥚 **모기에그(MogiEgg) 정적 데모 모드입니다!**\\n\\n현재 입력된 API 키가 없습니다. 왼쪽 아래 설정(⚙️)에서 OpenAI나 Gemini API 키 중 **1개만 입력하셔도** 정상적으로 답변을 받아보실 수 있습니다!\\n\\n요청하신 내용: " + text;
            aiContentEl.innerHTML = marked.parse(demoReply);
        }
        container.scrollTop = container.scrollHeight;
      } catch (err) {
        aiContentEl.innerHTML = marked.parse("⚠️ API 호출 중 오류가 발생했습니다. 키가 정확한지 확인해주세요. (" + err.message + ")");
      } finally {
        isGenerating = false;
        lucide.createIcons();
      }
    }"""

start_chat = content.find("async function processUserMessage(text) {")
end_chat = content.find("function appendMessageUI", start_chat)
content = content[:start_chat] + js_chat + "\n\n    " + content[end_chat:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Client-side direct API logic applied successfully.")
