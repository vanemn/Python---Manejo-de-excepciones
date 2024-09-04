class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        """
        Inicializa la excepción DimensionError con los detalles del error.

        Parámetros:
        -----------
        mensaje : str
            Mensaje descriptivo del error.
        dimension : str, opcional
            Nombre de la dimensión afectada (por ejemplo, 'ancho' o 'alto').
        maximo : int, opcional
            Valor máximo permitido para la dimensión.
        """
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        """
        Retorna una representación en forma de cadena del mensaje de error.

        Si los atributos `dimension` y `maximo` no se proporcionaron, retorna el mensaje de la clase base.
        En caso contrario, retorna un mensaje detallado con el nombre de la dimensión y el valor máximo permitido.

        Retorna:
        --------
        str: Mensaje de error detallado.
        """
        if self.dimension is None or self.maximo is None:
            return super().__str__()
        return f"{self.mensaje}. Dimension: {self.dimension}, Máximo permitido: {self.maximo}"
