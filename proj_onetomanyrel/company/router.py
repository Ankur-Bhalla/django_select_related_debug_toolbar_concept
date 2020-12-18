class CheckerRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'company':
            return 'mytestdb5'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'company':
            return 'mytestdb5'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'company' or obj2._meta.app_label == 'company':
            return True
        elif 'company' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'company':
            return db == 'mytestdb5'
        return None


