class Entry:

    # Initialiseer een entry met de gegeven parameters.
    def __init__(self, day=1, start=0, end=23, location="", description=""):
        self._description = description
        self._day = day
        self._start = start
        self._end = end
        self._location = location

    def is_equal(self,other):
        pass

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_day(self):
        return self._day

    def get_start_slot(self):
        return self._start

    def get_end_slot(self):
        return self._end

    def is_valid_slot(self, start):
        return 0 < start < 24

    def occupies_slot(self, time):
        return self._start <= time <= self._end

    def overlaps_with(self, activity):
        if activity.get_day() != self._day:
            return False

        return self._start <= activity.get_start_slot() <= self._end or self._start <= activity.get_end_slot() <= self._end \
               or (activity.get_start_slot() <= self._start and activity.get_end_slot() >= self._end)

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location

    def is_equal(self, activity):
        return activity.get_day() == self._day and activity.get_location() == self._location and activity.get_description() == self._description \
            and activity.get_start_slot() == self._start and activity.get_end_slot() == self._end

    #OVERLOADED OPERATIONS

    def __eq__(self, other):
        """
        Deze methode zorgt ervoor dat == kan gebruikt worden op 2 entry objecten bijvoorbeeld: entry1 == entry2.
        Om deze methode te laten werken moet eerst de is_equal methode geïmplementeerd worden.
        """
        return self.is_equal(other)

    def __ne__(self,other):
        return not self.is_equal(other)

    def __str__(self):
        """
        Return the textual representation of self.
        """
        string_voorstelling = self.get_description() + \
                              " on " + str(self.get_day()) + \
                              " from " + str(self.get_start_slot()) + \
                              " until " + str(self.get_end_slot())
        if len(self.get_location()) != 0:
            return string_voorstelling + " at " + self.get_location()
        return string_voorstelling


class Agenda:
    """
        deze methode zorgt ervoor dat je str() kan oproepen met een agenda object.
        Dit geeft een string terug die je kan printen.
    """
    def __init__(self):
        self._entries = []

    def get_entries(self):
        return self._entries

    def add_entry(self, entry):
        for el in self._entries:
            if el.overlaps_with(entry):
                return False

        self._entries.append(entry)
        return True

    def get_entries_on_day(self, day):
        filtered = list(filter(lambda el: el.get_day() == day, self._entries))
        return filtered

    def remove_entry(self, entry):
        if entry in self._entries:
            self._entries.remove(entry)


    def __str__(self):
        """
            Returns a chronologically ordered textual representation of the agenda.
        """
        string = ''
        for e in sorted(self.get_entries(), key=lambda entry: (entry.get_day(), entry.get_start_slot())):
            string += str(e) + '\n'
        return string


# STEP 1
entry = Entry(description="Methodiek van de informatica")
assert entry.get_description() == "Methodiek van de informatica"

# STEP 2
entry = Entry(day=200)
assert entry.get_day() == 200

# STEP 3
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert meeting.get_description() == "Dinner"
assert meeting.get_day() == 133
assert meeting.get_start_slot() == 18
assert meeting.get_end_slot() == 22

# STEP 4
meeting = Entry(description="Dinner", day=133, start=18, end=22)
for slot in range(0, 18):
    assert not meeting.occupies_slot(slot)
for slot in range(18, 23):
    assert meeting.occupies_slot(slot)
assert not meeting.occupies_slot(23)
meeting = Entry(description="Study", day=42, start=9, end=12)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
assert not meeting.overlaps_with(meeting2)
meeting2 = Entry(description="Lunch", day=42, start=12, end=13)
assert meeting.overlaps_with(meeting2)
meeting2 = Entry(description="Lunch", day=42, start=13, end=14)
assert not meeting.overlaps_with(meeting2)

# STEP 5
agenda = Agenda()
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert agenda.add_entry(meeting)
assert not agenda.add_entry(meeting)
assert len(agenda.get_entries()) == 1

agenda = Agenda()
meeting = Entry(description="Dinner", day=133, start=18, end=22)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
meeting3 = Entry(description="Breakfast", day=41, start=8, end=8)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
agenda.add_entry(meeting3)
assert len(agenda.get_entries_on_day(133)) == 1
assert len(agenda.get_entries_on_day(41)) == 2

# STEP 6
meeting = Entry()
meeting2 = Entry()
assert meeting == meeting2
assert not meeting != meeting2
meeting = Entry(description="Study", day=42, start=9, end=12)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
assert meeting != meeting2
assert not meeting == meeting2

# STEP 7
agenda = Agenda()
meeting = Entry(description="Breakfast", day=41, start=8, end=8)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
meeting3 = Entry(description="Lunch", day=41, start=12, end=13)
agenda.remove_entry(meeting3)
assert len(agenda.get_entries()) == 1
meeting4 = Entry(description="Dinner", day=133, start=18, end=22)
agenda.remove_entry(meeting4)
assert len(agenda.get_entries()) == 1

# STEP 8
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert meeting.get_location() == ""
meeting.set_location("De Volle Pollepel")
assert meeting.get_location() == "De Volle Pollepel"
meeting.set_location("")
assert meeting.get_location() == ""

# STEP 9
meeting = Entry(description="Dinner", day=133, start=18, end=22)
assert str(meeting) == "Dinner on 133 from 18 until 22"
meeting.set_location("De Volle Pollepel")
assert str(meeting) == "Dinner on 133 from 18 until 22 at De Volle Pollepel"

# STEP 10
agenda = Agenda()
meeting = Entry(description="Dinner", day=133, start=18, end=22)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
meeting3 = Entry(description="Breakfast", day=41, start=8, end=8)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
agenda.add_entry(meeting3)
a = str(agenda)
print(str(agenda))
assert str(agenda) == "Breakfast on 41 from 8 until 8\nLunch on 41 from 12 until 13\nDinner on 133 from 18 until 22\n"

print("OK.")
