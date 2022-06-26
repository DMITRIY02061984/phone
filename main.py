
class phone:
    def __init__(self, name, nokia, model, year):
        self.name = name
        self.brand = nokia
        self.model = model
        self.issue_year = year

# не работает, еще раз повторить про класссы и объекты
    def receive_call(self):
        return f'Звонит {self.name}'

    def get_info (self):
        return (self.brand, self.model, self.issue_year)

    def str(self):
        return f'Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}'


ph = phone('name', 'nokia', '3310', '2000')
print(ph.receive_call())
print(ph.get_info())
print(ph.str())