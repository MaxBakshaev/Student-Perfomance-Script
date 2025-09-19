# ➤ 📄 Экспорт зависимостей poetry в requirements.txt
req:
	poetry export --without-hashes -f requirements.txt -o requirements.txt