class NotFund(Exception):
    def __init__(self,resource, resource_id):
        msg =f"{resource} o ID {resource_id} nie znaleziono"
        super().__init__(msg)
        self.resource= resource
        self.resource_id=resource_id
    @classmethod
    def user (cls,user_id):
        return cls("Uzytkownik", user_id)
    @staticmethod
    def for_any(resource, resource_id):
        return NotFund(resource,resource_id)


#raise NotFund.user(7)
"""
Traceback (most recent call last):
  File "C:\Szkolenia\2025-05 BotCampPython\2025-06-14_zajecia\Zad20API.py", line 15, in <module>
    raise NotFund.user(7)
__main__.NotFund: Uzytkownik o ID 7 nie znaleziono
"""