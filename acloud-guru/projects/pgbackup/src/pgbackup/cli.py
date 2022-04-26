from argparse import ArgumentParser, Action


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser(
        description="""
        Backup pgsql database locally to S3 object storage
    """
    )

    parser.add_argument("url", help="URL of the database backup")
    parser.add_argument(
        "--driver",
        help="how & where to store backup",
        nargs=2,
        action=DriverAction,
        required=True,
    )
    return parser
