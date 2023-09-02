"""CP1404/CP5632 Practical
Project class """


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"Name: {self.name}, Start Date: {self.start_date}, Priority: {self.priority}," \
               f" Cost Estimate: ${self.cost_estimate:.2f}, Percent Complete: {self.percent_complete}%"