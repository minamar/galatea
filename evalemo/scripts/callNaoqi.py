#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use run Method"""

from django.core.management.base import BaseCommand, CommandError
import qi
import argparse
import sys
import runAnim


class Command(BaseCommand):

    help = "My test command"

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        # parser = argparse.ArgumentParser()
        # parser.add_argument("--ip", type=str, default="pepper.local",
        #                     help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
        # parser.add_argument("--port", type=int, default=9559,
        #                     help="Naoqi port number")

        # args = parser.parse_args()
        session = qi.Session()
        try:
            session.connect("tcp://pepper.local:9559")  #"tcp://" + args.ip + ":" + str(args.port))
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
                   "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)
        
        runAnim.main(session)