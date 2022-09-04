temperaturaC = float(input('digite a temperatura em °C: '))
farenheit = 1.8 * temperaturaC + 32
print(f'a tenperatura de {temperaturaC}°C corresponde a {farenheit:.1f}°F!')
temperaturaF = float(input('digite a temperatura em °F: '))
celsius = (temperaturaF - 32) / 1.8
print(f'a tenperatura de {temperaturaF}°F corresponde a {celsius:.1f}°C!')