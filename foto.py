from error import DimensionError

class Foto:

    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Inicializa una nueva instancia de la clase Foto.

        Parámetros:
        -----------
        ancho : int
            El ancho inicial de la foto.
        alto : int
            El alto inicial de la foto.
        ruta : str
            La ruta de la ubicación de la foto.

        """
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        """
        Obtiene el valor del ancho de la foto.

        Retorna:
        --------
        int: El ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """
        Establece un nuevo valor de ancho para la foto.

        Lanza una excepción si el valor proporcionado es menor a 1 o mayor que el valor máximo permitido (`MAX`).

        Parámetros:
        -----------
        ancho : int
            El nuevo valor para el ancho de la foto.

        Excepciones:
        ------------
        DimensionError:
            Si el ancho es menor a 1 o mayor al máximo permitido.
        """
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError("Valor de ancho inválido", "ancho", Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """
        Obtiene el valor del alto de la foto.

        Retorna:
        --------
        int: El alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """
        Establece un nuevo valor de alto para la foto.

        Lanza una excepción si el valor proporcionado es menor a 1 o mayor que el valor máximo permitido (`MAX`).

        Parámetros:
        -----------
        alto : int
            El nuevo valor para el alto de la foto.

        Excepciones:
        ------------
        DimensionError:
            Si el alto es menor a 1 o mayor al máximo permitido.
        """
        if alto < 1 or alto > Foto.MAX:
            raise DimensionError("Valor de alto inválido", "alto", Foto.MAX)
        self.__alto = alto
