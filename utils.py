import route53
from yaml import safe_load
import typer
app = typer.Typer(no_args_is_help=True, add_completion=False)


def load_config():
    with open('.config.yaml', 'r') as f:
        myyaml = safe_load(f)
    return myyaml


def connect():
    conf = load_config()
    conn = route53.connect(
        aws_access_key_id=conf['ACCESS_KEY'],
        aws_secret_access_key=conf['SECRET_KEY'],
    )
    return conn


@app.command('configtest')
def config_test():
    print(load_config())


@app.command('connecttest')
def connection_test():
    print(connect())


if __name__ == "__main__":
    app()
