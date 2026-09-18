import os
from pathlib import Path

# Переводы Privacy Policy по языкам
translations = {
    "en": """<!DOCTYPE html>
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
<p>MoneyApp developer respects your privacy. Below is a description of what data the app collects, where it goes, and how to delete it.</p>
<h2>1. Where Data is Stored</h2>
<p>MoneyApp operates on a private developer server (self-hosted model). There are no cloud providers between you and your data.</p>
<p><strong>What is stored:</strong></p>
<ul>
  <li>financial operations: amounts, dates, descriptions, accounts, and categories;</li>
  <li>scanned receipt photos and recognized items;</li>
  <li>bank statements uploaded for import;</li>
  <li>settings: currency, language, budget limits, templates, shopping list;</li>
  <li>username and password hash (the password itself is not stored);</li>
  <li>email address, if provided for access recovery.</li>
</ul>
<p>Each user's data resides in a separate database. Receipt photos are stored in a folder accessible only to the owner.</p>
<h2>2. Receipt Recognition & Third-Party AI Services</h2>
<p>The app requires camera and gallery access to recognize receipts and bank statements.</p>
<p>During scanning, images are transmitted to cloud recognition services: <strong>Google Gemini</strong>, and via backup models through <strong>OpenRouter</strong> if unavailable. Processing is governed by these providers' policies, which may use transmitted images to train their models.</p>
<div class="note">If you do not want your receipt sent to third-party services, enter the transaction manually — recognition will not be triggered.</div>
<h2>3. Error Reporting</h2>
<p>The app uses <strong>Sentry</strong> to collect crash data: error type, code location, app version, and device model. This helps find and fix crashes.</p>
<p>Reports do not contain amounts, operation names, receipt photos, or your IP address — personal data transmission is disabled. No screen recording is performed.</p>
<h2>4. Email</h2>
<p>If you specified an email for password recovery, the verification code letter is sent via <strong>Brevo</strong>. Only the recipient's address and the code letter text are transmitted. The app sends no newsletters or marketing emails.</p>
<h2>5. Notifications</h2>
<p>Expense entry reminders are created by your phone's operating system via timers. Push notification servers are not used.</p>
<h2>6. What the App Does Not Have</h2>
<ul>
  <li>ads and advertising SDKs;</li>
  <li>marketing trackers and profiling;</li>
  <li>transfer or sale of your data to third parties;</li>
  <li>access to contacts, location, microphone, or correspondence.</li>
</ul>
<h2>7. Retention Period</h2>
<p>Data is stored as long as you use the app. If the account is inactive for 24 months, associated data may be permanently deleted.</p>
<h2>8. Your Rights</h2>
<p>You can at any time:</p>
<ul>
  <li>view and correct any operation;</li>
  <li>reset operation history in app settings;</li>
  <li><strong>delete your account with all data</strong> via the "Account" section. Deletion is immediate and irreversible: operations, receipts, accounts, and the account itself are erased;</li>
  <li>request data export or deletion via email below — requests are processed within 3 business days.</li>
</ul>
<h2>9. Children</h2>
<p>The app is not intended for individuals under 13 years old and does not knowingly collect their data. If such data is discovered, it will be deleted.</p>
<h2>10. Changes</h2>
<p>The policy may be updated. The new edition takes effect upon publication on this page.</p>
<h2>Contacts</h2>
<p>Questions, data export, and deletion: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>MoneyApp — Personal finance tracking app. Beta version.</footer>
</div>
</body>
</html>""",

    "tr": """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gizlilik Politikası — MoneyApp</title>
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
<h1>Gizlilik Politikası</h1>
<div class="date">Yürürlük tarihi: 18 Eylül 2026</div>
<p>MoneyApp geliştiricisi gizliliğinize saygı duyar. Aşağıda uygulamanın hangi verileri topladığı, nereye aktardığı ve nasıl silineceği açıklanmaktadır.</p>
<h2>1. Veriler Nerede Saklanır</h2>
<p>MoneyApp, geliştiricinin özel sunucusunda (self-hosted model) çalışır. Sizinle verileriniz arasında hiçbir bulut sağlayıcısı yoktur.</p>
<p><strong>Ne saklanır:</strong></p>
<ul>
  <li>finansal işlemler: tutarlar, tarihler, açıklamalar, hesaplar ve kategoriler;</li>
  <li>taranan fiş fotoğrafları ve bunlardan tanınan kalemler;</li>
  <li>içe aktarmak için yüklediğiniz banka ekstreleri;</li>
  <li>ayarlar: para birimi, dil, bütçe limitleri, şablonlar, alışveriş listesi;</li>
  <li>kullanıcı adı ve şifre hash'i (şifrenin kendisi saklanmaz);</li>
  <li>erişimi kurtarmak için belirttiyseniz e-posta adresiniz.</li>
</ul>
<p>Her kullanıcının verileri ayrı bir veritabanında bulunur. Fiş fotoğrafları yalnızca sahibinin erişebileceği bir klasörde saklanır.</p>
<h2>2. Fiş Tanıma ve Üçüncü Taraf Yapay Zeka Servisleri</h2>
<p>Uygulamanın fişleri ve banka dekontlarını tanıyabilmesi için kamera ve galeri erişimine ihtiyacı vardır.</p>
<p>Tarama sırasında görüntü bulut tanıma servislerine gönderilir: <strong>Google Gemini</strong> ve kullanılamazsa <strong>OpenRouter</strong> üzerinden yedek modeller. İşlem, iletilen görüntüleri modellerini eğitmek için kullanabilecek bu sağlayıcıların politikalarına tabidir.</p>
<div class="note">Fişinizin üçüncü taraf servislerine gitmesini istemiyorsanız, işlemi manuel olarak girin — bu durumda tanıma tetiklenmez.</div>
<h2>3. Hata Raporları</h2>
<p>Uygulama çökmeleri toplamak için <strong>Sentry</strong> kullanır: hata türü, koddaki konum, uygulama sürümü ve cihaz modeli. Bu, çökmeleri bulup düzeltmek için gereklidir.</p>
<p>Raporlar tutarlar, işlem adları, fiş fotoğrafları veya IP adresinizi içermez — kişisel veri gönderimi devre dışıdır. Ekran kaydı yapılmaz.</p>
<h2>4. E-posta</h2>
<p>Şifre kurtarma için e-posta belirttiyseniz, kod içeren e-posta <strong>Brevo</strong> servisi aracılığıyla gönderilir. Yalnızca alıcının adresi ve kod metni aktarılır. Uygulama bülten veya pazarlama e-postaları göndermez.</p>
<h2>5. Bildirimler</h2>
<p>Gider ekleme hatırlatıcıları, telefonunuzun işletim sistemi tarafından zamanlayıcı aracılığıyla oluşturulur. Push bildirim sunucuları kullanılmaz.</p>
<h2>6. Uygulamada Olmayanlar</h2>
<ul>
  <li>reklamlar ve reklam SDK'ları;</li>
  <li>pazarlama takipçileri ve profilleme;</li>
  <li>verilerinizin üçüncü şahıslara aktarılması veya satılması;</li>
  <li>kişilere, konuma, mikrofona ve yazışmalara erişim.</li>
</ul>
<h2>7. Saklama Süresi</h2>
<p>Veriler, uygulamayı kullandığınız sürece saklanır. Hesap 24 ay boyunca etkin değilse, ilgili veriler kalıcı olarak silinebilir.</p>
<h2>8. Haklarınız</h2>
<p>İstediğiniz zaman:</p>
<ul>
  <li>herhangi bir işlemi görüntüleyebilir ve düzeltebilirsiniz;</li>
  <li>işlem geçmişini uygulama ayarlarından sıfırlayabilirsiniz;</li>
  <li><strong>tüm verilerinizle birlikte hesabınızı silebilirsiniz</strong> ("Hesap" bölümündeki düğme). Silme işlemi anında ve geri alınamaz şekilde gerçekleşir: işlemler, fişler, hesaplar ve hesabın kendisi silinir;</li>
  <li>aşağıda belirtilen e-posta yoluyla veri dışa aktarımı veya silme talebinde bulunabilirsiniz — talep 3 iş günü içinde işleme alınır.</li>
</ul>
<h2>9. Çocuklar</h2>
<p>Uygulama 13 yaş altı kişilere yönelik değildir ve onların verilerini bilerek toplamaz. Bu tür veriler tespit edilirse silinecektir.</p>
<h2>10. Değişiklikler</h2>
<p>Politika güncellenebilir. Yeni sürüm, bu sayfada yayınlandığı anda yürürlüğe girer.</p>
<h2>İletişim</h2>
<p>Sorular, veri dışa aktarımı ve silme işlemleri: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>MoneyApp — Kişisel finans takip uygulaması. Beta sürümü.</footer>
</div>
</body>
</html>""",

    "uz": """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maxfiylik siyosati — MoneyApp</title>
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
<h1>Maxfiylik siyosati</h1>
<div class="date">Kuchga kirish sanasi: 2026-yil 18-sentyabr</div>
<p>MoneyApp ilovasi ishlab chiqaruvchisi sizning maxfiyligingizni hurmat qiladi. Quyida ilova qanday ma'lumotlarni to'plashi, ular qayerga borishi va ularni qanday o'chirish mumkinligi tasvirlangan.</p>
<h2>1. Ma'lumotlar qayerda saqlanadi</h2>
<p>MoneyApp ishlab chiqaruvchining xususiy serverida (self-hosted model) ishlaydi. Siz va ma'lumotlaringiz o'rtasida hech qanday bulutli provayder yo'q.</p>
<p><strong>Nima saqlanadi:</strong></p>
<ul>
  <li>moliyaviy amallar: summalar, sanalar, tavsiflar, hisoblar va kategoriyalar;</li>
  <li>skanerlangan chek fotosuratlari va ulardan aniqlangan pozitsiyalar;</li>
  <li>import qilish uchun yuklagan bank ko'chirmalari;</li>
  <li>sozlamalar: valyuta, til, byudjet limitlari, namunalar, xaridlar ro'yxati;</li>
  <li>foydalanuvchi nomi va parol xeshi (parolning o'zi saqlanmaydi);</li>
  <li>kirishni tiklash uchun ko'rsatgan bo'lsangiz, elektron pochta manzili.</li>
</ul>
<p>Har bir foydalanuvchining ma'lumotlari alohida ma'lumotlar bazasida saqlanadi. Chek fotosuratlari faqat egasiga ruxsat etilgan papkada saqlanadi.</p>
<h2>2. Cheklarni aniqlash va uchinchi tomon sun'iy intellekt xizmatlari</h2>
<p>Cheklar va bank kvitansiyalarini aniqlash uchun ilovaga kamera va galereyaga kirish huquqi kerak.</p>
<p>Skanerlash vaqtida tasvir bulutli aniqlash xizmatlariga uzatiladi: <strong>Google Gemini</strong>, mavjud bo'lmaganda <strong>OpenRouter</strong> orqali zaxira modellar. Qayta ishlash ushbu provayderlarning siyosatlari bilan tartibga solinadi, ular uzatilgan tasvirlardan o'z modellarini o'qitish uchun foydalanishi mumkin.</p>
<div class="note">Agar chekingiz uchinchi tomon xizmatlariga tushishini xohlamasangiz, amalni qo'lda kiriting — bunda tanib olish ishga tushmaydi.</div>
<h2>3. Xatolar haqida hisobotlar</h2>
<p>Ilova nosozliklar haqida ma'lumot yig'ish uchun <strong>Sentry</strong>'dan foydalanadi: xato turi, kodDagi joylashuvi, ilova versiyasi va qurilma modeli. Bu xatoliklarni topish va bartaraf etish uchun kerak.</p>
<p>Hisobotlarda summalar, amallar nomlari, chek fotosuratlari va IP-manzilingiz bo'lmaydi — shaxsiy ma'lumotlarni yuborish o'chirilgan. Ekran yozib olinmaydi.</p>
<h2>4. Elektron pochta</h2>
<p>Parolni tiklash uchun pochta ko'rsatgan bo'lsangiz, kod bilan xat <strong>Brevo</strong> xizmati orqali yuboriladi. Unga faqat qabul qiluvchining manzili va kodli xat matni uzatiladi. Ilova reklama va marketing xatlarini yubormaydi.</p>
<h2>5. Bildirishnomalar</h2>
<p>Xarajatlarni kiritish haqidagi eslatmalar telefoningiz operatsion tizimi tomonidan taymer bo'yicha yaratiladi. Push-xabarnoma serverlaridan foydalanilmaydi.</p>
<h2>6. Ilovada nimalar yo'q</h2>
<ul>
  <li>reklama va reklama SDK'lari;</li>
  <li>marketing trekerlari va profillash;</li>
  <li>ma'lumotlaringizni uchinchi shaxslarga berish yoki sotish;</li>
  <li>kontaktlar, joylashuv, mikrofon va yozishmalarga kirish.</li>
</ul>
<h2>7. Saqlash muddati</h2>
<p>Ma'lumotlar ilovadan foydalanganingizcha saqlanadi. Agar hisob 24 oy davomida faol bo'lmasa, unga bog'langan ma'lumotlar qaytarib bo'lmaydigan tarzda o'chirib yuborilishi mumkin.</p>
<h2>8. Sizning huquqlaringiz</h2>
<p>Istalgan vaqtda quyidagilarni amalga oshirishingiz mumkin:</p>
<ul>
  <li>istalgan amalni ko'rish va to'g'rilash;</li>
  <li>amal tarixini noldan boshlash — ilova sozlamalarida;</li>
  <li><strong>barcha ma'lumotlar bilan birga hisobni o'chirish</strong> — "Hisob" bo'limidagi tugma. O'chirish darhol va qaytarib bo'lmaydigan tarzda sodir bo'ladi: amallar, cheklar, hisoblar va yozuvning o'zi o'chib ketadi;</li>
  <li>ma'lumotlarni chiqarib olish yoki quyida ko'rsatilgan pochta orqali o'chirishni so'rash — so'rov 3 ish kuni ichida bajariladi.</li>
</ul>
<h2>9. Bolalar</h2>
<p>Ilova 13 yoshga to'lmagan shaxslarga mo'ljallanmagan va ularning ma'lumotlarini o'z xohishi bilan to'plamaydi. Agar bunday ma'lumotlar aniqlansa, ular o'chirib tashlanadi.</p>
<h2>10. O'zgartirishlar</h2>
<p>Siyosat yangilanishi mumkin. Yangi tahrir ushbu sahifada e'lon qilingan paytdan boshlab kuchga kiradi.</p>
<h2>Aloqa</h2>
<p>Savollar, ma'lumotlarni chiqarib olish va o'chirish: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>MoneyApp — Shaxsiy moliya hisobi ilovasi. Beta-versiya.</footer>
</div>
</body>
</html>""",

    "de": """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Datenschutzerklärung — MoneyApp</title>
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
<h1>Datenschutzerklärung</h1>
<div class="date">Gültig ab: 18. September 2026</div>
<p>Der Entwickler der MoneyApp respektiert Ihre Privatsphäre. Im Folgenden wird beschrieben, welche Daten die App erfasst, wohin sie fließen und wie Sie diese löschen können.</p>
<h2>1. Wo Daten gespeichert werden</h2>
<p>MoneyApp läuft auf einem privaten Server des Entwicklers (Self-Hosted-Modell). Es gibt keinen Cloud-Anbieter zwischen Ihnen und Ihren Daten.</p>
<p><strong>Was gespeichert wird:</strong></p>
<ul>
  <li>Finanztransaktionen: Beträge, Daten, Beschreibungen, Konten und Kategorien;</li>
  <li>Fotos von gescannten Belegen und daraus erkannte Positionen;</li>
  <li>Hochgeladene Kontoauszüge für den Import;</li>
  <li>Einstellungen: Währung, Sprache, Budgetlimits, Vorlagen, Einkaufsliste;</li>
  <li>Benutzername und Passwort-Hash (das Passwort selbst wird nicht gespeichert);</li>
  <li>E-Mail-Adresse, falls zur Wiederherstellung angegeben.</li>
</ul>
<p>Die Daten jedes Benutzers liegen in einer separaten Datenbank. Belegfotos werden in einem Ordner gespeichert, auf den nur der Besitzer Zugriff hat.</p>
<h2>2. Belegenerkennung & KI-Dienste von Drittanbietern</h2>
<p>Die App benötigt Kamera- und Galeriezugriff, um Belege und Kontoauszüge zu erkennen.</p>
<p>Beim Scannen werden Bilder an Cloud-Erkennungsdienste übermittelt: <strong>Google Gemini</strong> und bei Nichtverfügbarkeit über Backup-Modelle via <strong>OpenRouter</strong>. Die Verarbeitung unterliegt den Richtlinien dieser Anbieter, die übermittelte Bilder möglicherweise zum Training ihrer Modelle verwenden.</p>
<div class="note">Wenn Sie nicht möchten, dass Ihr Beleg an Drittanbieterdienste gesendet wird, erfassen Sie die Transaktion manuell — die Erkennung wird dabei nicht ausgelöst.</div>
<h2>3. Fehlerberichte</h2>
<p>Die App verwendet <strong>Sentry</strong> zur Erfassung von Absturzdaten: Fehlerart, Code-Position, App-Version und Gerätemodell. Dies dient dem Finden und Beheben von Fehlern.</p>
<p>Berichte enthalten keine Beträge, Transaktionsnamen, Belegfotos oder Ihre IP-Adresse — die Übertragung persönlicher Daten ist deaktiviert. Es wird keine Bildschirmaufzeichnung durchgeführt.</p>
<h2>4. E-Mail</h2>
<p>Wenn Sie eine E-Mail zur Passwortwiederherstellung angegeben haben, wird der Code per <strong>Brevo</strong> versendet. Es werden lediglich die Empfängeradresse und der Text des Codes übermittelt. Die App versendet keine Newsletter oder Marketing-E-Mails.</p>
<h2>5. Benachrichtigungen</h2>
<p>Erinnerungen zur Expense-Erfassung werden vom Betriebssystem Ihres Telefons über Timer erstellt. Es werden keine Push-Server verwendet.</p>
<h2>6. Was die App nicht enthält</h2>
<ul>
  <li>Werbung und Werbe-SDKs;</li>
  <li>Marketing-Tracker und Profiling;</li>
  <li>Übertragung oder Verkauf Ihrer Daten an Dritte;</li>
  <li>Zugriff auf Kontakte, Standort, Mikrofon oder Nachrichten.</li>
</ul>
<h2>7. Speicherdauer</h2>
<p>Daten werden gespeichert, solange Sie die App nutzen. Ist das Konto 24 Monate lang inaktiv, können zugehörige Daten unwiderruflich gelöscht werden.</p>
<h2>8. Ihre Rechte</h2>
<p>Sie können jederzeit:</p>
<ul>
  <li>jede Transaktion einsehen und korrigieren;</li>
  <li>den Transaktionsverlauf in den App-Einstellungen zurücksetzen;</li>
  <li><strong>Ihr Konto mit allen Daten löschen</strong> — über die Schaltfläche im Bereich „Konto“. Die Löschung erfolgt sofort und unwiderruflich: Transaktionen, Belege, Konten und das Konto selbst werden gelöscht;</li>
  <li>einen Datenexport oder eine Löschung per E-Mail anfordern (siehe unten) — die Bearbeitung erfolgt innerhalb von 3 Werktagen.</li>
</ul>
<h2>9. Kinder</h2>
<p>Die App ist nicht für Personen unter 13 Jahren bestimmt und sammelt deren Daten nicht wissentlich. Werden solche Daten entdeckt, werden sie gelöscht.</p>
<h2>10. Änderungen</h2>
<p>Die Richtlinie kann aktualisiert werden. Die Neufassung tritt mit der Veröffentlichung auf dieser Seite in Kraft.</p>
<h2>Kontakt</h2>
<p>Fragen, Datenexport und Löschung: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>MoneyApp — App zur persönlichen Finanzverwaltung. Beta-Version.</footer>
</div>
</body>
</html>""",

    "es": """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Política de privacidad — MoneyApp</title>
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
<h1>Política de privacidad</h1>
<div class="date">Fecha de entrada en vigor: 18 de septiembre de 2026</div>
<p>El desarrollador de MoneyApp respeta su privacidad. A continuación se describe qué datos recopila la aplicación, dónde se almacenan y cómo eliminarlos.</p>
<h2>1. Dónde se almacenan los datos</h2>
<p>MoneyApp funciona en un servidor privado del desarrollador (modelo self-hosted). No existen proveedores de nube intermediarios entre usted y sus datos.</p>
<p><strong>Qué se almacena:</strong></p>
<ul>
  <li>operaciones financieras: importes, fechas, descripciones, cuentas y categorías;</li>
  <li>fotos de recibos escaneados y elementos reconocidos en ellos;</li>
  <li>extractos bancarios subidos para importación;</li>
  <li>configuraciones: moneda, idioma, límites de presupuesto, plantillas, lista de la compra;</li>
  <li>nombre de usuario y hash de contraseña (la contraseña en sí no se almacena);</li>
  <li>dirección de correo electrónico, si se proporcionó para la recuperación de acceso.</li>
</ul>
<p>Los datos de cada usuario residen en una base de datos independiente. Las fotos de los recibos se almacenan en una carpeta accesible únicamente para el propietario.</p>
<h2>2. Reconocimiento de recibos y servicios de IA de terceros</h2>
<p>La aplicación requiere acceso a la cámara y galería para reconocer recibos y extractos bancarios.</p>
<p>Durante el escaneo, las imágenes se transmiten a servicios de reconocimiento en la nube: <strong>Google Gemini</strong>, y mediante modelos de respaldo a través de <strong>OpenRouter</strong> si no está disponible. El procesamiento se rige por las políticas de dichos proveedores, que pueden utilizar las imágenes transmitidas para entrenar sus modelos.</p>
<div class="note">Si no desea que su recibo sea enviado a servicios de terceros, introduzca la operación manualmente; el reconocimiento no se iniciará.</div>
<h2>3. Informes de errores</h2>
<p>La aplicación utiliza <strong>Sentry</strong> para recopilar datos de fallos: tipo de error, ubicación en el código, versión de la aplicación y modelo de dispositivo. Esto es necesario para encontrar y solucionar fallos.</p>
<p>Los informes no contienen importes, nombres de operaciones, fotos de recibos ni su dirección IP; la transmisión de datos personales está desactivada. No se realizan grabaciones de pantalla.</p>
<h2>4. Correo electrónico</h2>
<p>Si indicó un correo electrónico para la recuperación de contraseña, el mensaje con el código se envía a través del servicio <strong>Brevo</strong>. Solo se transmiten la dirección del destinatario y el texto del código. La aplicación no envía boletines ni correos de marketing.</p>
<h2>5. Notificaciones</h2>
<p>Los recordatorios de registro de gastos son creados por el sistema operativo de su teléfono mediante temporizadores. No se utilizan servidores de notificaciones push.</p>
<h2>6. Qué no incluye la aplicación</h2>
<ul>
  <li>anuncios y SDKs de publicidad;</li>
  <li>rastreadores de marketing y perfiles;</li>
  <li>transferencia o venta de sus datos a terceros;</li>
  <li>acceso a contactos, ubicación, micrófono o mensajería.</li>
</ul>
<h2>7. Período de retención</h2>
<p>Los datos se almacenan mientras usted utilice la aplicación. Si la cuenta permanece inactiva durante 24 meses, los datos asociados podrán eliminarse de forma permanente.</p>
<h2>8. Sus derechos</h2>
<p>Puede en cualquier momento:</p>
<ul>
  <li>ver y corregir cualquier operación;</li>
  <li>restablecer el historial de operaciones en los ajustes de la aplicación;</li>
  <li><strong>eliminar su cuenta con todos los datos</strong> desde la sección "Cuenta". La eliminación es inmediata e irreversible: se borran operaciones, recibos, cuentas y la propia cuenta;</li>
  <li>solicitar la exportación o eliminación de datos a través del correo electrónico indicado más abajo; la solicitud se procesa en un plazo de 3 días laborables.</li>
</ul>
<h2>9. Menores</h2>
<p>La aplicación no está destinada a menores de 13 años ni recopila conscientemente sus datos. Si se descubren tales datos, serán eliminados.</p>
<h2>10. Modificaciones</h2>
<p>La política puede actualizarse. La nueva versión entra en vigor desde el momento de su publicación en esta página.</p>
<h2>Contactos</h2>
<p>Preguntas, exportación y eliminación de datos: <a href="mailto:yamaladec@gmail.com">yamaladec@gmail.com</a></p>
<footer>MoneyApp — Aplicación de control de finanzas personales. Versión beta.</footer>
</div>
</body>
</html>"""
}

# Папка для политик конфиденциальности
os.makedirs('pages_p', exist_ok=True)

# Записываем файлы
for lang, content in translations.items():
    file_path = f"pages_p/privacy_{lang}.html"
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"Создано: {file_path}")

print("Все переводы политики конфиденциальности успешно сгенерированы!")
