"""goalsaver Models."""

from django.db import models
import datetime


class Goal(models.Model):
    """Goals store the goals a user has saved, including the user id of the user, and the date, amount, and name for
    the goal.
    """
    user_id = models.TextField()
    end_date = models.DateField()
    goal_amount = models.FloatField()
    amount_saved_to_date = models.FloatField()
    name = models.TextField()
    description = models.TextField()
    thermometer_color = models.TextField()
    is_current_goal = models.BooleanField()
    is_completed = models.BooleanField()

    def __str__(self):
        """Returns str.

        >>> time = datetime.date(2018, 5, 5)
        >>> str(Goal(user_id='123', end_date=time, goal_amount=532.31, amount_saved_to_date=12.34,\
        name='Vacation to Thailand', description='$100 for airfare, $200 for housing, $232.31 for expenses',\
        thermometer_color='blue', is_current_goal=True, is_completed=False))
        'Goal(123, 2018-05-05, 532.31, 12.34, 'Vacation to Thailand', '$100 for airfare, $200 for housing, $232.31 for \
expenses', 'blue', True, False)'
        """
        return 'Goal({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.user_id, self.end_date, self.goal_amount,
                                                                 self.amount_saved_to_date, self.name, self.description,
                                                                 self.thermometer_color, self.is_current_goal,
                                                                 self.is_completed)

    def __repr__(self):
        """Returns repr.

        >>> time = datetime.date(2018, 5, 5)
        >>> repr(Goal(user_id='123', end_date=time, goal_amount=532.31, amount_saved_to_date=12.34,\
        name='Vacation to Thailand', description='$100 for airfare, $200 for housing, $232.31 for expenses',\
        thermometer_color='blue', is_current_goal=True, is_completed=False))
        'Goal(user_id='123', end_date=2018-05-05, goal_amount=532.31, amount_saved_to_date=12.34, \
name='Vacation to Thailand', description='$100 for airfare, $200 for housing, $232.31 for expenses', thermometer_color=\
'blue', is_current_goal=True, is_completed=False)'
        """
        return 'Goal(user_id={!r}, end_date={!r}, goal_amount={!r}, amount_saved_to_date={!r}, name={!r}, ' \
               'description={!r}, thermometer_color={!r}, is_current_goal={!r}, is_completed={!r})'.\
            format(self.user_id, self.end_date, self.goal_amount, self.amount_saved_to_date, self.name,
                   self.description, self.thermometer_color, self.is_current_goal, self.is_completed)
