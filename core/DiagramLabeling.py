class DiagramLabeling(object):

    def __init__(self):
        self.title_dict = {'Weight': 'Body Weight', 'Fat': 'Body Fat', 'Bench Press': 'Bench Press', 'Rowing': 'Rowing',
                      'Chin-up': 'Chin-up', 'Dips': 'Dips', 'Shoulder Press': 'Shoulder Press',
                      'Bizeps Curls': 'Bizeps Curls', 'Trizeps Curls': 'Trizeps Curls', 'Deadlift': 'Deadlift',
                      'Leg Press': 'Leg Press', 'Leg Extension': 'Leg Extension', 'Leg Curl': 'Leg Curl'}

        self.y_label_dict = {'Weight': 'Weight [kg]', 'Fat': 'Body Fat [%]', 'Bench Press': 'Weight [kg]',
                        'Rowing': 'Weight [kg]', 'Chin-up': 'Weight [kg]', 'Dips': 'Weight [kg]',
                        'Shoulder Press': 'Weight [kg]', 'Bizeps Curls': 'Weight [kg]', 'Trizeps Curls': 'Weight [kg]',
                        'Deadlift': 'Weight [kg]', 'Leg Press': 'Weight [kg]', 'Leg Extension': 'Weight [kg]',
                        'Leg Curl': 'Weight [kg]'}

    def get_labels(self, header):
        title = self.title_dict[header]
        y_label = self.y_label_dict[header]

        return title, y_label