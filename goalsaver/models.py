"""goalsaver Models."""

from django.db import models
import datetime

class Goal(models.Model):
    """Goals store the goals a user has saved, including the user id of the user, and the date, amount, and name for
    the goal.
    """
    user_id = models.TextField()
    date = models.DateField()
    amount = models.FloatField()
    name = models.TextField()

    def __str__(self):
        """Returns str.

        >>> time = datetime.date(2017, 5, 5)
        >>> str(Goal(user_id='123', date=time, amount=532.31, name='Vacation to Thailand'))
        'Goal(123, 2017-05-05, 532.31, 'Vacation to Thailand')'
        """
        return 'Goal({}, {}, {}, {})'.format(self.user_id, self.date, self.amount, self.name)

    def __repr__(self):
        """Returns repr.

        >>> time = datetime.date(2017, 5, 5)
        >>> repr(Goal(user_id='123', date=time, amount=532.31, name='Vacation to Thailand'))
        "Goal(user_id='123', date=datetime.date(2017-05-05), amount=532.31, name='Vacation to Thailand)"
        """
        return 'Goal(user_id={!r}, date={!r}, amount={!r}, name={!r})'.format(self.user_id, self.date, self.amount,
                                                                              self.name)
