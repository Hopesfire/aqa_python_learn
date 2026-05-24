class Lead:
    def __init__(self, name):
        self.name = name

    # def change_name(self, new_name):
    #     self.name = new_name

def change_name(lead, new_name):
    lead.name = new_name

lead_ex = Lead("Ivan")
print(lead_ex.name)

# lead_ex.change_name("Michael")
change_name(lead_ex, "Michael")
print(lead_ex.name)