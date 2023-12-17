from encap_wild_cap_zoo.animal import Animal
from encap_wild_cap_zoo.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return f"Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return f"Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return f"Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if self.__budget < total_salaries:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care

        if self.__budget < total_money_for_care:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_entity_str(self.animals, 'Lion')
        result += self.__build_entity_str(self.animals, 'Tiger')
        result += self.__build_entity_str(self.animals, 'Cheetah')

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__build_entity_str(self.workers, 'Keeper')
        result += self.__build_entity_str(self.workers, 'Caretaker')
        result += self.__build_entity_str(self.workers, 'Vet')

        return result.strip()

    def __build_entity_str(self, entities, entity_type):
        counter = 0
        result = ''

        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + "\n"

        return f"----- {counter} {entity_type}s:\n" + result





