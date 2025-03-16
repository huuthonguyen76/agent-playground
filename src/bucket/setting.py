from src.model.setting_model import SettingModel


def get_setting() -> SettingModel:
    """
    Retrieve the setting model.

    Returns:
        SettingModel: The setting model object.
    """
    setting_model = SettingModel()
    return setting_model
