import os, requests

TOKEN=os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID=os.environ['TELEGRAM_CHAT_ID']
text=os.environ.get('ALERT_TEXT','Test alert')
url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
r=requests.post(url, data={'chat_id':CHAT_ID, 'text':text})
r.raise_for_status()
print(r.text)
