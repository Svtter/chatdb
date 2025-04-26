from invoke import task

from utils import get_engine


@task
def create(c):
  """create database file"""
  get_engine()


@task
def migrate(c):
  """migrate database"""
  # get_engine(c.db_path)
  raise NotImplementedError("not implemented")
