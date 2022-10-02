import pokemon

pikachu = pokemon.pokemon()
regionPikachu = pokemon.hoenn()
ataquePikachu = pokemon.electrico()

pikachu.setNombre("Pikachu")
pikachu.setAltura(0.5)
pikachu.setEstadoCapturado("Capturado")

infoPoke = ("---- POKEMON ----")
infoPoke += f"\nNombre: {pikachu.getNombre()}" 
infoPoke += f"\nEstado de captura: {pikachu.getEstadoCapturado()}" 
infoPoke += f"\nAltura: {pikachu.getAltura()}" 

infoPoke += f"\nRegion: {regionPikachu.getRegion()}" 

infoPoke += f"\nTipo: {ataquePikachu.tipo}"
infoPoke += f"\nAtaque 1: {ataquePikachu.ataque1('Impactrueno')}"

print(infoPoke)