class Query:
    class Question:
        def __init__(self, question: str):
            self.question = question

        def builder(self, db_details: str):
            return self.question % db_details

    class Lang:
        PL = "PL"
        EN = "EN"

        @staticmethod
        def create_from(lang: str):
            if lang.lower() == Query.Lang.PL.lower():
                return Query.Lang.PL
            elif lang.lower() == Query.Lang.EN.lower():
                return Query.Lang.EN
            else:
                raise Exception("Invalid language")

    TABLES_PL = Question(
        "Wygeneruj opis dla tabel w relacyjnej bazie danych o takiej strukturze JSON: %s Opis powinien próbować odgadnąć semantyke oraz relacje pomiędzy tabelami. Opis tabeli powinien zawierać minimalnie 3 zdania, maksymalnie 5. Wyniki zwróć w formacie JSON w postaci: {\"table_name\": \"description\"}")
    TABLES_EN = Question(
        "Generate a description for a table with such a structure: %s The description should try to guess the semantics and relationships between tables")

    VIEWS_PL = Question(
        "Wygeneruj opis dla widoków w relacyjnej bazie danych o takiej strukturze JSON: %s . Opis widoku powinien zawierać minimalnie 3 zdania, maksymalnie 5. Wyniki zwróć w formacie JSON w postaci: {\"view_name\": \"description\"}")
    VIEWS_EN = Question("")