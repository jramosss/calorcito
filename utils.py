from datetime import datetime

Y = datetime.now().year
SUMMER_DAY = datetime(Y,12,21).date().timetuple().tm_yday
AUTUMN_DAY = datetime(Y,3,21).date().timetuple().tm_yday
WINTER_DAY = datetime(Y,6,21).date().timetuple().tm_yday
SPRING_DAY = datetime(Y,9,21).date().timetuple().tm_yday

class StationsSTR:
    def __init__(self) -> None:
        self.SUMMER = "Summer"
        self.AUTUMN = "Autumn"
        self.WINTER = "Winter"
        self.SPRING = "Spring"


class Stations:
    def __init__(self) -> None:
        self.AUTUMN = range(AUTUMN_DAY,WINTER_DAY)
        self.WINTER = range(WINTER_DAY,SPRING_DAY)
        self.SPRING = range(SPRING_DAY,SUMMER_DAY)

def checkTime ():
    today = datetime.now().timetuple().tm_yday
    stations = Stations()
    st = StationsSTR()
        
    if today in stations.SPRING:
        return st.SPRING
    elif today in stations.AUTUMN:
        return st.AUTUMN
    elif today in stations.WINTER:
        return st.WINTER
    else:
        return st.SUMMER


def leftingDaysForSummer ():
    today_number = datetime.now().timetuple().tm_yday
    today = datetime.now().date()

    st = Stations()
    summer_date = datetime(Y,12,21).date()
    if not (today_number in st.SPRING or today_number in st.WINTER or today_number in st.AUTUMN):
        return None
    else:
        return int(str(summer_date - today).split(' ')[0])
