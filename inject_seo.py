import os
from pathlib import Path

# Словарь переводов для тегов description и keywords под каждый язык
seo_data = {
    "ru": {
        "desc": "MoneyApp — умный трекер финансов с ИИ-распознаванием чеков, строгой иерархией категорий и поддержкой мультивалютности. Скачать APK.",
        "keys": "MoneyApp, учет финансов, трекер расходов, приложение для бюджета, финансы APK, распознавание чеков ИИ"
    },
    "en": {
        "desc": "MoneyApp — smart finance tracker with AI receipt recognition, strict category hierarchy, and multi-currency support. Download APK.",
        "keys": "MoneyApp, finance tracker, expense tracker, budget app, finance APK, AI receipt scanning"
    },
    "tr": {
        "desc": "MoneyApp — yapay zeka fiş tanıma, katı kategori hiyerarşisi ve çoklu para birimi desteğine sahip akıllı finans takip uygulaması. APK İndir.",
        "keys": "MoneyApp, finans takibi, bütçe uygulaması, gider takibi, para yönetimi APK"
    },
    "uz": {
        "desc": "MoneyApp — sun'iy intellekt orqali cheklarni aniqlash, qat'iy kategoriya ierarxiyasi va ko'p valyutalarni qo'llab-quvvatlovchi aqlli moliya ilovasi. APK yuklab olish.",
        "keys": "MoneyApp, moliya hisobi, xarajatlar trekeri, byudjet ilovasi, moliya APK"
    },
    "de": {
        "desc": "MoneyApp — intelligenter Finanztracker mit KI-Belegerkennung, strikter Kategoriehierarchie und Multiwährungsunterstützung. APK herunterladen.",
        "keys": "MoneyApp, Finanztracker, Haushaltsbuch App, Budget App, Ausgaben verwalten APK"
    },
    "es": {
        "desc": "MoneyApp — rastreador inteligente de finanzas con reconocimiento de recibos por IA, estricta jerarquía de categorías y soporte multidivisa. Descargar APK.",
        "keys": "MoneyApp, control de gastos, finanzas personales, app de presupuesto, APK finanzas"
    }
}

# Функция вставки мета-тегов в HTML
def process_file(file_path, lang):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Проверяем, есть ли уже теги, чтобы не дублировать
    if 'name="description"' in content:
        print(f"Пропущено (уже есть теги): {file_path}")
        return

    meta_tags = f'    <meta name="description" content="{seo_data[lang]["desc"]}">\n    <meta name="keywords" content="{seo_data[lang]["keys"]}">\n'

    # Вставляем сразу после <head>
    if '<head>' in content:
        content = content.replace('<head>', '<head>\n' + meta_tags)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Обновлено: {file_path} ({lang})")

# Проходим по корню и папке indexes
root_index = Path('index.html')
if root_index.exists():
    process_file(root_index, 'ru')

indexes_dir = Path('indexes')
if indexes_dir.exists():
    for file in indexes_dir.glob('index_*.html'):
        # определяем язык по имени файла (например, index_en.html -> en)
        lang_code = file.stem.split('_')[1]
        if lang_code in seo_data:
            process_file(file, lang_code)

print("Готово!")
