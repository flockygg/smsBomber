import requests

# Список игр с URL изображений
games = [
    {"name": "Cyberpunk 2077", "icon_url": "https://example.com/cyberpunk-icon.jpg", "banner_url": "https://example.com/cyberpunk-banner.jpg"},
    {"name": "Elden Ring", "icon_url": "https://example.com/eldenring-icon.jpg", "banner_url": "https://example.com/eldenring-banner.jpg"},
    # Добавьте больше игр
]

# Функция для скачивания файлов
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"{filename} успешно загружен!")
    else:
        print(f"Не удалось загрузить {filename}.")

# Скачивание иконок и баннеров
for game in games:
    download_file(game["icon_url"], f"assets/icons/{game['name'].lower().replace(' ', '_')}-icon.jpg")
    download_file(game["banner_url"], f"assets/banners/{game['name'].lower().replace(' ', '_')}-banner.jpg")