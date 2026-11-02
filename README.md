# ClearSlip — Landing Page & Releases

Официальная веб-страница и дистрибутив мобильного приложения ClearSlip. 

🔗 **Сайт:** [clearslip.app](https://clearslip.app)
📦 **Скачать APK:** [Последний релиз](https://github.com/mrcsbek/mrcsbek.github.io/releases)

## О проекте
ClearSlip — приложение для умного учета финансов с автоматическим сканированием чеков.
* **Платформа:** Android (React Native Expo)
* **Архитектура:** Self-hosted (синхронизация с личным сервером разработчика)
* **Стек:** CameraX + Google ML Kit OCR + облачный ИИ-парсинг (Gemini)
* **Приватность:** Без рекламы, трекеров и передачи аналитики третьим лицам.

## Структура репозитория
Этот публичный репозиторий содержит только сайт (Jekyll) и `.apk` в разделе Releases.

```
index.html, privacy.html, terms.html, delete-account.html   английская версия (корень)
ru/ tr/ uz/ es/ de/ fr/ ar/                                 те же страницы на других языках
_data/<язык>.yml                                            тексты сайта, версия, «Что нового»
_layouts/  _includes/                                       шаблоны страниц и общий <head>
assets/site.css                                             стили
assets/img/                                                 иконка и картинка для превью ссылок
assets/screens/                                             скриншоты приложения
favicon.ico, apple-touch-icon.png                           иконки (браузеры ищут их в корне)
CNAME, robots.txt, sitemap.xml, .well-known/                домен, поиск, security.txt
```

> [!NOTE]
> Исходный код мобильного приложения и серверной части размещен в изолированных приватных репозиториях для обеспечения криптографической безопасности, защиты API-ключей и сокрытия эндпоинтов бэкенда.

---
**Служба поддержки:** support@clearslip.app
