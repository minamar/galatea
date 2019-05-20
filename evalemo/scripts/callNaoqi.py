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

    def handle(self, *args, **options):

        session = qi.Session()

        try:
            session.connect("tcp://10.0.206.62:9559")  #"tcp://" + args.ip + ":" + str(args.port))
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
                   "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)
        
        runAnim.main(session)