import os

from ubuntutweak.janitor import JanitorCachePlugin
from ubuntutweak.settings.configsettings import RawConfigSetting

class MozillaCachePlugin(JanitorCachePlugin):
    __category__ = 'application'

    targets = ['Cache',
               'OfflineCache',
               'TestPilotErrorLog.log',
               'downloads.sqlite',
               'cookies.sqlite',
               'cookies.sqlite-shm',
               'cookies.sqlite-wal']
    app_path = ''

    @classmethod
    def get_path(cls):
        profiles_path = os.path.expanduser('%s/profiles.ini' % cls.app_path)
        if os.path.exists(profiles_path):
            config = RawConfigSetting(profiles_path)
            profile_id = config.get_value('General', 'StartWithLastProfile')
            for section in config.sections():
                if section.startswith('Profile'):
                    relative_id = config.get_value(section, 'IsRelative')
                    if relative_id == profile_id:
                        return os.path.expanduser('%s/%s' % (cls.app_path, config.get_value(section, 'Path')))
        return cls.root_path


class FirefoxCachePlugin(MozillaCachePlugin):
    __title__ = _('Firefox Cache')

    app_path = '~/.mozilla/firefox'

class ThunderbirdCachePlugin(MozillaCachePlugin):
    __title__ = _('Thunderbird Cache')

    app_path = '~/.thunderbird'
