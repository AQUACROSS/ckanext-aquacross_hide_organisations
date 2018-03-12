import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic

def organization_list(context, data_dict=None):
    data = logic.action.get.organization_list(context, data_dict)
    data_len = len(data)
    for i in range(data_len):
        if( 'name' in data[i] and data[i]['name'] == 'qc'):
            # expected when 'all_fields'is True in data_dict
            del data[i]
            return data
        elif( data[i] == 'qc' ):
            # expected when 'all_fields'is False in data_dict
            del data[i]
            return data
    return data

class Aquacross_Hide_OrganisationsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'aquacross_hide_organisations')

    def get_actions(self):
        return {'organization_list': organization_list}
