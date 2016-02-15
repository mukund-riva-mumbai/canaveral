import os
import subprocess

import ledger.db_connect as dbc
import ledger.db_query as dbq


def set_env_vars(proj, master_app_dict={}, app_name="", app_ver="", ren_name="", ren_ver="", set_env=True):
    def_app = master_app_dict.get(app_name)

    env_set_cmd = ""
    env_set_cmd += "set %s=%s\n" % ("PROJECT_NAME", proj.upper())
    if set_env:
        os.environ["PROJECT_NAME"] = proj.upper()

    app_id = 1
    for each in def_app:
        if each.get("version") == app_ver:
            app_id = each.get("id")
            env_set_cmd += "set %s=%s\n" % (app_name.upper() + "_VER", str(each.get("version")))
            env_set_cmd += "set %s=%s\n" % (app_name.upper() + "_LOC", str(each.get("location")))
            if set_env:
                os.environ[app_name.upper() + "_VER"] = str(each.get("version"))
                os.environ[app_name.upper() + "_LOC"] = str(each.get("location"))

        if ren_name:
            env_set_cmd += "set %s=%s\n" % ("RENDERER", ren_name.upper())
            env_set_cmd += "set %s=%s\n" % (ren_name.upper() + "_VER", ren_ver)
            if set_env:
                os.environ["RENDERER"] = ren_name.upper()
                os.environ[ren_name.upper() + "_VER"] = ren_ver
            for each_renderer in master_app_dict[ren_name]:
                if each_renderer.get("version") == ren_ver:
                    env_set_cmd += "set %s=%s\n" % (ren_name.upper() + "_LOC", each_renderer.get("location"))
                    if set_env:
                        os.environ[ren_name.upper() + "_LOC"] = each_renderer.get("location")

    app_var_query = dbq.generate_query_str(["variablename", "variablevalue"], ["app_variables"], where_and=[("appid", "=", str(app_id))])
    riva_db = dbc.RivaDatabase("gfx61", dbuser="riva-root", dbname=proj, passwd="RXppb09uQVRodXJzZGF5")
    result = []
    try:
        riva_db.connect()
        result = riva_db.query(app_var_query)
    except:
        print "An exception occured."
    finally:
        riva_db.close()

    for each in result:
        var_decl = str(each["variablevalue"])
        if var_decl == "":
            continue
        if ("%RENDERER_VER%" in var_decl):
            var_decl = var_decl.replace("%RENDERER_VER%", ren_ver)
        if ("%" + app_name.upper() + "_VER%" in var_decl):
            var_decl = var_decl.replace("%" + app_name.upper() + "_VER%", app_ver)
        env_set_cmd += "set %s=%s\n" % (str(each["variablename"]), var_decl)
        if set_env:
            os.environ[str(each["variablename"])] = var_decl

    return env_set_cmd


def launch_app(proj, master_app_dict={}, app_name="", app_ver="", ren_name="", ren_ver="", app_arg_str=""):
    set_env_vars(proj, master_app_dict, app_name, app_ver, ren_name, ren_ver)
    launch_params = os.getenv(app_name.upper() + "_LOC")
    if app_arg_str:
        launch_params += " " + app_arg_str
    subprocess.Popen(launch_params)