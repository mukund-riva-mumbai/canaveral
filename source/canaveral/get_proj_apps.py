
import ledger.db_connect as dbc
import ledger.db_query as dbq


def get_proj_info():
    proj_list = []
    riva_db = dbc.RivaDatabase("gfx61", dbuser="riva-root", passwd="RXppb09uQVRodXJzZGF5")
    riva_db.connect()
    databases = riva_db.query("SHOW DATABASES")
    riva_db.close()

    ignore_db_list = ["information_schema", "mysql", "performance_schema"]

    for each in databases:
        if not each.get("Database") in ignore_db_list:
            proj_list.append(each.get("Database"))

    return proj_list


def get_app_info(proj):
    master_app_dict = {}

    riva_db = dbc.RivaDatabase("gfx61", dbuser="riva-root", dbname=proj, passwd="RXppb09uQVRodXJzZGF5")
    app_query = dbq.generate_query_str(["appid", "appname", "appversion", "defaultapplocation", "isrenderer"], ["apps"])
    result = []
    try:
        riva_db.connect()
        result = riva_db.query(app_query)
    except:
        print "An exception occured."
    finally:
        riva_db.close()

    for each in result:
        app_vars = {}
        if each.get("appname") not in master_app_dict.keys():
            master_app_dict[each.get("appname")] = []
        app_vars["id"] = int(each.get("appid"))
        app_vars["version"] = each.get("appversion")
        app_vars["location"] = each.get("defaultapplocation")
        app_vars["isrenderer"] = each.get("isrenderer")
        master_app_dict[each.get("appname")].append(app_vars)

    return master_app_dict