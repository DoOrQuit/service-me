from io import BufferedRandom
from pyexpat import model
from sys import _enablelegacywindowsfsencoding


class Service_me():
    def __init__(self, brand, model, engine, transmition, mileage):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.transmition = transmition
        self.mileage = mileage