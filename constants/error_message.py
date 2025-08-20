# from enum import Enum

# # Error messages for user-related actions

# class ErrorMessage(Enum):
#     E0001 = 'User creation failed.'
#     E0002 = 'User update failed.'
#     E0003 = 'User deletion failed.'
#     E0004 = 'Profile creation failed.'
#     E0005 = 'Profile update failed.'
#     E0006 = 'Profile deletion failed.'
#     E0007 = 'Order creation failed.'
#     E0008 = 'Order update failed.'
#     E0009 = 'Order deletion failed.'
#     E0010 = 'Payment processing failed.'
#     E0011 = 'Payment refund failed.'
#     E0012 = 'Item addition to cart failed.'
#     E0013 = 'Item removal from cart failed.'
#     E0014 = 'Cart clearing failed.'
#     E0015 = 'Checkout process failed.'
#     E0016 = 'Subscription creation failed.'
#     E0017 = 'Subscription update failed.'
#     E0018 = 'Subscription cancellation failed.'
#     E0019 = 'Notification sending failed.'
#     E0020 = 'Settings update failed.'

#     def __str__(self):
#         return self.value


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
    E0021 = 'Failed to create category.'
    E0022 = 'Category not found.'
    E0023 = 'Failed to update category.'
    E0024 = 'Failed to delete category.'
    E0025 = 'Unexpected error occurred while deleting category.'
    E0026 = 'Failed to load products.'
    E0027 = 'Product not found.'
    E0028 = 'Failed to create product.'
    E0029 = 'Failed to update product.'
    E0030 = 'Product not found or could not be deleted.'
    E0031 = 'An unexpected error occurred.'

    def __str__(self):
        return self.value