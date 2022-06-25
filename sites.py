import json, requests, pulumi

from flask import *
import pulumi.automation as auto
from pulumi_aws import s3

bp = Blueprint("sites",__name__,url_prefix="/sites")
