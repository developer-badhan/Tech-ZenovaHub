from enum import Enum

# Success messages for user-related actions

class SuccessMessage(Enum):
    S0001 = 'User successfully created.'
    S0002 = 'User successfully updated.'
    S0003 = 'User successfully deleted.'
    S0004 = 'Profile successfully created.'
    S0005 = 'Profile successfully updated.'
    S0006 = 'Profile successfully deleted.'
    S0007 = 'Order successfully created.'
    S0008 = 'Order successfully updated.'
    S0009 = 'Order successfully deleted.'
    S0010 = 'Payment successfully processed.'
    S0011 = 'Payment successfully refunded.'
    S0012 = 'Item successfully added to cart.'
    S0013 = 'Item successfully removed from cart.'
    S0014 = 'Cart successfully cleared.'
    S0015 = 'Checkout successfully completed.'
    S0016 = 'Subscription successfully created.'
    S0017 = 'Subscription successfully updated.'
    S0018 = 'Subscription successfully cancelled.'
    S0019 = 'Notification successfully sent.'
    S0020 = 'Settings successfully updated.'

    def __str__(self):
        return self.value   