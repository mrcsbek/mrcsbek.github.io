import os
from pathlib import Path

# Переводы Terms of Use по языкам
terms_translations = {
    "en": """<!DOCTYPE html>
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
<p>The app is provided "AS IS". Data synchronizes with a private developer server. An internet connection is required to save operations — without it, entered data may not reach the server.</p>
<p>The developer does not guarantee uninterrupted server operation, data integrity, or service availability at any time.</p>
<h2>3. Receipt Recognition</h2>
<p>Cloud services (Google Gemini and backup models via OpenRouter) are used to parse receipts. Recognition accuracy is not guaranteed: the model may make errors in amounts, dates, store names, or items.</p>
<p><strong>Verify parsed data before saving.</strong> You are responsible for the correctness of entered amounts.</p>
<h2>4. Your Responsibility</h2>
<ul>
  <li>you are responsible for keeping your password and recovery code safe;</li>
  <li>you verify data accuracy before saving;</li>
  <li>you do not use the app for illegal activities;</li>
  <li>you understand receipt images are sent to third-party AI services.</li>
</ul>
<h2>5. Limitation of Liability</h2>
<p>The developer is not liable for:</p>
<ul>
  <li>financial losses of any kind;</li>
  <li>incorrect analytics, inaccurate amounts, and erroneous categories;</li>
  <li>data loss, database damage, or server failures;</li>
  <li>decisions made based on app data.</li>
</ul>
<p>MoneyApp is a personal tracking tool, not an accounting system and not a professional financial advisor.</p>
<h2>6. Termination</h2>
<p>You can delete your account and all data at any time via the "Account" section. The developer reserves the right to suspend access upon service abuse.</p>
<h2>7. Changes to Terms</h2>
<p>Terms may change. The new edition takes effect upon publication on this page. By continuing to use the app, you accept the updated terms.</p>
<h2>Feedback</h2>
<p>Questions and technical support: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>See also <a href="privacy.html">Privacy Policy</a>.</footer>
</div>
</body>
</html>""",

    "tr": """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kullanım Şartları — MoneyApp</title>
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
<h1>Kullanım Şartları</h1>
<div class="date">Yürürlük tarihi: 18 Eylül 2026</div>
<div class="warn">
  <h3>Beta Sürümü</h3>
  <p>MoneyApp erken test aşamasındadır. Hatalar, veri kaybı ve hesaplama yanlışlıkları oluşabilir. Uygulamayı tek muhasebe kaynağı olarak kullanmayın — önemli kayıtların yedeğini saklayın.</p>
</div>
<h2>1. Şartların Kabulü</h2>
<p>MoneyApp'i yükleyerek ve kullanarak bu Şartları kabul etmiş olursunuz. Herhangi bir noktayı kabul etmiyorsanız, uygulamayı kullanmayı bırakın ve hesabınızı silin.</p>
<h2>2. Servis Nasıl Çalışır</h2>
<p>Uygulama "olduğu gibi" (AS IS) sağlanmaktadır. Veriler geliştiricinin özel sunucusuyla senkronize edilir. İşlemleri kaydetmek için internet bağlantısı gereklidir — bağlantı olmadan girilen veriler sunucuya ulaşmayabilir.</p>
<p>Geliştirici, kesintisiz sunucu çalışmasını, veri bütünlüğünü veya her an hizmet kullanılabilirliğini garanti etmez.</p>
<h2>3. Fiş Tanıma</h2>
<p>Fişleri ayrıştırmak için bulut servisleri (Google Gemini ve OpenRouter üzerinden yedek modeller) kullanılır. Tanıma doğruluğu garanti edilmez: model tutar, tarih, mağaza adı veya kalemlerde hata yapabilir.</p>
<p><strong>Kaydetmeden önce tanınan verileri kontrol edin.</strong> Girilen tutarların doğruluğunun sorumluluğu kullanıcıya aittir.</p>
<h2>4. Sorumluluğunuz</h2>
<ul>
  <li>şifrenizi ve kurtarma kodunuzu güvenli tutmaktan siz sorumlusunuz;</li>
  <li>kaydetmeden önce veri doğruluğunu kontrol edersiniz;</li>
  <li>uygulamayı yasadışı faaliyetler için kullanmazsınız;</li>
  <li>fiş görsellerinin üçüncü taraf yapay zeka servislerine gönderildiğini anlarsınız.</li>
</ul>
<h2>5. Sorumluluğun Sınırlandırılması</h2>
<p>Geliştirici aşağıdakilerden sorumlu tutulamaz:</p>
<ul>
  <li>her türlü finansal zarar;</li>
  <li>yanlış analitik, hatalı tutarlar ve yanlış kategoriler;</li>
  <li>veri kaybı, veritabanı hasarı veya sunucu arızaları;</li>
  <li>uygulama verilerine dayanarak alınan kararlar.</li>
</ul>
<p>MoneyApp bir muhasebe sistemi veya profesyonel finansal danışman değil, kişisel takip aracıdır.</p>
<h2>6. Kullanımın Sonlandırılması</h2>
<p>Hesabınızı ve tüm verilerinizi "Hesap" bölümündeki düğme ile istediğiniz zaman silebilirsiniz. Geliştirici, hizmetin kötüye kullanımı durumunda erişimi askıya alma hakkını saklı tutar.</p>
<h2>7. Şartlardaki Değişiklikler</h2>
<p>Şartlar değişebilir. Yeni sürüm, bu sayfada yayınlandığı anda yürürlüğe girer. Uygulamayı kullanmaya devam ederek güncellenmiş şartları kabul etmiş olursunuz.</p>
<h2>Geri Bildirim</h2>
<p>Sorular ve teknik destek: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>Ayrıca bkz. <a href="privacy.html">Gizlilik Politikası</a>.</footer>
</div>
</body>
</html>""",

    "uz": """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Foydalanish shartlari — MoneyApp</title>
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
<h1>Foydalanish shartlari</h1>
<div class="date">Kuchga kirish sanasi: 2026-yil 18-sentyabr</div>
<div class="warn">
  <h3>Beta-versiya</h3>
  <p>MoneyApp dastlabki sinov bosqichida. Nosozliklar, ma'lumotlarni yo'qotish va hisob-kitoblardagi xatolar bo'lishi mumkin. Ilovani yagona hisob manbai sifatida ishlatmang — muhim yozuvlarning zaxira nusxasini saqlang.</p>
</div>
<h2>1. Shartlarni qabul qilish</h2>
<p>MoneyApp'ni o'rnatish va undan foydalanish orqali siz ushbu Shartlarga rozilik bildirasiz. Agar biron bir bandga rozi bo'lmasangiz, ilovadan foydalanishni to'xtating va hisobingizni o'chiring.</p>
<h2>2. Xizmat qanday ishlaydi</h2>
<p>Ilova "qanday bo'lsa, shunday" (AS IS) tamoyili asosida taqdim etiladi. Ma'lumotlar ishlab chiqaruvchining xususiy serveri bilan sinxronlanadi. Amallarni saqlash uchun internet aloqasi kerak — undatsiz kiritilgan ma'lumotlar serverga bormasligi mumkin.</p>
<p>Ishlab chiqaruvchi serverning uzluksiz ishlashini, ma'lumotlar saqlanishini yoki xizmatning istalgan vaqtda mavjud bo'lishini kafolatlamaydi.</p>
<h2>3. Cheklarni aniqlash</h2>
<p>Cheklarni tahlil qilish uchun bulutli xizmatlar (Google Gemini va OpenRouter orqali zaxira modellar) ishlatiladi. Aniqlik kafolatlanmaydi: model summa, sana, do'kon nomi yoki pozitsiyalarda xato qilishi mumkin.</p>
<p><strong>Saqlashdan oldin aniqlangan ma'lumotlarni tekshiring.</strong> Kiritilgan summalarning to'g'riligi uchun javobgarlik foydalanuvchiga yuklanadi.</p>
<h2>4. Sizning javobgarligingiz</h2>
<ul>
  <li>parolingiz va tiklash kodingiz xavfsizligi uchun javobgarsiz;</li>
  <li>saqlashdan oldin ma'lumotlar aniqligini tekshirasiz;</li>
  <li>ilovadan noqonuniy faoliyat uchun foydalanmaysiz;</li>
  <li>chek rasmlari uchinchi tomon sun'iy intellekt xizmatlariga uzatilishini tushunasiz.</li>
</ul>
<h2>5. Javobgarlikni cheklash</h2>
<p>Ishlab chiqaruvchi quyidagilar uchun javobgar emas:</p>
<ul>
  <li>har qanday moliyaviy yo'qotishlar;</li>
  <li>noto'g'ri tahlillar, noaniq summalar va xato kategoriyalar;</li>
  <li>ma'lumotlarni yo'qotish, baza shikastlanishi yoki server nosozliklari;</li>
  <li>ilova ma'lumotlari asosida qabul qilingan qarorlar.</li>
</ul>
<p>MoneyApp — bu buxgalteriya tizimi yoki professional moliyaviy maslahatchi emas, shaxsiy hisob vositasi.</p>
<h2>6. Foydalanishni to'xtatish</h2>
<p>Hisobingizni va barcha ma'lumotlarni "Hisob" bo'limidagi tugma orqali istalgan vaqtda o'chirib yuborishingiz mumkin. Ishlab chiqaruvchi xizmatdan suiiste'mol qilinganda kirishni to'xtatib turish huquqini o'zida saqlab qoladi.</p>
<h2>7. Shartlarga o'zgartirishlar</h2>
<p>Shartlar o'zgarishi mumkin. Yangi tahrir ushbu sahifada e'lon qilingan paytdan boshlab kuchga kiradi. Ilovadan foydalanishni davom ettirib, siz yangilangan shartlarni qabul qilasiz.</p>
<h2>Aloqa</h2>
<p>Savollar va texnik yordam: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>Shuningdek qarang: <a href="privacy.html">Maxfiylik siyosati</a>.</footer>
</div>
</body>
</html>""",

    "de": """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nutzungsbedingungen — MoneyApp</title>
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
<h1>Nutzungsbedingungen</h1>
<div class="date">Gültig ab: 18. September 2026</div>
<div class="warn">
  <h3>Beta-Version</h3>
  <p>MoneyApp befindet sich im frühen Teststadium. Störungen, Datenverlust und Berechnungsfehler können auftreten. Verwenden Sie die App nicht als einzige Buchhaltungsquelle — bewahren Sie ein Backup wichtiger Datensätze auf.</p>
</div>
<h2>1. Annahme der Bedingungen</h2>
<p>Durch die Installation und Nutzung von MoneyApp erklären Sie sich mit diesen Bedingungen einverstanden. Wenn Sie mit einem Punkt nicht einverstanden sind, stellen Sie die Nutzung der App ein und löschen Sie Ihr Konto.</p>
<h2>2. Funktionsweise des Dienstes</h2>
<p>Die App wird „wie besehen“ (AS IS) bereitgestellt. Die Daten werden mit einem privaten Server des Entwicklers synchronisiert. Für das Speichern von Transaktionen ist eine Internetverbindung erforderlich — ohne diese erreichen eingegebene Daten möglicherweise den Server nicht.</p>
<p>Der Entwickler garantiert keinen ununterbrochenen Serverbetrieb, keine Datensicherheit und keine ständige Verfügbarkeit des Dienstes.</p>
<h2>3. Belegenerkennung</h2>
<p>Zur Auswertung von Belegen werden Cloud-Dienste (Google Gemini und Backup-Modelle über OpenRouter) genutzt. Die Erkennungsgenauigkeit wird nicht garantiert: Das Modell kann sich bei Beträgen, Daten, Geschäftsnamen oder Positionen irren.</p>
<p><strong>Überprüfen Sie erkannte Daten vor dem Speichern.</strong> Die Verantwortung für die Korrektheit eingegebener Beträge liegt beim Benutzer.</p>
<h2>4. Ihre Verantwortung</h2>
<ul>
  <li>Sie sind verantwortlich für die Sicherheit Ihres Passworts und Wiederherstellungscodes;</li>
  <li>Sie überprüfen die Datenrichtigkeit vor dem Speichern;</li>
  <li>Sie nutzen die App nicht für illegale Aktivitäten;</li>
  <li>Sie verstehen, dass Belegbilder an KI-Dienste von Drittanbietern gesendet werden.</li>
</ul>
<h2>5. Haftungsbeschränkung</h2>
<p>Der Entwickler haftet nicht für:</p>
<ul>
  <li>finanzielle Verluste jeglicher Art;</li>
  <li>fehlerhafte Analysen, ungenaue Beträge und falsche Kategorien;</li>
  <li>Datenverlust, Beschädigung der Datenbank oder Serverausfälle;</li>
  <li>Entscheidungen, die auf Basis von App-Daten getroffen wurden.</li>
</ul>
<p>MoneyApp ist ein persönliches Tracking-Tool, kein Buchhaltungssystem und kein professioneller Finanzberater.</p>
<h2>6. Beendigung der Nutzung</h2>
<p>Sie können Ihr Konto und alle Daten jederzeit über den Bereich „Konto“ löschen. Der Entwickler behält sich das Recht vor, den Zugriff bei Missbrauch des Dienstes zu sperren.</p>
<h2>7. Änderungen der Bedingungen</h2>
<p>Die Bedingungen können sich ändern. Die Neufassung tritt mit der Veröffentlichung auf dieser Seite in Kraft. Durch die fortgesetzte Nutzung der App akzeptieren Sie die aktualisierten Bedingungen.</p>
<h2>Feedback</h2>
<p>Fragen und technischer Support: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>Siehe auch <a href="privacy.html">Datenschutzerklärung</a>.</footer>
</div>
</body>
</html>""",

    "es": """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Términos de uso — MoneyApp</title>
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
<h1>Términos de uso</h1>
<div class="date">Fecha de entrada en vigor: 18 de septiembre de 2026</div>
<div class="warn">
  <h3>Versión Beta</h3>
  <p>MoneyApp se encuentra en fase de pruebas tempranas. Pueden producirse fallos, pérdida de datos y errores de cálculo. No utilice la aplicación como su única fuente de contabilidad; mantenga una copia de seguridad de los registros importantes.</p>
</div>
<h2>1. Aceptación de los términos</h2>
<p>Al instalar y utilizar MoneyApp, usted acepta estos Términos. Si no está de acuerdo con cualquier parte, deje de usar la aplicación y elimine su cuenta.</p>
<h2>2. Cómo funciona el servicio</h2>
<p>La aplicación se proporciona "tal cual" (AS IS). Los datos se sincronizan con un servidor privado del desarrollador. Se requiere conexión a internet para guardar operaciones; sin ella, los datos introducidos pueden no llegar al servidor.</p>
<p>El desarrollador no garantiza el funcionamiento ininterrumpido del servidor, la integridad de los datos ni la disponibilidad del servicio en todo momento.</p>
<h2>3. Reconocimiento de recibos</h2>
<p>Se utilizan servicios en la nube (Google Gemini y modelos de respaldo a través de OpenRouter) para analizar los recibos. No se garantiza la precisión del reconocimiento: el modelo puede cometer errores en importes, fechas, nombres de comercios o artículos.</p>
<p><strong>Verifique los datos analizados antes de guardarlos.</strong> La responsabilidad de la exactitud de los importes introducidos recae en el usuario.</p>
<h2>4. Su responsabilidad</h2>
<ul>
  <li>usted es responsable de mantener seguros su contraseña y código de recuperación;</li>
  <li>usted verifica la precisión de los datos antes de guardarlos;</li>
  <li>no utiliza la aplicación para actividades ilegales;</li>
  <li>comprende que las imágenes de los recibos se envían a servicios de IA de terceros.</li>
</ul>
<h2>5. Limitación de responsabilidad</h2>
<p>El desarrollador no es responsable de:</p>
<ul>
  <li>pérdidas financieras de ningún tipo;</li>
  <li>análisis incorrectos, importes inexactos y categorías erróneas;</li>
  <li>pérdida de datos, daños en la base de datos o fallos del servidor;</li>
  <li>decisiones tomadas en base a los datos de la aplicación.</li>
</ul>
<p>MoneyApp es una herramienta de seguimiento personal, no un sistema contable ni un asesor financiero profesional.</p>
<h2>6. Terminación</h2>
<p>Puede eliminar su cuenta y todos los datos en cualquier momento desde la sección "Cuenta". El desarrollador se reserva el derecho de suspender el acceso en caso de uso indebido del servicio.</p>
<h2>7. Modificaciones de los términos</h2>
<p>Los términos pueden cambiar. La nueva edición entra en vigor desde el momento de su publicación en esta página. Al continuar utilizando la aplicación, usted acepta los términos actualizados.</p>
<h2>Contacto</h2>
<p>Preguntas y soporte técnico: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>Véase también la <a href="privacy.html">Política de privacidad</a>.</footer>
</div>
</body>
</html>"""
}

# Папка для условий использования (создадим в pages_t или корне по аналогии)
os.makedirs('pages_t', exist_ok=True)

# Записываем файлы
for lang, content in terms_translations.items():
    file_path = f"pages_t/terms_{lang}.html"
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"Создано: {file_path}")

print("Все переводы условий использования успешно сгенерированы!")
