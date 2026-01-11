import datetime

# 1. Создайте словарь email, содержащий следующие поля:
email = {
    "subject": "Тема письма",
    "from": "   Sender.Email@Example.COM   ",
    "to": "   Recipient.Email@Personal.ru   ",
    "body": "Это тело письма. Оно может быть очень длинным и содержать много текста. Мы будем обрабатывать его по заданию."
}

# 2. Добавьте дату отправки
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date

# 3. Нормализуйте e-mail адреса отправителя и получателя
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. Извлеките логин и домен отправителя
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

# 5. Создайте сокращённую версию текста
email["short_body"] = email["body"][:10] + "..."

# 6. Списки доменов
personal_domains = ['gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru']
corporate_domains = ['company.ru', 'corporation.com', 'university.edu', 'organization.org', 'company.ru', 'business.net']

# 7
# Проверьте что в списке личных и корпоративных доменов нет пересечений (вывод результата проверки в конце после
intersection = personal_domains & corporate_domains

# Убираем дубликаты (сделаем уникальными)
personal_domains = list(set(personal_domains))
corporate_domains = list(set(corporate_domains))

# 8. Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domains

# 9. Соберите «чистый» текст сообщения
clean_body = email["body"].replace("\t", " ").replace("\n", " ")
email["clean_body"] = clean_body

# 10. Сформируйте текст отправленного письма
email["sent_text"] = f"Кому: {email['to']}, от {email['from']} Тема: {email['subject']}, дата {email['date']} {email['clean_body']}"

# 11. Рассчитайте количество страниц печати
pages = (len(email["sent_text"]) + 499) // 500  # округление в большую сторону

# 12. Проверьте пустоту темы и тела письма
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

# 13. Создайте «маску» e-mail отправителя
email["masked_from"] = login[:2] + "***@" + domain

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru"
if "list.ru" in personal_domains:
    personal_domains.remove("list.ru")
if "bk.ru" in personal_domains:
    personal_domains.remove("bk.ru")

#  вывод ключевых результатов для быстрой проверки
print(email)
print(is_corporate, pages, is_subject_empty, is_body_empty)