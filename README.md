# hr_test

[العربية](#العربية) | [English](#english)

## العربية

### نبذة

`hr_test` هو نموذج أولي صغير مكتوب بلغة Python، يستقبل تحديثات Webhook الخاصة ببوت Telegram عبر HTTP، ثم يحاول إرسال رد بسيط بحسب الرابط الموجود في الرسالة.

### ما الذي يفعله؟

- يشغّل خادم HTTP على المنفذ `8443`.
- يستقبل تحديثات Telegram بصيغة JSON عبر طلبات `POST`.
- يقرأ نص الرسالة ومعرّف المحادثة.
- يتعرّف على روابط YouTube وTikTok وInstagram وFacebook.
- يعالج كل تحديث في خيط تنفيذ منفصل.
- يرسل الرد عبر واجهة Telegram Bot API.

### الحالة الحالية

المشروع إثبات مفهوم، وليس أداة تنزيل مكتملة أو بوتاً جاهزاً للاستخدام الإنتاجي. معالجات المنصات الأربع تعيد حالياً نصوصاً تجريبية فقط؛ فهي لا تنزّل الوسائط ولا تنشئ روابط تنزيل حقيقية.

لا يتضمن المستودع إعداد Webhook أو إنهاء اتصال HTTPS أو التحقق من الطلبات أو الاختبارات الآلية أو معالجة أخطاء مناسبة للإنتاج. كما أن معاملات طلب Telegram تُدرج مباشرة في الرابط من دون ترميز آمن.

### التقنيات

- Python 3.
- مكتبة Python القياسية فقط: `http.server` و`urllib.request` و`json` و`threading`.
- Telegram Bot API.

لا يحتاج المشروع إلى حزم Python خارجية.

### هيكل المشروع

```text
.
├── main.py      # خادم HTTP وتوجيه التحديثات وإرسال ردود Telegram
└── README.md
```

### التشغيل محلياً

1. تأكد من تثبيت Python 3:

   ```bash
   python --version
   ```

2. افتح `main.py` واضبط قيمة `TELEGRAM_TOKEN`.

   يحتوي المصدر حالياً على قيمة مؤقتة، ولا يقرأ الرمز من متغير بيئة. لا تضف رمزاً حقيقياً إلى Git؛ وعند النشر العام أو المشترك، عدّل التطبيق ليقرأه من متغير بيئة آمن أو مدير أسرار.

3. شغّل الخادم:

   ```bash
   python main.py
   ```

4. يستمع الخادم على العنوان:

   ```text
   http://0.0.0.0:8443
   ```

لاستقبال تحديثات Telegram الفعلية، يجب توجيه نقطة وصول HTTPS عامة إلى هذا الخادم وتسجيلها بوصفها Webhook للبوت. إعداد TLS وتسجيل Webhook غير موجودين في هذا المستودع.

### سلوك الرسائل

| محتوى الرسالة | سلوك الرد الحالي |
| --- | --- |
| `youtube.com` أو `youtu.be` | يعيد نص رابط تجريبي لـ YouTube |
| `tiktok.com` | يعيد نص رابط تجريبي لـ TikTok |
| `instagram.com` | يعيد نص رابط تجريبي لـ Instagram |
| `facebook.com` | يعيد نص رابط تجريبي لـ Facebook |
| أي محتوى آخر | يعيد رسالة تفيد بأن الرابط أو الأمر غير مدعوم |

### قبل الاستخدام الإنتاجي

- تنفيذ المعالجات الفعلية الخاصة بكل منصة.
- تحميل رمز البوت بصورة آمنة بدلاً من تخزينه في المصدر.
- إضافة HTTPS وتسجيل Webhook والتحقق من المدخلات والمهل الزمنية ومعالجة الأخطاء.
- ترميز معاملات Telegram API بصورة آمنة.
- إضافة السجلات والاختبارات واستخدام خادم مناسب للإنتاج.

## English

### Overview

`hr_test` is a small Python prototype that receives Telegram Bot webhook updates over HTTP and attempts to send a simple reply based on the link found in each message.

### What it does

- Starts an HTTP server on port `8443`.
- Accepts Telegram-style JSON updates through `POST` requests.
- Reads the message text and chat ID.
- Recognizes links from YouTube, TikTok, Instagram, and Facebook.
- Processes each update in a separate thread.
- Sends replies through the Telegram Bot API.

### Current status

The project is a proof of concept, not a finished downloader or a production-ready bot. The four platform handlers currently return placeholder text only; they do not download media or create real download links.

The repository does not include webhook registration, HTTPS termination, request validation, automated tests, or production-grade error handling. Telegram request parameters are also inserted directly into the URL without safe encoding.

### Technology

- Python 3.
- Python standard library only: `http.server`, `urllib.request`, `json`, and `threading`.
- Telegram Bot API.

No third-party Python packages are required.

### Project structure

```text
.
├── main.py      # HTTP server, update routing, and Telegram replies
└── README.md
```

### Run locally

1. Make sure Python 3 is installed:

   ```bash
   python --version
   ```

2. Open `main.py` and configure `TELEGRAM_TOKEN`.

   The source currently contains a placeholder and does not read the token from an environment variable. Do not commit a real token. For shared or public deployments, update the application to read it from a secure environment variable or secret manager.

3. Start the server:

   ```bash
   python main.py
   ```

4. The server listens on:

   ```text
   http://0.0.0.0:8443
   ```

To receive real Telegram updates, route a public HTTPS endpoint to this server and register that endpoint as the bot webhook. TLS and webhook setup are not included in this repository.

### Message behavior

| Message contains | Current reply behavior |
| --- | --- |
| `youtube.com` or `youtu.be` | Returns YouTube placeholder-link text |
| `tiktok.com` | Returns TikTok placeholder-link text |
| `instagram.com` | Returns Instagram placeholder-link text |
| `facebook.com` | Returns Facebook placeholder-link text |
| Anything else | Returns an unsupported-link-or-command message |

### Before production use

- Implement the platform-specific handlers.
- Load the bot token securely instead of storing it in source code.
- Add HTTPS, webhook registration, input validation, timeouts, and error handling.
- Encode Telegram API parameters safely.
- Add logging, tests, and a production server strategy.
