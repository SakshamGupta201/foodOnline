from accounts.models import CustomUser


def detect_user(user: CustomUser) -> str:
    if user.role == CustomUser.CUSTOMER:
        return "customerDashboard"
    elif user.role == CustomUser.VENDOR:
        return "vendorDashboard"
    elif user.role == None and user.is_superadmin:
        return "admin"
