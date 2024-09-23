import route53
from yaml import safe_load
import typer
app = typer.Typer(no_args_is_help=True, add_completion=False)


class awsClass:
    def __init__(self):
        self.config = self.load_config()
        self.connect()

    def load_config(self):
        with open('.config.yaml', 'r') as f:
            myyaml = safe_load(f)
        return myyaml

    def connect(self):
        conn = route53.connect(
            aws_access_key_id=self.config['ACCESS_KEY'],
            aws_secret_access_key=self.config['SECRET_KEY'],
        )
        self.conn = conn
        return conn

    def get_hosted_zone(self):
        self.zone = self.conn.get_hosted_zone_by_id(self.config['ZONEID'])
        return self.zone


@app.command('configtest')
def config_test():
    testing = awsClass()
    print(testing.config)


@app.command('connecttest')
def connection_test():
    testing = awsClass()
    print(testing.conn)


@app.command('hostedTest')
def hosted_zone_test():
    testing = awsClass()
    print(testing.get_hosted_zone())


if __name__ == "__main__":
    app()
