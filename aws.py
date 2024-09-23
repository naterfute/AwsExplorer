from utils import awsClass
import typer

app = typer.Typer(no_args_is_help=True, add_completion=False)

aws = awsClass()


@app.command('getZones')
def get_zones():
    for zone in aws.conn.list_hosted_zones():
        # You can then do various things to the zone.
        print(zone.name)

        # Perhaps you want to see the record sets under this zone
        for record_set in zone.record_sets:
            print(record_set)


@app.command('retrieve')
def retrieve_hosted_zone(zoneid: str):
    zone = aws.conn.get_hosted_zone_by_id(zoneid)
    print(zone)
    return zone


@app.command('getRecordSet')
def get_record_set(name_to_match: str):

    for record_set in aws.get_hosted_zone().record_sets:
        if record_set.name == name_to_match:
            print(record_set)
            # Stopping early may save some additional HTTP requests,
            # since zone.record_sets is a generator.
            break


if __name__ == "__main__":
    app()
