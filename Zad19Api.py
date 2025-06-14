class APIError(Exception):
    def __init__(self, message, code=400):
        super().__init__(message)
        self.code=code

    @staticmethod
    def from_response(response):
        msg = response.get("error", "Unknown error")
        code = response.get ("code", 500)
        return APIError (msg, code=code)


#symulujemy odpowiedz z serwera

response = {'error': "Brak tokena JWT", "code":401}
raise APIError.from_response(response)