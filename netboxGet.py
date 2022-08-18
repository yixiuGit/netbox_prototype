import pynetbox
import operator


class get_netbox_info:

    def __init__(self, netbox_ip, netbox_token):
        self.netbox_ip = netbox_ip
        self.token = netbox_token
        self.nb = pynetbox.api(self.netbox_ip, self.token)

    def check_existing_request(self, api_attr, obj_filter, filter_data):
        for obj in filter_data:
            return_object = operator.attrgetter(api_attr)(self.nb).filter(**{obj_filter: obj})

            if return_object:
                return True
            else:
                return False


