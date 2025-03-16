import os

from src.model.setting_model import SettingModel, SettingModelEnvironment


def get_setting() -> SettingModel:
    """
    Retrieve the setting model.

    Returns:
        SettingModel: The setting model object.
    """
    try:
        setting_model = SettingModel()
        return setting_model
    except Exception as e:
        setting_model_environment = SettingModelEnvironment()
        return setting_model_environment
