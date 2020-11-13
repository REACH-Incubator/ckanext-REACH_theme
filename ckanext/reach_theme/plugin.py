import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Reach_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')  
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'reach_theme')

    # IRoutes

    def before_map(self, map):
        map.connect('/privacy',
                    controller='ckanext.reach_theme.controller:ReachThemeController',
                    action='privacy')

        return map