# Alerts © 2024
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


# [Hooks]
def extend(bootinfo):
    import frappe
    from frappe import _
    
    from .alert import get_alerts_cache
    from .common import log_error
    
    try:
        bootinfo.alerts = get_alerts_cache(frappe.session.user)
    except Exception:
        log_error(_(
            "An error has occurred while getting cached alerts on boot."
        ))
