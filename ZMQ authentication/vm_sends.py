import logging
import os
import sys
import json
import zmq
import zmq.auth
from zmq.auth.thread import ThreadAuthenticator


def run():
    ''' Run Ironhouse example '''

    # These directories are generated by the generate_certificates script
    base_dir = os.path.dirname(__file__)
    keys_dir = os.path.join(base_dir, 'certificates')
    public_keys_dir = os.path.join(base_dir, 'public_keys')
    secret_keys_dir = os.path.join(base_dir, 'private_keys')

    if not (os.path.exists(keys_dir) and
            os.path.exists(public_keys_dir) and
            os.path.exists(secret_keys_dir)):
        logging.critical("Certificates are missing - run generate_certificates.py script first")
        sys.exit(1)

    ctx = zmq.Context.instance()

    # Start an authenticator for this context.
    auth = ThreadAuthenticator(ctx)
    auth.start()
    auth.allow('127.0.0.1')
    # Tell authenticator to use the certificate in a directory
    auth.configure_curve(domain='*', location=public_keys_dir)

    server = ctx.socket(zmq.PUSH)

    server_secret_file = os.path.join(secret_keys_dir, "server.key_secret")
    server_public, server_secret = zmq.auth.load_certificate(server_secret_file)
    server.curve_secretkey = server_secret
    server.curve_publickey = server_public
    server.curve_server = True  # must come before bind
    server.bind('tcp://*:9000')

    
    server_public_file = os.path.join(public_keys_dir, "server.key")
    server_public, _ = zmq.auth.load_certificate(server_public_file)
    # The client must know the server's public key to make a CURVE connection.
  

    server.send('{AdvisorId" : "71864", "Phone": "952-921-4972"}')

    

    

if __name__ == '__main__':
    if zmq.zmq_version_info() < (4,0):
        raise RuntimeError("Security is not supported in libzmq version < 4.0. libzmq version {0}".format(zmq.zmq_version()))

    if '-v' in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")

    run()
