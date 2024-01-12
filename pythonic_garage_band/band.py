class Band:
    instances = []
    
    def __init__(self, name, members):

        """
        Initializes a Band object with the given name and members.

        Parameters:
        - name (str): The name of the band.
        - members (list): A list of members in the band.

        Note:
        The Band object is added to the 'instances' class variable.
        """
              
        self.name = name
        self.members = members
        Band.instances.append(self)

    @classmethod
    def to_list(cls):
        """
        Returns a list of all Band instances.

        Returns:
        list: A list containing all Band instances.
        """
        return cls.instances

    def play_solos(self):
        """
        Calls the play_solo method for each band member and returns a list of solos.

        Returns:
        list: A list of solos played by each band member.
        """
        return [member.play_solo() for member in self.members]

class Musician:
    def __init__(self, name):
        """
        Initializes a Musician object with the given name.

        Parameters:
        - name (str): The name of the musician.
        """
        self.name = name

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"