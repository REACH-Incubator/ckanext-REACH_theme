import ckan.plugins.toolkit as toolkit

class ReachThemeController(toolkit.BaseController):

    def privacy(self):
        return toolkit.render('reach/privacy.html')