---
layout: default
title: MoneyApp — Умный учет финансов
---

<style>
  /* Базовый сброс и шрифты */
  body { margin: 0; font-family: system-ui, -apple-system, sans-serif; background: #0f172a; color: #f8fafc; line-height: 1.6; }
  .container { max-width: 1000px; margin: 0 auto; padding: 0 20px; }
  
  /* Главный экран */
  .hero { text-align: center; padding: 80px 0 60px; }
  .hero h1 { font-size: 3.5rem; background: linear-gradient(to right, #818cf8, #c084fc); -webkit-background-clip: text; color: transparent; margin-bottom: 20px; }
  .hero p { font-size: 1.25rem; color: #94a3b8; max-width: 600px; margin: 0 auto 40px; }
  .btn { display: inline-block; background: #6366f1; color: white; padding: 16px 32px; border-radius: 8px; font-weight: 600; text-decoration: none; transition: background 0.2s; font-size: 1.1rem; box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39); }
  .btn:hover { background: #4f46e5; }
  
  /* Сетка карточек с функциями */
  .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin: 60px 0; }
  .card { background: #1e293b; padding: 30px; border-radius: 16px; border: 1px solid #334155; transition: transform 0.2s; }
  .card:hover { transform: translateY(-5px); border-color: #475569; }
  .card h3 { color: #f1f5f9; margin-top: 0; font-size: 1.4rem; }
  .card p { color: #94a3b8; font-size: 1rem; margin-bottom: 0; }

  /* Технический стек */
  .tech-stack { text-align: center; margin: 60px 0; padding: 40px; background: #1e293b; border-radius: 16px; border: 1px solid #334155; }
  .tech-tags { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 20px; }
  .tag { background: #0f172a; color: #e2e8f0; padding: 8px 16px; border-radius: 99px; font-size: 0.9rem; border: 1px solid #334155; }
  
  /* Подвал */
  footer { text-align: center; padding: 40px 0; border-top: 1px solid #334155; color: #64748b; font-size: 0.9rem; margin-top: 40px; }
  footer a { color: #818cf8; text-decoration: none; }
  footer a:hover { text-decoration: underline; }
</style>

<div class="container">
  <header class="hero">
    <h1>MoneyApp</h1>
    <p>Умный учет финансов с автоматическим распознаванием чеков. Полный контроль бюджета без рутинного ввода.</p>
    <a href="https://github.com/mrcsbek/mrcsbek.github.io/releases/download/v1.0.0/application-44bf268d-0f77-4826-a618-2a5741c74e1b.apk" class="btn">Скачать APK для Android</a>
  </header>

  <section class="features">
    <div class="card">
      <h3>📷 Мгновенный ввод</h3>
      <p>Интеграция CameraX и Google ML Kit OCR. Наведите камеру на чек, и алгоритм автоматически спарсит позиции и суммы.</p>
    </div>
    <div class="card">
      <h3>📊 Точная категоризация</h3>
      <p>Организация финансов со строгой двухуровневой иерархией категорий для максимальной прозрачности аналитики.</p>
    </div>
    <div class="card">
      <h3>🛡 Полная приватность</h3>
      <p>Никакой передачи чеков на серверы. Обработка изображений и хранение базы данных происходят локально на устройстве.</p>
    </div>
    <div class="card">
      <h3>🎯 Контроль бюджета</h3>
      <p>Индивидуальные правила и жесткие лимиты расходования средств для каждой категории с системой предупреждений.</p>
    </div>
  </section>

  <section class="tech-stack">
    <h2>Технический профиль</h2>
    <div class="tech-tags">
      <span class="tag">Android</span>
      <span class="tag">React Native Expo</span>
      <span class="tag">CameraX</span>
      <span class="tag">ML Kit OCR</span>
      <span class="tag">Local SQLite</span>
    </div>
  </section>

  <footer>
    <p>© 2026 MoneyApp.<br><a href="privacy.html">Политика конфиденциальности</a></p>
  </footer>
</div>
