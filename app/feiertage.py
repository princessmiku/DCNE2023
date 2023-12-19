"""
Hier findet man alle Registrierten feiertage in Deutschland mit eingetragenen Bundesland und
ggf einer kleinen Beschreibung (Quelle ist ProSieben Galileo bisher)

Die Liste der Bundesländer findet man separat nochmal in der 'Bundesländer.md'
"""
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

_current_year = datetime.now().year

_bundesland_liste = [
    'Baden-Württemberg',
    'Bayern',
    'Berlin',
    'Brandenburg',
    'Bremen',
    'Hamburg',
    'Hessen',
    'Mecklenburg-Vorpommern',
    'Niedersachsen',
    'Nordrhein-Westfalen',
    'Rheinland-Pfalz',
    'Saarland',
    'Sachsen',
    'Sachsen-Anhalt',
    'Schleswig-Holstein',
    'Thüringen'
]


def calc_ostern(year: int) -> datetime:
    """
    Hiermit kann man die Osterfeiertage berechnen, diese basieren auf einer bestimmten Formel,
    welche man Nachbilden kann.\n
    Alle Osterfeiertage haben einen bestimmten abstand zu Ostersonntag, welcher hier berechnet wird.\n
    Mehr informationen unter https://web.de/magazine/wissen/geschichte/datum-feiertage-ostern-berechnen-32192316
    :param year: das Jahr in dem Ostern stattfindet
    :return:
    """
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((a * 19) + 24) % 30
    e = ((b * 2) + (c * 4) + (d * 6) + 5) % 7
    ostern_day = 22 + d + e
    if ostern_day > 31:
        ostern_day = ostern_day - 31
        return datetime(year, 4, ostern_day)
    return datetime(year, 3, ostern_day)


class Feiertag(ABC):

    def __init__(self, name: str, bundesland_liste: list = None):
        self._name = name
        self._description = "Keine Vorhanden"
        if bundesland_liste is None:
            bundesland_liste = []
        if len(bundesland_liste) > 0:
            for bundesland in bundesland_liste:
                if bundesland not in _bundesland_liste:
                    raise ValueError(f"Bundesland not found: {bundesland}. Check the bundesland list.")
        self._bundesland_liste = bundesland_liste.copy()
        self._current_year_date = self.date(_current_year)
        self._next_year_date = self.date(_current_year + 1)

    @property
    def current_year_date(self) -> datetime:
        return self._current_year_date

    @property
    def next_year_date(self) -> datetime:
        return self._next_year_date

    @property
    def name(self):
        return self._name

    @property
    def bundesland_liste(self):
        return self._bundesland_liste

    @property
    def is_global(self):
        return len(self._bundesland_liste) > 0

    def is_for_me(self, bundesland: str):
        if len(self._bundesland_liste) == 0:
            return True
        return bundesland in self._bundesland_liste

    @abstractmethod
    def date(self, year: int) -> datetime:
        pass


class Neujahr_F(Feiertag):

    def __init__(self):
        super().__init__('Neujahr')

    def date(self, year: int) -> datetime:
        return datetime(year, 1, 1)


class HeiligeDreiKoenige_F(Feiertag):

    def __init__(self):
        super().__init__('Heilige Drei Könige')
        self._description = ("Am 6. Januar, dem Dreikönigstag, wird den drei Weisen Caspar, Melchior und Balthasar "
                             "gedacht, welche in der Bibel einem Stern folgend nach der Geburt Jesu Christi nach "
                             "Betlehem gekommen waren. Traditionell segnen an diesem Tag in den katholischen "
                             "Gemeinden Sternsinger:innen Häuser und deren Bewohner:innen, indem sie mit Kreide die "
                             "Kürzel der drei Weisen sowie die Jahreszahl an die Haustüren schreiben. Sie sammeln "
                             "damit Spenden für Kinder in Not.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return datetime(year, 1, 6)


class InternationalerFrauentag_F(Feiertag):

    def __init__(self):
        super().__init__('Internationaler Frauentag', ['Berlin', 'Mecklenburg-Vorpommern'])
        self._description = ("Der 8. März ist der Internationale Frauentag. An ihm wird seit über 100 Jahren weltweit "
                             "für Frauenrechte, Gleichberechtigung und Antidiskriminierung demonstriert. 2019 wurde "
                             "der 8. März in Berlin als weiterer gesetzlicher Feiertag eingeführt, "
                             "weil die Hauptstadt bis dahin bundesweit die wenigsten Feiertage hatte."
                             "\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return datetime(year, 3, 8)


class Karfreitag_F(Feiertag):

    def __init__(self):
        super().__init__('Karfreitag', [])
        self._description = ("Am Karfreitag gedenken Christ:innen der Kreuzigung Jesu, seines Leidens und seines "
                             "Todes. Nach ihrem Glauben nahm Jesus Christus durch seinen Tod all ihre Sünden und "
                             "Schuld auf sich. Gottesdienste beginnen in der Regel um 15 Uhr - nach dem Neuen "
                             "Testament der Todesstunde Jesu Christi. Traditionell finden in Italien und Spanien, "
                             "aber auch in einigen Regionen in Deutschland am Karfreitag Prozessionen statt. In "
                             "Jerusalem beten Gläubige entlang des Kreuzwegs durch die Via Dolorosa. Am Karfreitag "
                             "sollen die Menschen innehalten, weswegen an ihm bei uns auch ein Tanzverbot gilt."
                             "\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return calc_ostern(year) - timedelta(days=2)


class Ostersonntag_F(Feiertag):

    def __init__(self):
        super().__init__('Ostersonntag', ['Brandenburg'])
        self._description = ("Am Ostersonntag beginnt das eigentliche Osterfest. Nach dem Neuen Testament ist Jesus an "
                             "diesem Tag von den Toten auferstanden, damit bildet er den höchsten Feiertag für "
                             "christliche Gläubige.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return calc_ostern(year)


class Ostermontag_F(Feiertag):

    def __init__(self):
        super().__init__('Ostermontag')
        self._description = ("Der Ostermontag erinnert Christ:innen daran, dass laut ihrem Glauben Jesus Christus in "
                             "Emmaus, etwa 30 Kilometer westlich von Jerusalem, zwei Jüngern erschienen ist. Diese "
                             "waren nach der Kreuzigung Jesu gerade aus Jerusalem auf dem Weg zurück in ihr Dorf, "
                             "als sie einem Mann begegneten. Während sie ihr Brot mit ihm teilten, erkannten sie in "
                             "ihm den auferstandenen Jesus Christus, doch er verschwand vor ihren Augen. Sofort "
                             "kehrten die beiden nach Jerusalem zurück, um hier die Frohe Botschaft der Auferstehung "
                             "zu verbreiten.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return calc_ostern(year)


class TagDerArbeit_F(Feiertag):

    def __init__(self):
        super().__init__('Tag der Arbeit')
        self._description = ("Der Tag der Arbeit geht auf einen Arbeiterstreik im Jahr 1886 in den USA zurück. Seitdem "
                             "wird am 1. Mai weltweit für Arbeitnehmerrechte demonstriert.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return datetime(year, 5, 1)


class ChristiHimmelfahrt_F(Feiertag):

    def __init__(self):
        super().__init__('Christi Himmelfahrt')
        self._description = ('An Christi Himmelfahrt ist Jesus dem christlichen Glauben nach als Sohn Gottes von der '
                             'Erde zu seinem Vater in den Himmel zurückgekehrt. Christi Himmelfahrt wird genau 39 '
                             'Tage nach dem Ostersonntag gefeiert. Deshalb fällt es immer auf einen Donnerstag. Zum '
                             '"Vatertag" mit seiner Tradition der "Herrentagspartie" wurde Christi Himmelfahrt '
                             'vermutlich Ende des 19. Jahrhunderts.\nQuelle: ProSieben')

    def date(self, year: int) -> datetime:
        return calc_ostern(year) + timedelta(days=40)


class Pingstsonntag_F(Feiertag):

    def __init__(self):
        super().__init__('Pfingstsonntag', ['Brandenburg'])
        self._description = ("Das Pfingstfest, zehn Tage nach Christi Himmelfahrt und 50 Tage nach Ostern, bildet für "
                             "Christ:innen das offizielle Ende der Osterzeit. Der Bibel nach schickte Jesus an "
                             "Pfingsten den Heiligen Geist zu den Menschen auf die Erde. Ausgestattet mit dieser "
                             "göttlichen Kraft konnten sie dann in der ganzen Welt seine Botschaft verkünden - die "
                             "Geburtsstunde der Kirche.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return calc_ostern(year) + timedelta(days=50)


class Pingstmontag_F(Feiertag):

    def __init__(self):
        super().__init__('Pfingstmontag')

    def date(self, year: int) -> datetime:
        return calc_ostern(year) + timedelta(days=51)


class Fronleichnam_F(Feiertag):

    def __init__(self):
        super().__init__('Fronleichnam', [
            'Baden-Württemberg',
            'Bayern',
            'Hessen',
            'Nordrhein-Westfalen',
            'Rheinland-Pfalz',
            'Saarland'
        ])
        self._description = ('Am zweiten Donnerstag nach Pfingsten feiern katholische Christ:innen Fronleichnam. Beim '
                             '"Fest des heiligsten Leibes und Blutes Christi" danken sie der Gegenwart von Jesus '
                             'Christus in Form von Brot und Wein und erinnern gleichzeitig an das Letzte Abendmahl. '
                             'Durch den Verzehr der Hostie, einer kleinen Oblate, die den Leib Christi symbolisiert, '
                             'und Wein als Symbol für sein Blut fühlen sich die Gläubigen Jesus besonders nah.'
                             '\nQuelle: ProSieben')

    def date(self, year: int) -> datetime:
        return calc_ostern(year) + timedelta(days=61)


class MariaHimmelfahrt_F(Feiertag):

    def __init__(self):
        super().__init__('Mariä Himmelfahrt', ['Saarland'])
        self._description = ("An Mariä Himmelfahrt am 15. August erinnern Gläubige daran, dass Jesus Christus der "
                             "Bibel nach seine Mutter Maria nach deren Tod zu sich in den Himmel gerufen hat."
                             "\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return datetime(year, 8, 15)


class Weltkindertag_F(Feiertag):

    def __init__(self):
        super().__init__('Weltkindertag', ['Thüringen'])
        self._description = ("Am Weltkindertag stehen die Rechte und der Schutz von Kindern auf der ganzen Welt im "
                             "Fokus. Kinderrechts-Organisationen wie UNICEF veranstalten jedes Jahr am 20. September "
                             "Aktionen, Kundgebungen und Feste. Thüringen will mit dem 2019 eingeführten Feiertag "
                             "Kinder und Familien würdigen.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return datetime(year, 9, 20)


class TagDerDeutschenEinheit_F(Feiertag):

    def __init__(self):
        super().__init__('Tag der Deutschen Einheit')
        self._description = ("Am 3. Oktober 1990 trat die DDR offiziell der Bundesrepublik bei, wodurch die "
                             "Wiedervereinigung der beiden deutschen Staaten besiegelt wurde. Seitdem ist dieser Tag "
                             "unser Nationalfeiertag. In der BRD war bis 1990 der 17. Juni Nationalfeiertag - zum "
                             "Gedenken an den Volksaufstand in der DDR 1953. In der DDR war bis 1989 der 7. Oktober "
                             "der Tag der Republik.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return datetime(year, 10, 3)


class Reformationstag_F(Feiertag):

    def __init__(self):
        super().__init__('Reformationstag', [
            "Brandenburg",
            "Bremen",
            "Hamburg",
            "Hessen",
            "Mecklenburg-Vorpommern",
            "Niedersachsen",
            "Sachsen",
            "Sachsen-Anhalt",
            "Schleswig-Holstein",
            "Thüringen"
        ])

    def date(self, year: int) -> datetime:
        return datetime(year, 10, 31)


class Allerheiligen_F(Feiertag):

    def __init__(self):
        super().__init__('Allerheiligen', [
            "Brandenburg",
            "Bremen",
            "Hamburg",
            "Hessen",
            "Mecklenburg-Vorpommern",
            "Niedersachsen",
            "Sachsen",
            "Sachsen-Anhalt",
            "Schleswig-Holstein",
            "Thüringen"
        ])
        self._description = ("Allerheiligen ist ein katholischer Feiertag am 1. November. An ihm wird der Heiligen, "
                             "verdienten Christ:innen und Toten gedacht. Traditionell werden an diesem Tag auch die "
                             "Gräber geschmückt und für den Winter mit Tannenzweigen abgedeckt.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        return datetime(year, 11, 1)


class BusUndBetTag_F(Feiertag):

    def __init__(self):
        super().__init__('Buß- und Bettag', ['Sachsen'])
        self._description = ("Der Buß- und Bettag soll Protestant:innen Besinnung und Neuorientierung schenken. Er "
                             "war bis 1995 ein bundesweiter Feiertag. Dann wurde er abgeschafft, um mit diesem "
                             "weiteren Arbeitstag Teile der neu eingeführten Pflegeversicherung finanzieren zu "
                             "können. Nur in Sachsen blieb der Tag ein Feiertag. Dafür müssen die Menschen im "
                             "Freistaat seitdem 0,5 Prozent ihres Bruttolohns mehr in die Pflegeversicherung "
                             "einzahlen als alle anderen Deutschen.\nQuelle: ProSieben")

    def date(self, year: int) -> datetime:
        last_advent = datetime(year=year, month=12, day=24)
        while last_advent.strftime("%A") != 'Sunday':
            last_advent -= timedelta(days=1)
        busbettag = last_advent - timedelta(days=32)
        return busbettag


class Weihnachtstag_F(Feiertag):

    def __init__(self):
        super().__init__('Weihnachtstag')

    def date(self, year: int) -> datetime:
        return datetime(year, 12, 25)


class ZweiterWeihnachtstag_F(Feiertag):

    def __init__(self):
        super().__init__('Zweiter Weihnachtstag')

    def date(self, year: int) -> datetime:
        return datetime(year, 12, 26)


def get_feiertage_as_list():
    """
    Die Funktion initialisiert alle Feiertage und gibt diese als liste zurück.
    :return:
    """
    return [
        Neujahr_F(),
        HeiligeDreiKoenige_F(),
        InternationalerFrauentag_F(),
        Karfreitag_F(),
        Ostersonntag_F(),
        Ostermontag_F(),
        TagDerArbeit_F(),
        ChristiHimmelfahrt_F(),
        Pingstsonntag_F(),
        Pingstmontag_F(),
        Fronleichnam_F(),
        MariaHimmelfahrt_F(),
        Weltkindertag_F(),
        TagDerDeutschenEinheit_F(),
        Reformationstag_F(),
        Allerheiligen_F(),
        BusUndBetTag_F(),
        Weihnachtstag_F(),
        ZweiterWeihnachtstag_F()
    ]


if __name__ == '__main__':
    pri_str = ""
    for feiertag in get_feiertage_as_list():
        if not feiertag.is_for_me('Niedersachsen'):
            continue
        pri_str += f"{feiertag.name:26}: {feiertag.next_year_date.strftime('%d.%m.%Y')}\n"
    print(pri_str)
