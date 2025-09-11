import urllib.request
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
WEBHOOK_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data)
        threading.Thread(target=self.handle_update, args=(update,)).start()
        self.send_response(200)
        self.end_headers()

    def handle_update(self, update):
        chat_id = update.get('message', {}).get('chat', {}).get('id')
        text = update.get('message', {}).get('text', '')
        response = self.process_message(text)
        self.send_message(chat_id, response)

    def process_message(self, text):
        if "youtube.com" in text or "youtu.be" in text:
            return self.handle_youtube_link(text)
        elif "tiktok.com" in text:
            return self.handle_tiktok_link(text)
        elif "instagram.com" in text:
            return self.handle_instagram_link(text)
        elif "facebook.com" in text:
            return self.handle_facebook_link(text)
        return "Unsupported link or command."

    def handle_youtube_link(self, text):
        # Add logic to handle YouTube link
        return "YouTube download link: [Link]"

    def handle_tiktok_link(self, text):
        # Add logic to handle TikTok link
        return "TikTok download link: [Link]"

    def handle_instagram_link(self, text):
        # Add logic to handle Instagram link
        return "Instagram download link: [Link]"

    def handle_facebook_link(self, text):
        # Add logic to handle Facebook link
        return "Facebook download link: [Link]"

    def send_message(self, chat_id, text):
        url = f"{WEBHOOK_URL}sendMessage?chat_id={chat_id}&text={text}"
        urllib.request.urlopen(url)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8443):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()