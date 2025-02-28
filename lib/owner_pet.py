class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exoctic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self._owner = None
        self.owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")
        if self._owner is not None:
            self._owner._pets.remove(self)
        self._owner = owner
        if owner is not None:
            owner._pets.append(self)



class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):  # Remove quotes around Pet

          raise Exception("The pet must be an instance of Pet")
        if pet.owner is not None:
            pet.owner._pets.remove(pet)
        pet.owner = self
        if pet not in self._pets:
         self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self._owner = None  
        self.owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")
        if self._owner is not None:
            self._owner._pets.remove(self)
        self._owner = owner
        if owner is not None:
            owner._pets.append(self)