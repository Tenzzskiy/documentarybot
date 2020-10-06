from docxtpl import DocxTemplate

doc = DocxTemplate("/Users/aleksandrten/Downloads/github/technobot/shablon.docx")
context = { 'emitent' : 'ООО Ромашка', 'address1' : 'г. Москва, ул. Долгоруковская, д. 0', 'участник': 'ООО Участник', 'адрес_участника': 'г. Москва, ул. Полевая, д. 0', 'director': 'И.И. Иванов'}
doc.render(context)
doc.save("/Users/aleksandrten/Downloads/github/technobot/finalcut.docx")
