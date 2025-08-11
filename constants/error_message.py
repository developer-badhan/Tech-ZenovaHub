from enum import Enum

# Error messages for user-related actions

class ErrorMessage(Enum):
    E0001 = 'User creation failed.'
    E0002 = 'User update failed.'
    E0003 = 'User deletion failed.'
    E0004 = 'Profile creation failed.'
    E0005 = 'Profile update failed.'
    E0006 = 'Profile deletion failed.'
    E0007 = 'Order creation failed.'
    E0008 = 'Order update failed.'
    E0009 = 'Order deletion failed.'
    E0010 = 'Payment processing failed.'
    E0011 = 'Payment refund failed.'
    E0012 = 'Item addition to cart failed.'
    E0013 = 'Item removal from cart failed.'
    E0014 = 'Cart clearing failed.'
    E0015 = 'Checkout process failed.'
    E0016 = 'Subscription creation failed.'
    E0017 = 'Subscription update failed.'
    E0018 = 'Subscription cancellation failed.'
    E0019 = 'Notification sending failed.'
    E0020 = 'Settings update failed.'

    def __str__(self):
        return self.value