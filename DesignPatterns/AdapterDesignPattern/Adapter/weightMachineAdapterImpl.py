from Adapter.weightMachineAdapter import WeightMachineAdapter
from Adaptee.weightMachine import WeightMachine

class WeightMachineAdapterImpl(WeightMachineAdapter):
    def __init__(self, weight_machine: WeightMachine) -> None:
        self.weight_machine = weight_machine

    def get_weight_in_kg(self):
        weight_in_pound = self.weight_machine.get_weight_in_pound()
        weight_in_kg = weight_in_pound * .45
        return weight_in_kg