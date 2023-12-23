from zoodb import ZooDB


def main():
    Zoodb = ZooDB()
    Zoodb.connect_to_DB()
    Zoodb.create_all_tables()


if __name__ == '__main__':
    main()