import os

file_path = 'templates/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 채팅 시스템 프롬프트 추가 (Gemini & OpenAI)
old_chat_js = """        if (geminiKey && geminiKey.trim() !== '') {
            const gHistory = chatHistory.map(m => ({
                role: m.role === 'user' ? 'user' : 'model',
                parts: [{ text: m.content }]
            }));
            const res = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=' + geminiKey, {"""

new_chat_js = """        const systemPrompt = "당신은 유튜브 마케팅 및 숏폼 콘텐츠 기획 전문가 '모기에그(MogiEgg)'입니다. 사용자의 유튜브 채널 성장을 돕고, 3초 안에 시선을 끄는 훅(Hook)과 숏폼 대본을 작성해줍니다. 무조건 친절하고 마케팅 전문가다운 어조로 대답하세요.";
        
        if (geminiKey && geminiKey.trim() !== '') {
            const gHistory = chatHistory.map(m => ({
                role: m.role === 'user' ? 'user' : 'model',
                parts: [{ text: m.content }]
            }));
            const res = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=' + geminiKey, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    system_instruction: { parts: [{ text: systemPrompt }] },
                    contents: gHistory 
                })
            });
            if(!res.ok) throw new Error('Gemini API Error');"""
            
content = content.replace(old_chat_js, new_chat_js)
content = content.replace("body: JSON.stringify({ contents: gHistory })", "") # Clean up the leftover old body string if it exists.


old_openai_js = """        else if (openaiKey && openaiKey.trim() !== '') {
            const res = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + openaiKey },
                body: JSON.stringify({ model: 'gpt-4o-mini', messages: chatHistory })
            });"""

new_openai_js = """        else if (openaiKey && openaiKey.trim() !== '') {
            const messagesWithSystem = [{ role: 'system', content: systemPrompt }, ...chatHistory];
            const res = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + openaiKey },
                body: JSON.stringify({ model: 'gpt-4o-mini', messages: messagesWithSystem })
            });"""
content = content.replace(old_openai_js, new_openai_js)

# 2. 숏폼 생성 기능 클라이언트 직접 호출로 변경
old_sf_js = """      try {
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
        if(titleEl) titleEl.innerText = `[${category}] ${topic} - 30초 완성 숏폼 기획안`;"""

new_sf_js = """      const geminiKey = localStorage.getItem('mogiegg_gemini');
      const openaiKey = localStorage.getItem('mogiegg_openai');
      const prompt = `카테고리: ${category}\\n타겟: ${target}\\n주제: ${topic}\\n이 내용을 바탕으로 30초짜리 숏폼 대본을 만들어줘. 결과는 반드시 순수한 JSON 형식으로만 줘. (마크다운 백틱 없이) 형식: {"title": "제목", "hook_3sec": "3초 훅 대사", "scenes": [{"time": "0~3초", "phase": "도입부", "sound": "효과음", "narration": "대사", "visual": "화면 연출"}]}`;
      
      try {
        let aiText = '';
        if (geminiKey && geminiKey.trim() !== '') {
            const res = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=' + geminiKey, {
                method: 'POST', headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ contents: [{role: 'user', parts: [{text: prompt}]}] })
            });
            const data = await res.json();
            aiText = data.candidates[0].content.parts[0].text;
        } else if (openaiKey && openaiKey.trim() !== '') {
            const res = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST', headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + openaiKey },
                body: JSON.stringify({ model: 'gpt-4o-mini', messages: [{role: 'user', content: prompt}] })
            });
            const data = await res.json();
            aiText = data.choices[0].message.content;
        } else {
            throw new Error('API 키가 없습니다.');
        }
        
        let parsed;
        try {
            const jsonMatch = aiText.match(/\\{.*\\}/s);
            parsed = JSON.parse(jsonMatch ? jsonMatch[0] : aiText);
        } catch(e) {
            parsed = JSON.parse(aiText.replace(/```json/g, '').replace(/```/g, '').trim());
        }
        
        if(titleEl) titleEl.innerText = parsed.title || `[${category}] ${topic}`;
        if(hookEl) hookEl.innerText = parsed.hook_3sec || '훅 대사';
        if(listEl) {
            listEl.innerHTML = '';
            (parsed.scenes || []).forEach(scene => {
              listEl.innerHTML += `<div class="p-3 rounded-xl bg-dark-surface border border-dark-border text-xs space-y-1"><div class="flex items-center justify-between"><span class="font-bold text-brand-400">${scene.time} · ${scene.phase}</span><span class="text-[10px] text-slate-400 bg-slate-800 px-2 py-0.5 rounded">${scene.sound}</span></div><p class="text-slate-300 font-medium">${scene.narration}</p><p class="text-[11px] text-slate-400">🎬 <span class="italic">${scene.visual}</span></p></div>`;
            });
        }
      } catch (err) {
        if(titleEl) titleEl.innerText = `[${category}] ${topic} - 30초 완성 숏폼 기획안 (데모 모드)`;"""
content = content.replace(old_sf_js, new_sf_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('System prompt and dynamic shortform generation applied.')
