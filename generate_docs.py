import os
from pathlib import Path

# Тексты на английском
en_terms = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Terms of Use — MoneyApp</title>
<style>
  :root { --bg: #0B0F14; --card: #141416; --text: #FFFFFF; --muted: #9CA3AF; --accent: #B02222; --border: #2A2A2E; }
  * { box-sizing: border-box; }
  body { margin: 0; padding: 0; background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.65; }
  .wrap { max-width: 760px; margin: 0 auto; padding: 48px 20px 80px; }
  h1 { font-size: 30px; margin: 0 0 6px; letter-spacing: -0.5px; }
  .date { color: var(--muted); font-size: 14px; margin-bottom: 36px; }
  h2 { font-size: 19px; margin: 34px 0 12px; padding-top: 22px; border-top: 1px solid var(--border); }
  h2:first-of-type { border-top: none; padding-top: 0; }
  p { margin: 0 0 14px; } ul { margin: 0 0 14px; padding-left: 22px; } li { margin-bottom: 8px; } a { color: var(--accent); }
  .warn { background: var(--card); border-left: 3px solid var(--accent); border-radius: 0 14px 14px 0; padding: 18px 20px; margin: 22px 0; }
  .warn h3 { margin: 0 0 10px; font-size: 16px; } .warn p { margin: 0; color: var(--muted); font-size: 15px; }
  strong { color: var(--text); } footer { margin-top: 50px; padding-top: 22px; border-top: 1px solid var(--border); color: var(--muted); font-size: 14px; }
</style>
</head>
<body>
<div class="wrap">
<h1>Terms of Use</h1>
<div class="date">Effective date: September 18, 2026</div>
<div class="warn">
  <h3>Beta Version</h3>
  <p>MoneyApp is in early testing. Glitches, data loss, and calculation errors may occur. Do not use the app as your sole accounting source — keep a backup of important records.</p>
</div>
<h2>1. Acceptance of Terms</h2>
<p>By installing and using MoneyApp, you agree to these Terms. If you disagree with any part, stop using the app and delete your account.</p>
<h2>2. How the Service Works</h2>
<p>The app is provided "AS IS". Data syncs with a private developer server. An internet connection is required to save operations.</p>
<p>The developer does not guarantee uninterrupted server operation, data integrity, or service availability at all times.</p>
<h2>3. Receipt Recognition</h2>
<p>Cloud services (Google Gemini and backup models via OpenRouter) are used to parse receipts. Recognition accuracy is not guaranteed: the model may make errors in amounts, dates, or items.</p>
<p><strong>Verify parsed data before saving.</strong> You are responsible for the correctness of entered amounts.</p>
<h2>4. Your Responsibility</h2>
<ul>
  <li>you are responsible for keeping your password and recovery code safe;</li>
  <li>you verify data accuracy before saving;</li>
  <li>you do not use the app for illegal activities;</li>
  <li>you understand receipt images are sent to third-party AI services.</li>
</ul>
<h2>5. Limitation of Liability</h2>
<p>The developer is not liable for financial losses, incorrect analytics, data loss, or decisions made based on app data.</p>
<h2>6. Termination</h2>
<p>You can delete your account and all data at any time via the "Account" section.</p>
<h2>7. Changes to Terms</h2>
<p>Terms may change. The new edition takes effect upon publication on this page.</p>
<h2>Contact</h2>
<p>Support: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>See also <a href="privacy.html">Privacy Policy</a>.</footer>
</div>
</body>
</html>"""

en_privacy = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Privacy Policy — MoneyApp</title>
<style>
  :root { --bg: #0B0F14; --card: #141416; --text: #FFFFFF; --muted: #9CA3AF; --accent: #B02222; --border: #2A2A2E; }
  * { box-sizing: border-box; }
  body { margin: 0; padding: 0; background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.65; }
  .wrap { max-width: 760px; margin: 0 auto; padding: 48px 20px 80px; }
  h1 { font-size: 30px; margin: 0 0 6px; letter-spacing: -0.5px; }
  .date { color: var(--muted); font-size: 14px; margin-bottom: 36px; }
  h2 { font-size: 19px; margin: 34px 0 12px; padding-top: 22px; border-top: 1px solid var(--border); }
  h2:first-of-type { border-top: none; padding-top: 0; }
  p { margin: 0 0 14px; } ul { margin: 0 0 14px; padding-left: 22px; } li { margin-bottom: 8px; } a { color: var(--accent); }
  .note { background: var(--card); border-radius: 14px; padding: 16px 18px; margin: 18px 0; font-size: 15px; color: var(--muted); }
  strong { color: var(--text); } footer { margin-top: 50px; padding-top: 22px; border-top: 1px solid var(--border); color: var(--muted); font-size: 14px; }
</style>
</head>
<body>
<div class="wrap">
<h1>Privacy Policy</h1>
<div class="date">Effective date: September 18, 2026</div>
<p>MoneyApp respects your privacy. Below is what data is collected and how it is handled.</p>
<h2>1. Where Data is Stored</h2>
<p>MoneyApp runs on a private developer server (self-hosted model). No cloud providers are involved.</p>
<p><strong>What is stored:</strong></p>
<ul>
  <li>financial operations: amounts, dates, descriptions, accounts, and categories;</li>
  <li>scanned receipt photos and recognized items;</li>
  <li>uploaded bank statements;</li>
  <li>settings: currency, language, budget limits, templates, shopping lists;</li>
  <li>username and password hash;</li>
  <li>email address (if provided for recovery).</li>
</ul>
<h2>2. Receipt Recognition & Third-Party AI</h2>
<p>Receipt images are sent to cloud recognition services: <strong>Google Gemini</strong> or backup models via <strong>OpenRouter</strong>.</p>
<div class="note">If you prefer not to share images with third-party services, enter transactions manually.</div>
<h2>3. Error Reporting</h2>
<p>Sentry is used to collect crash reports without personal data, amounts, or receipt photos.</p>
<h2>4. Email</h2>
<p>Password recovery emails are sent via <strong>Brevo</strong>.</p>
<h2>5. Data Retention & Your Rights</h2>
<p>Data is stored while you use the app. You can delete your account completely via the "Account" section at any time.</p>
<h2>Contact</h2>
<p>Data requests: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>MoneyApp — Personal Finance Tracker. Beta version.</footer>
</div>
</body>
</html>"""

# Сохраняем корневые (русские)
Path('terms.html').write_text(..., encoding='utf-8') # уже созданы пользователем

# Создаем папку pages_p и записываем локализации (пример для EN, для остальных языков аналогично)
os.makedirs('pages_p', exist_ok=True)
Path('pages_p/terms_en.html').write_text(en_terms, encoding='utf-8')
Path('pages_p/privacy_en.html').write_text(en_privacy, encoding='utf-8')

print("Документы подготовлены!")
