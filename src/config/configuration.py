import toml

_config: dict = toml.load('./src/config.toml')

class Configuration:
    class Application:
        _app_config = _config.get('application', {})

        host: str = _app_config.get('host')
        port: int = _app_config.get('port')

    class Database:
        class PSQL:
            _psql_config = _config.get('database', {}).get('psql', {})

            connection_string: str = _psql_config.get('connection_string')

        psql = PSQL()

    application = Application()
    database = Database()

config = Configuration()