import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import lxml


def get_image_urls(url_page: str, headers):
	url = url_page

	image_urls = []

	response = requests.get(url, headers=headers, timeout=20)
	response.raise_for_status()

	# html - в нее можно закинуть код страницы вручную, если автоматически не получается
	# html = """<div data-v-29bc99d1="" class="swiper-slide swiper-slide-active"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113858_17642.jpg" alt="p0"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide swiper-slide-next"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113901_53430.jpg" alt="p1"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113903_89291.jpg" alt="p2"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113906_60554.jpg" alt="p3"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113907_98627.jpg" alt="p4"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113908_86338.gif" alt="p5"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113910_28765.gif" alt="p6"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113911_61917.gif" alt="p7"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113913_56026.gif" alt="p8"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113913_33029.jpg" alt="p9"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113915_29064.gif" alt="p10"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113916_71571.gif" alt="p11"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113917_41804.gif" alt="p12"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113918_94378.jpg" alt="p13"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113919_10248.jpg" alt="p14"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113921_70314.jpg" alt="p15"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113922_35662.jpg" alt="p16"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113924_36237.jpg" alt="p17"><!----><!----></div><div data-v-29bc99d1="" class="swiper-slide"><img data-v-29bc99d1="" class="content-big-img" src="https://www.nitecore.com/storage/images/album/uploads/attached/image/20240911/20240911113925_41554.jpg" alt="p18"><!----><!----></div>"""


	# для LiitoKala soup = BeautifulSoup(response.text, "html.parser")
	soup = BeautifulSoup(response.text, "lxml")
	# для nitecore soup = BeautifulSoup(html, "lxml")

	for img in soup.find_all("img"):
		print(img)
		src = img.get("src")
		print(src)
		if not src:
			continue
#		if src.startswith('/Upload/'):
		if src.startswith('/uploads/allimg'):
			print(src)
			image_url = urljoin(url, src)
			print(image_url)
			image_urls.append(image_url)

	return tuple(image_urls)


def load_save_images(image_urls: tuple, save_dir, headers ):
	for image_url in image_urls:
		image_response = requests.get(image_url, headers=headers, timeout=30)
		image_response.raise_for_status()

		filename = Path(urlparse(image_url).path).name

		file_path = save_dir / filename

		file_path.write_bytes(image_response.content)
		print(f"Скачано: {image_url}")
		print(f"Сохранено: {file_path}")


def main():
	URL = "https://www.foxsur.com/products/163.html"

	SAVE_DIR = Path(r"H:\Besolve-images-work")
	headers = {"User-Agent": "Mozilla/5.0"}
	img_urls = get_image_urls(URL, headers)

	load_save_images(img_urls, SAVE_DIR, headers)


if __name__ == '__main__':
	main()
