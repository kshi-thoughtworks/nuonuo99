import MySQLdb
from optparse import make_option
from django.core.management.base import BaseCommand
from django.conf import settings
import sys

class Command(BaseCommand):
    help = "Set mysql to utf-8 for DB and table columns"

    option_list = BaseCommand.option_list + (
        make_option("-H", "--host", dest="host", help="Host"),
        make_option("-u", "--user", dest="user", help="User"),
        make_option("-p", "--password", dest="password", help="Password"),
        make_option("-d", "--database", dest="database", help="Database"),
        )

    def handle(self, *args, **options):
        host = options["host"]
        user = options["user"]
        password = options["password"]
        database = options["database"]
        if host is None:
            host = settings.DATABASES.get("default").get("HOST")
        if user is None:
            user = settings.DATABASES.get("default").get("USER")
        if password is None:
            password = settings.DATABASES.get("default").get("PASSWORD")
        if database is None:
            database = settings.DATABASES.get("default").get("NAME")

        db = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("ALTER DATABASE `%s` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci'" % database)
        
        table_columns_varchar = {
            #Member: ["first_name", "last_name", "middle_name"],
        }

        for model, columns in table_columns_varchar.iteritems():
            for column in columns:
                sql = "ALTER TABLE {database}.{table} MODIFY COLUMN {column} VARCHAR({max_length}) CHARACTER SET utf8 COLLATE utf8_general_ci".format(
                    database=database, table=model._meta.db_table, column=column, max_length=model._meta.get_field_by_name(column)[0].max_length)
                cursor.execute(sql)
                print "column: {} in {}.{} is set to utf-8".format(column, database, model._meta.db_table)

