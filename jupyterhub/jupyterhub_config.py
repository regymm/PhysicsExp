c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.DummyAuthenticator.password = "password"
c.JupyterHub.port = 443
c.JupyterHub.ssl_key = '/opt/myjupyterhub/jupyterhub.key'
c.JupyterHub.ssl_cert = '/opt/myjupyterhub/jupyterhub.crt'
from dockerspawner import DockerSpawner
c.DockerSpawner.image = 'regymm/jupyterhub:latest'
c.DockerSpawner.volumes = {
                    '/opt/myjupyterhub/shared/': '/home/riemann/shared'
                    
        }
c.DockerSpawner.remove = True
c.JupyterHub.spawner_class = DockerSpawner
import netifaces
docker0 = netifaces.ifaddresses('docker0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]
c.JupyterHub.hub_ip = docker0_ipv4['addr']
