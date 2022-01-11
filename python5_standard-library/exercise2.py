#py -m pip install emoji
# La utilidad pip instala los paquetes y las dependencias que se enumeran en el
# índice de paquetes de Python (PyPI)
import emoji
message = emoji.emojize('Howdy :sun_with_face:')
print(message)