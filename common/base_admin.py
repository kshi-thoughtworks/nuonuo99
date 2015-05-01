class BaseAdmin(object):
    reversion_enable = True
    list_per_page = 10
    list_filter = ("nn_created_at", "nn_status")
        
    
