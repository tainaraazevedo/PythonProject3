# o assert sempre verifica se o retorno da condiçao é true
assert True

# assert numbers
#num_esperado = 1
#num_obtido = 2
#assert num_esperado > num_obtido, f"Esperado{num_esperado} nao é maior que o numero Atual{num_obtido}."

# assert text
text_esperado = "selenium webdriver"
text_obtido = "selenium Webdriver"
assert text_esperado.lower() == text_obtido.lower(),f"Esperado{text_esperado},  Atual{text_obtido}."


# assert text in string
text_esperado = "seleniumddd"
text_obtido = "selenium Webdriver"
assert text_esperado.lower() in text_obtido.lower(),f"Esperado '{text_esperado}', dentro da string Atual'{text_obtido}'."


# assert is_displeyed/is_enabled/is_selected