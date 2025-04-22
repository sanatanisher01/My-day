"""
Custom migration questioner that always returns default values.
This is used to avoid interactive prompts during migrations.
"""
from django.db.migrations.questioner import InteractiveMigrationQuestioner


class NonInteractiveMigrationQuestioner(InteractiveMigrationQuestioner):
    """
    A migration questioner that always returns default values.
    """
    def ask_not_null_addition(self, field_name, model_name):
        """
        Always return empty string as default value for not null fields.
        """
        return ""
    
    def ask_not_null_alteration(self, field_name, model_name):
        """
        Always return empty string as default value for not null alterations.
        """
        return ""
    
    def ask_rename(self, model_name, old_name, new_name, field_instance):
        """
        Always return False for rename questions.
        """
        return False
    
    def ask_rename_model(self, old_model_state, new_model_state):
        """
        Always return False for model rename questions.
        """
        return False
    
    def ask_merge(self, app_label):
        """
        Always return True for merge questions.
        """
        return True


# Create an instance to use in settings
questioner = NonInteractiveMigrationQuestioner()
