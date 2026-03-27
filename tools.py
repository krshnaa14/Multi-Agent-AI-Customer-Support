def get_refund_policy():
    return "Refunds are allowed within 30 days of purchase."

def get_shipping_info():
    return "Shipping takes 5-7 days (standard), 1-2 days (express)."

def reset_password():
    return "Click 'Forgot Password' on login page."

def escalate():
    return "Escalated to human support."

TOOLS = {
    "get_refund_policy": get_refund_policy,
    "get_shipping_info": get_shipping_info,
    "reset_password": reset_password,
    "escalate": escalate
}