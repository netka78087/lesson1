def format_price(price):
	return str('Цена: ' + str(float(price)) + 'руб.')

display_price = format_price('56.24')
print(display_price)
