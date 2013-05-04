#!/usr/bin/python2.7
#coding=utf-8

import MySQLdb

import sys

class StorageHelper:
    pass

class MysqlHelper(StorageHelper):
    host = "127.0.0.1"
    port = 3306
    username = "root"
    password = "hello1234"
    dbname = "pinbox"
    table_name = "table_site_link"
    conn = None
    cursor = None

    #def __init__(self, host=None, port=None, username, password):
    def __init__(self, username, password, host=None, port=None):
        if host:
            self.host = host
        if port:
            self.port = port
        self.username = username
        self.password = password

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.conn:
            self.conn.close()
            self.conn = None

    def connect(self, dbname):
        try:
            self.conn = MySQLdb.connect(host=self.host, user=self.username, passwd=self.password, port=self.port, charset='utf8')
            self.conn.select_db(self.dbname)
            self.cursor = self.conn.cursor()
            self.cursor.execute('SET CHARACTER SET utf8;')
            #self.cursor.execute("SET NAMES utf8")
            #self.cursor.execute("SET CHARACTER_SET_CLIENT=utf8")
            #self.cursor.execute("SET CHARACTER_SET_RESULTS=utf8")
            self.conn.commit()
            return True
        except MySQLdb.Error, e:
            print "mysql error %d: %s" % (e.args[0], e.args[1])
            return False
    
    def execute(self, cmd):
        try:
            self.cursor.execute(cmd)#.decode('utf8'))
            #self.cursor.commit()
            #results = self.cursor.fetchall()
            self.conn.commit()
            return True
        except MySQLdb.Error, e:
            print "mysql error %d: %s" % (e.args[0], e.args[1])
            return False

    def query(self, cmd):
        try:
            self.cursor.execute(cmd)#.decode('utf8'))
            results = self.cursor.fetchall()
            #self.conn.commit()
            return results
        except MySQLdb.Error, e:
            print "mysql error %d: %s" % (e.args[0], e.args[1])
            return None

def test_write_MysqlHelper1():
    storage = MysqlHelper(username="root", password="hello1234")
    if not storage.connect(storage.dbname):
        print "conn to %s error" % storage.dbname
        return False
    cmd = 'insert into table_site_link(name, link) values("%s", "%s")' % ('中国2', "nnn")
    if not storage.execute(cmd):
        print "execute to %s error" % storage.dbname
        return False
    print "execute to %s succ" % storage.dbname
    return True


def test_write_MysqlHelper2(value):
    storage = MysqlHelper(username="root", password="hello1234")
    if not storage.connect(storage.dbname):
        print "conn to %s error" % storage.dbname
        return False
    cmd = 'insert into table_site_link(name, link) values("%s", "%s")' % (value[0], value[1])
    if not storage.execute(cmd):
        print "execute to %s error" % storage.dbname
        return False
    print "execute to %s succ" % storage.dbname
    return True

def test_read_MysqlHelper():
    storage = MysqlHelper(username="root", password="hello1234")
    if not storage.connect(storage.dbname):
        print "conn to %s error" % storage.dbname
        return False
    results = storage.query('select * from table_site_link where link = "http://blog.csdn.net/haoel"')
    if not results:
        print "execute to %s error" % storage.dbname
        return False
    print "execute to %s succ" % storage.dbname
    print results
    return True

if __name__ == '__main__':
    test_read_MysqlHelper()   
    test_write_MysqlHelper1()
    #test_write_MysqlHelper2()
    #test_read_MysqlHelper()   
