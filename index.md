---
layout: default
title: MoneyApp — Умный учет финансов
---

<style>
  body { background-color: #121212; color: #e0e0e0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 30px; }
  h1, h2, h3 { color: #ffffff; margin-top: 1.5em; }
  a { color: #bb86fc; text-decoration: none; }
  a:hover { text-decoration: underline; }
  .download-btn { display: inline-block; background-color: #bb86fc; color: #121212; padding: 12px 24px; font-weight: bold; border-radius: 8px; margin: 20px 0; text-decoration: none; }
  .download-btn:hover { background-color: #9965f4; text-decoration: none; }
  hr { border: 1px solid #333; margin: 40px 0; }
  code { background-color: #2a2a2a; padding: 2px 6px; border-radius: 4px; color: #ffb86c; }
</style>

# MoneyApp
Умный учет финансов с автоматическим распознаванием чеков. Полный контроль над бюджетом без рутинного ручного ввода.

<a href="СЮДА_ВСТАВИТЬ_ССЫЛКУ_НА_APK" class="download-btn">Скачать для Android (.apk)</a>

## Ключевые функции
* **Мгновенный ввод данных:** Интеграция CameraX и ML Kit OCR позволяет парсить кассовые чеки и переносить позиции в базу.
* **Продвинутая аналитика:** Настраиваемые финансовые модели со строгой двухуровневой иерархией подкатегорий.
* **Контроль бюджета:** Индивидуальные правила и жесткие лимиты расходования средств для каждой отдельной категории.
* **Локальная обработка:** Все финансовые данные и распознавание текста происходят локально на устройстве без отправки на сторонние серверы.

---

## Техническая спецификация
* **Платформа:** Android.
* **Фреймворк:** React Native Expo.
* **Ядро сканирования:** CameraX + Google ML Kit OCR.

## Схема данных (Базовые модули)
* `Transactions`: Сумма, дата, ID категории, фото чека, сырой текстовый вывод после OCR-парсинга.
* `Categories`: Дерево финансовых категорий.
* `Budgets`: Правила и финансовые лимиты.
