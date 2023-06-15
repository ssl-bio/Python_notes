# Random walk
from random import choice


class RandomWalk():
    """A class to generate random walks

    """
    def __init__(self, num_points=5000):
        """Attributes of a walk
        """
        # super(RandomWalk, self).__init__()
        self.num_points = num_points

        # Walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, max_step):
        """Decide the direction and distance
        """
        i_direction = choice([1, -1])  # choose either 1 or -1
        i_distance = choice(list(range(0, max_step+1)))
        return i_direction * i_distance

    def fill_walk(self):
        """Generate the points in the walk
        """
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far
            x_step = self.get_step(4)
            y_step = self.get_step(4)

            # Ignore steps that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def fill_walk_v2(self):
        """Generate the points in the walk
        """
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far
            x_step = self.get_step(16)
            y_step = self.get_step(4)

            # Ignore steps that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
