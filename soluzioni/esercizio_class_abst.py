# Soluzione esercizio classi abstract

class Person:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def presentati(self):
        return f"Ciao, sono {self.nome} {self.cognome}, ho {self.eta} anni."


class Studente(Person):
    def __init__(self, nome, cognome, eta, corso):
        super().__init__(nome, cognome, eta)
        self.corso = corso

    def studia(self):
        return f"{self.nome} studia {self.corso}."


class Dipendente(Person):
    def __init__(self, nome, cognome, eta, stipendio):
        super().__init__(nome, cognome, eta)
        self.stipendio = stipendio

    def lavora(self):
        return f"{self.nome} lavora con stipendio di {self.stipendio} euro."


class Docente(Dipendente):
    def __init__(self, nome, cognome, eta, stipendio, materia):
        super().__init__(nome, cognome, eta, stipendio)
        self.materia = materia

    def insegna(self):
        return f"{self.nome} insegna {self.materia}."


class Freelance(Dipendente):
    def __init__(self, nome, cognome, eta, stipendio, progetto):
        super().__init__(nome, cognome, eta, stipendio)
        self.progetto = progetto

    def lavora(self):
        return f"{self.nome} lavora come freelance sul progetto {self.progetto}."


class Freelance(Dipendente):
    def __init__(self, nome, cognome, eta, stipendio, progetto):
        super().__init__(nome, cognome, eta, stipendio)
        self.progetto = progetto

    def lavora(self):
        return f"{self.nome} lavora come freelance sul progetto {self.progetto}."


person1 = Person("Gege", "Xia", 30)
studente1 = Studente("Luca", "Rossi", 22, "Python")
dipendente1 = Dipendente("Marco", "Verdi", 40, 3500)
docente1 = Docente("Gian", "Bianchi", 35, 3000, "Matematica")
freelance1 = Freelance("Sara", "Neri", 29, 2500, "Sito web")


print(person1.presentati())
print(studente1.studia())
print(dipendente1.lavora())
print(docente1.insegna())
print(freelance1.lavora())
