import toml
from os.path import abspath, dirname, join
from pathlib import Path

_current_file_dir = dirname(abspath(__file__))
ROOT_DIR: str = Path(_current_file_dir).parent.absolute()

_config: dict = toml.load(join(ROOT_DIR, 'config.toml'))

class Configuration:
    class Application:
        _app_config = _config.get('application', {})

        host: str = _app_config.get('host')
        port: int = _app_config.get('port')
        debug: bool = _app_config.get('debug')

    class Database:
        class PSQL:
            _psql_config = _config.get('database', {}).get('psql', {})

            connection_string: str = _psql_config.get('connection_string')

        psql = PSQL()

    application = Application()
    database = Database()

config = Configuration()