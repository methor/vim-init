"-----------------------------------------------------------------
" 缩写定义
" ----------------------------------------------------------------
iabbrev py_thrift_header # coding=utf8<cr>from pyutil.springdb import SpringDBClient<cr>from pyutil.pyredis.redis_client import RedisClient<cr>import os, sys<cr>import MySQLdb<cr>from sqlalchemy import Column, String, create_engine<cr>from pyutil.thrift.thrift_client import ThriftRetryClient<cr>from hashmobile_pyrpc.thrift_gen.toutiao.user.hash_mobile.HashMobileService import Client<cr>from hashmobile_pyrpc.thrift_gen.toutiao.user.hash_mobile.ttypes import GetMobileIdByMobileRequest<cr>from service_rpc.thrift_gen.base.ttypes import Base
