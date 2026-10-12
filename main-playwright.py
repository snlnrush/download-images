from playwright.sync_api import sync_playwright
with sync_playwright() as p:
	# Запускаем Chromium
	browser = p.chromium.launch()

	# Показываем окно браузера и замедляем действия на 50 мс
	# browser = p.chromium.launch(
	#	headless=False, # параметр управляет режимом показа браузера или работы в фоне
	#	slow_mo=50
	# )

	# Создаём новую вкладку
	page = browser.new_page()
	# Переходим на страницу и ждём её загрузки
	page.goto("https://www.liitokala.com.cn/battery/LiitoKala-Battery/417.html")
	# Получаем заголовок страницы
	print(page.title())
	header_h1 = page.locator("[class = 'title']").nth(0).inner_text()
	print(header_h1)
	images = page.locator("img").all()

	images_url = set()

	for item in images:
		if 'Upload' in item.get_attribute('src'):
			images_url.add(item.get_attribute('src'))

	print(images_url)

	# images_url = page.get_attribute('div a img', 'src')
	# print(images_url)

	# Сохраняем скриншот в файл
	page.screenshot(path="example.png")
	# Закрываем браузер
	browser.close()

