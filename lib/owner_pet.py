class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of pets that belong to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner after type checking"""
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of the owner's pets by name"""
        return sorted(self.pets(), key=lambda p: p.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.pet_type = pet_type

        self.owner = None
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner.")
            self.owner = owner

        Pet.all.append(self)
