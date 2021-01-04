class ShodanCredentialsError(Exception):
    """Zgłasza wyjątek gdy nie można utworzyć obiketu przechowujące dane użytkownika do seriwsu https://shodan.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class ShodanCredentials:
    """Klasa przechowująca wymagane dane dla seriwsu trzeciego https://shodan.io/.
    Daje także możliwość aktualizacji danych uwierzytelniających użytkownika np. w przypadku przekroczenia ilości
    wyszukiwań na darmowym koncie w serwisie."""

    def __init__(self, data):
        if not data:
            raise ShodanCredentialsError("No data to https://shodan.io/ service. Please check "
                                         "sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json file.")

        self.data= data
        self.__base_url = self.__set_data("base_url")
        self.__api_key = self.__set_data("api_key")
        self.__user = self.__set_data("user")

    def __set_data(self, info_tag:str):
        """Metoda pomocnicza zwracajaca wybrane ifnormacje do seriwsu http://censys.io/ z pliku user_credentials.json
        :param: info_tag
        """
        if self.data.get(info_tag, None):
            return self.data[info_tag]
        else:
            raise ShodanCredentialsError(f'No data in "{info_tag}" for https://shodan.io/ service. Please check '
                                         f'sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json file.')

    @property
    def base_url(self):
        return self.__base_url

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self):
        return self.__api_key

    @property
    def user(self):
        return self.__user