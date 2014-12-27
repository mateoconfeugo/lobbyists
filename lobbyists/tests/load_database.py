import os
import os.path
import lobbyists
import lobbyists.util
import sys

def load(dir, db_path):
    files = sorted(os.listdir(dir), reverse=True)
    for file in files:
        fp = dir + file
        if os.path.exists(fp):
            try:
                lobbyists.util.load_db([fp], db_path)
                print dir + file
            except KeyError:
                print "KeyError:", sys.exc_info()[0]
            except IOError as (errno, strerror):
                print "I/O error({0}): {1}".format(errno, strerror)
            except ValueError:
                print "Could not convert data to an integer."
            except:
                print "Unexpected error:", sys.exc_info()[0]


if __name__ == "__main__":
    dir = '/home/pair/github/ltd/resources/downloads/lobby_db/'
    db_path = '/home/pair/github/ltd/new-ltd.db'
    load(dir, db_path)
