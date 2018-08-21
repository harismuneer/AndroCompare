import sys

sys.path.insert(0, './libs/')

from apk import APK
import sqlite3
from hurry.filesize import size

database = "results.sqlite"

conn = sqlite3.connect(database)
cur = conn.cursor()

try:
    # change the paths to the relevant apps to be compared
    apk1_path = "./app1.apk"
    apk2_path = "./app2.apk"

    app1 = apk1_path.split('/')[-1]
    app2 = apk2_path.split('/')[-1]

    # insert apps into database
    cur.execute("INSERT OR IGNORE INTO APPS VALUES (?,?,NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "
                "NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "
                "NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)",
                (app1, app2))

    apk1 = APK(apk1_path)
    apk2 = APK(apk2_path)

    # ----------version-------------------
    a_v1 = apk1.get_androidversion_name()
    a_v2 = apk1.get_androidversion_code()

    b_v1 = apk2.get_androidversion_name()
    b_v2 = apk2.get_androidversion_code()

    cur.execute(
        'Update apps set app1_version_name = ?, app1_version_code = ?, app2_version_name = ?, app2_version_code = ? '
        'where app1_name = ? and app2_name = ?', (a_v1, a_v2, b_v1, b_v2, app1, app2))

    # ----------cert-------------------
    a_c = apk1.cert_text
    b_c = apk2.cert_text

    cert_diff = "True"

    if a_c == b_c:
        cert = "False"

    cur.execute('Update apps set app1_cert = ?, app2_cert = ?, cert_same = ? where app1_name = ? and app2_name = ?',
                (a_c, b_c, cert, app1, app2))

    # ----------package name-------------------
    a_c = apk1.package
    b_c = apk2.package

    cur.execute('Update apps set app1_package = ?, app2_package = ? where app1_name = ? and app2_name = ?',
                (a_c, b_c, app1, app2))

    # ----------permissions-------------------
    p1_d = apk1.get_permissions()
    p2_d = apk2.get_permissions()

    p1 = set(p1_d)
    p2 = set(p2_d)

    t1 = p1.difference(p2)  # in p1 but not in p2 (removed in p2)
    t2 = p2.difference(p1)  # in p1 but in p1 (added in p2)
    t3 = p1.intersection(p2)  # in both

    add_count = len(t2)
    added = ",".join(t2)
    removed = ",".join(t1)
    same = ",".join(t3)

    cur.execute(
        'Update apps set perm_added = ?, perm_removed=?, perm_same=?, perm_add_count=? where app1_name=? and app2_name = ?',
        (added, removed, same, add_count, app1, app2))

    # ----------activities-------------------
    p1_d = apk1.get_activities()
    p2_d = apk2.get_activities()

    p1 = set(p1_d)
    p2 = set(p2_d)

    t1 = p1.difference(p2)  # in p1 but not in p2 (removed in p2)
    t2 = p2.difference(p1)  # in p1 but in p1 (added in p2)
    t3 = p1.intersection(p2)  # in both

    added = ",".join(t2)
    removed = ",".join(t1)
    same = ",".join(t3)

    cur.execute(
        'Update apps set activities_added = ?, activities_removed=?, same_activities=? where app1_name=? and app2_name = ?',
        (added, removed, same, app1, app2))

    # ----------services-------------------
    p1_d = apk1.get_services()
    p2_d = apk2.get_services()

    p1 = set(p1_d)
    p2 = set(p2_d)

    t1 = p1.difference(p2)  # in p1 but not in p2 (removed in p2)
    t2 = p2.difference(p1)  # in p1 but in p1 (added in p2)
    t3 = p1.intersection(p2)  # in both

    added = ",".join(t2)
    removed = ",".join(t1)
    same = ",".join(t3)

    cur.execute(
        'Update apps set services_added = ?, services_removed=?, same_services=? where app1_name=? and app2_name = ?',
        (added, removed, same, app1, app2))

    # ----------receivers-------------------
    p1_d = apk1.get_receivers()
    p2_d = apk2.get_receivers()

    p1 = set(p1_d)
    p2 = set(p2_d)

    t1 = p1.difference(p2)  # in p1 but not in p2 (removed in p2)
    t2 = p2.difference(p1)  # in p1 but in p1 (added in p2)
    t3 = p1.intersection(p2)  # in both

    added = ",".join(t2)
    removed = ",".join(t1)
    same = ",".join(t3)

    cur.execute(
        'Update apps set receivers_added = ?, receivers_removed=?, same_receivers=? where app1_name=? and app2_name = ?',
        (added, removed, same, app1, app2))

    # ----------providers-------------------
    p1_d = apk1.get_providers()
    p2_d = apk2.get_providers()

    p1 = set(p1_d)
    p2 = set(p2_d)

    t1 = p1.difference(p2)  # in p1 but not in p2 (removed in p2)
    t2 = p2.difference(p1)  # in p1 but in p1 (added in p2)
    t3 = p1.intersection(p2)  # in both

    added = ",".join(t2)
    removed = ",".join(t1)
    same = ",".join(t3)

    cur.execute(
        'Update apps set providers_added = ?, providers_removed=?, same_providers=? where app1_name=? and app2_name = ?',
        (added, removed, same, app1, app2))

    # ----------size-------------------
    f1 = size(apk1.file_size)
    f2 = size(apk2.file_size)

    cur.execute('Update apps set app1_size = ?, app2_size=? where app1_name=? and app2_name = ?', (f1, f2, app1, app2))

    # ----------main_activity-------------------
    a1 = apk1.get_main_activity()
    a2 = apk2.get_main_activity()

    if a1 == a2:
        same = "same"
    else:
        same = "diff"

    cur.execute(
        'Update apps set app1_main_activity = ?, app2_main_activity = ?, main_activity_diff = ?, '
        'perm_analysis=1 where app1_name=? and app2_name = ?'
        , (a1, a2, same, app1, app2))

    print("----------------")
    print("Done")
    print("----------------")

    conn.commit()
    conn.close()

except Exception as e:
    print("Error!")
    print(e.message)
