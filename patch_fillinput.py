import os

file_path = 'templates/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 추천 질문 버튼의 함수를 sendPresetMessage에서 fillInputBox로 변경
content = content.replace("sendPresetMessage('구독자 10만~50만", "fillInputBox('구독자 10만~50만")
content = content.replace("sendPresetMessage('유튜브 채널 10배", "fillInputBox('유튜브 채널 10배")
content = content.replace("sendPresetMessage('이번 주 유튜브 핫비디오", "fillInputBox('이번 주 유튜브 핫비디오")
content = content.replace("sendPresetMessage('마케팅 및 콘텐츠 자동화", "fillInputBox('마케팅 및 콘텐츠 자동화")

# 80+ 스킬 라이브러리도 마찬가지로 적용 (통일성 확보)
content = content.replace("sendPresetMessage('3초 안에 스크롤", "fillInputBox('3초 안에 스크롤")
content = content.replace("sendPresetMessage('올리브영 베스트 상품 리뷰를", "fillInputBox('올리브영 베스트 상품 리뷰를")
content = content.replace("sendPresetMessage('인스타그램 릴스 & 유튜브 쇼츠", "fillInputBox('인스타그램 릴스 & 유튜브 쇼츠")
content = content.replace("sendPresetMessage('유튜브 썸네일에 들어갈", "fillInputBox('유튜브 썸네일에 들어갈")
content = content.replace("sendPresetMessage('경쟁사 제품과 비교하는", "fillInputBox('경쟁사 제품과 비교하는")
content = content.replace("sendPresetMessage('콘텐츠 하나로 쇼츠", "fillInputBox('콘텐츠 하나로 쇼츠")

# 사이드바 최근 기록 (샘플 버튼)은 바로 실행되게 두거나 변경 (여기서는 fillInputBox로 통일)
content = content.replace("sendPresetMessage('구독자 10만~50만 뷰티 유튜버 추천해줘')", "fillInputBox('구독자 10만~50만 뷰티 유튜버 추천해줘')")
content = content.replace("sendPresetMessage('유튜브 채널 10배 성장 숏폼 전략 알려줘')", "fillInputBox('유튜브 채널 10배 성장 숏폼 전략 알려줘')")

# JS 함수 추가
old_js = """    function sendPresetMessage(text) {
      switchTab('chat');
      processUserMessage(text);
    }"""
new_js = """    function sendPresetMessage(text) {
      switchTab('chat');
      processUserMessage(text);
    }
    
    function fillInputBox(text) {
      switchTab('chat');
      const input = document.getElementById('chat-input');
      if(input) {
          input.value = text;
          input.focus();
      }
    }"""
content = content.replace(old_js, new_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Applied fillInputBox patch.')
