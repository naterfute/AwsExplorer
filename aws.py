from utils import connect
import typer

app = typer.Typer(no_args_is_help=True, add_completion=False)

conn = connect()


@app.command('getZones')
def get_zones():
    for zone in conn.list_hosted_zones():
        # You can then do various things to the zone.
        print(zone.name)

        # Perhaps you want to see the record sets under this zone
        for record_set in zone.record_sets:
            print(record_set)


@app.command('retrieve')
def retrieve_hosted_zone(zoneid: str):
    zone = conn.get_hosted_zone_by_id(zoneid)
    print(zone)


if __name__ == "__main__":
    app()
